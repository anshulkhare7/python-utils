import requests
from bs4 import BeautifulSoup

# List of years to scrape
years = list(range(1977, 1998))

# Initialize an empty list to store the text content
all_text = []

# Loop through each year and download the text
for year in years:
    url = f"https://www.berkshirehathaway.com/letters/{year}.html"
    print(f"Downloading text for {year}...")

    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Extract the text content from the webpage
            text = soup.get_text()
            all_text.append(text)
            print(f"Successfully downloaded text for {year}")
        else:
            print(f"Error fetching data for {year}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading text for {year}: {e}")
        continue

# Combine all the text content into a single string
combined_text = "\n\n".join(all_text)

# Write the combined text to a file
with open("website_text.txt", "w", encoding="utf-8") as file:
    file.write(combined_text)

print("Text content saved to 'website_text.txt'.")