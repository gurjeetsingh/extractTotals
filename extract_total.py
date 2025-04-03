import re
import PyPDF2
import os

def extract_invoice_total(pdf_path):
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            
            # Extract text from all pages
            for page in reader.pages:
                text += page.extract_text()
            
            # Search for the total after "Invoice Subtotal"
            match = re.search(r"Invoice Subtotal\s*\$([0-9]+\.[0-9]{2})", text)
            if match:
                return float(match.group(1))
            else:
                return None
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return None

def extract_and_sum_totals(directory):
    total_sum = 0.0
    for file_name in os.listdir(directory):
        if file_name.lower().endswith('.pdf'):
            pdf_path = os.path.join(directory, file_name)
            total = extract_invoice_total(pdf_path)
            if total is not None:
                total_sum += total
            else:
                print(f"Total not found in {pdf_path}")
    return total_sum

# Example usage
if __name__ == "__main__":
    directory = "."  # Replace with your directory path if needed
    total_sum = extract_and_sum_totals(directory)
    print(f"Total Sum: ${total_sum:.2f}")
