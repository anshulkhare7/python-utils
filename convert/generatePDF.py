import os
import random
from fpdf import FPDF

def generate_pdf(file_path, size_kb):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    # Add some text content to the PDF
    pdf.cell(200, 10, txt="Sample PDF content", ln=True, align='C')

    # Save the PDF file
    pdf.output(file_path)

    # Adjust the file size
    with open(file_path, 'ab') as f:
        current_size = os.path.getsize(file_path)
        target_size = size_kb * 1024
        if current_size < target_size:
            # Add padding to reach the target size
            f.write(b'0' * (target_size - current_size))

def generate_sample_pdfs(prefix, min_size_kb, max_size_kb, num_files=100, folder="output"):
    # Create the folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)
    
    for i in range(num_files):
        size_kb = random.randint(min_size_kb, max_size_kb)
        file_name = f"{prefix}_{size_kb}KB_{i+1}.pdf"
        file_path = os.path.join(folder, file_name)
        generate_pdf(file_path, size_kb)
        print(f"Generated: {file_path} of size {size_kb} KB")

# Example usage: Specify folder where the files will be created
generate_sample_pdfs(prefix="sample", min_size_kb=100, max_size_kb=1024, num_files=25, folder="/Users/anshul/tmp/s3")