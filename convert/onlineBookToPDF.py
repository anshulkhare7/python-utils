import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import networkx as nx

class WebsiteToPDFConverter:
    def __init__(self, base_url):
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc
        self.graph = nx.DiGraph()
        self.content = []
        self.styles = getSampleStyleSheet()
        
        # Set up Selenium WebDriver
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_soup(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        return BeautifulSoup(self.driver.page_source, 'html.parser')

    def extract_content(self, url, soup):
        main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content')
        if main_content:
            for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'img']):
                if element.name.startswith('h'):
                    self.content.append(Paragraph(element.text, self.styles[element.name]))
                elif element.name == 'p':
                    self.content.append(Paragraph(element.text, self.styles['Normal']))
                elif element.name == 'img':
                    img_url = urljoin(url, element['src'])
                    try:
                        img_data = BytesIO(requests.get(img_url).content)
                        img = Image(img_data, width=300, height=200)
                        self.content.append(img)
                    except Exception as e:
                        print(f"Error processing image {img_url}: {e}")
                self.content.append(Spacer(1, 12))

    def build_site_graph(self, url, parent=None):
        if url in self.graph:
            return

        print(f"Mapping: {url}")
        self.graph.add_node(url)
        if parent:
            self.graph.add_edge(parent, url)

        soup = self.get_soup(url)
        nav_menu = soup.find('nav') or soup.find('ul', class_='menu')
        
        if nav_menu:
            for link in nav_menu.find_all('a', href=True):
                next_url = urljoin(url, link['href'])
                if next_url.startswith(self.base_url) and self.domain in next_url:
                    self.build_site_graph(next_url, url)

    def process_site(self):
        self.build_site_graph(self.base_url)
        
        for url in nx.dfs_preorder_nodes(self.graph, self.base_url):
            print(f"Processing: {url}")
            soup = self.get_soup(url)
            self.extract_content(url, soup)

    def create_pdf(self, output_filename):
        doc = SimpleDocTemplate(output_filename, pagesize=letter)
        doc.build(self.content)

    def cleanup(self):
        self.driver.quit()

def main():
    base_url = input("Enter the base URL of the website: ")
    output_filename = input("Enter the output PDF filename: ")
    
    converter = WebsiteToPDFConverter(base_url)
    try:
        converter.process_site()
        converter.create_pdf(output_filename)
        print(f"PDF created: {output_filename}")
    finally:
        converter.cleanup()

if __name__ == "__main__":
    main()