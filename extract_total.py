import re
import PyPDF2

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
                return f"${match.group(1)}"
            else:
                return "Total not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    pdf_path = "invoice.pdf"  # Replace with the path to your PDF file
    total = extract_invoice_total(pdf_path)
    print(f"Extracted Total: {total}")
