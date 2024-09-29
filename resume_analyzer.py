# import os
# from pdfminer.high_level import extract_text

# def search_keywords_in_pdfs(folder_path, keywords):
#     try:
#         # Iterate over each file in the specified folder
#         for filename in os.listdir(folder_path):
#             if filename.endswith(".pdf"):
#                 file_path = os.path.join(folder_path, filename)
#                 print(f"\nSearching in file: {file_path}")

#                 # Extract text from the PDF file
#                 text = extract_text(file_path)

#                 # Check if any of the keywords are present in the extracted text
#                 if any(keyword.lower() in text.lower() for keyword in keywords):
#                     print(f"Keyword(s) found in {filename}")

#     except Exception as e:
#         print(f"Error: {e}")

# # Example usage:
# pdf_folder_path = "/home/melanee/Downloads"
# search_keywords = ["python", "programming", "example"]

# search_keywords_in_pdfs(pdf_folder_path, search_keywords)
#------------------------------------------------------------------------------------------------------
# import os
# from pdfminer.high_level import extract_text

# def count_keyword_occurrences(file_path, keyword):
#     try:
#         # Extract text from the PDF file
#         text = extract_text(file_path)

#         # Count the occurrences of the keyword in the extracted text
#         occurrences = text.lower().count(keyword.lower())

#         print(f"Occurrences of '{keyword}' in {file_path}: {occurrences}")

#     except Exception as e:
#         print(f"Error: {e}")

# # Example usage:
# pdf_file_path = "/home/melanee/Downloads/resume.pdf"
# search_keyword = "data"

# count_keyword_occurrences(pdf_file_path, search_keyword)

#----------------------------------------------------------------------------
import os
from pdfminer.high_level import extract_text

def count_keywords_occurrences(file_path, keywords):
    try:
        # Extract text from the PDF file
        text = extract_text(file_path)

        # Convert the extracted text and keywords to lowercase for case-insensitive search
        text_lower = text.lower()

        # Count occurrences for each keyword
        occurrences = {keyword: text_lower.count(keyword.lower()) for keyword in keywords}

        # Print the results
        print(f"\nOccurrences in {file_path}:")
        for keyword, count in occurrences.items():
            print(f"'{keyword}': {count} times")

    except Exception as e:
        print(f"Error: {e}")

# Example usage:
pdf_file_path = "/home/melanee/Downloads/resume.pdf"
search_keywords = ["python", "programming", "example"]

count_keywords_occurrences(pdf_file_path, search_keywords)

#-----------------------------------------------------------------------------------------

# import os
# from pdfminer.high_level import extract_text

# def calculate_weighted_average(file_path, keyword_weights):
#     try:
#         # Extract text from the PDF file
#         text = extract_text(file_path)

#         # Convert the extracted text to lowercase for case-insensitive search
#         text_lower = text.lower()

#         # Initialize variables for weighted sum and total occurrences
#         weighted_sum = 0
#         total_occurrences = 0

#         # Calculate weighted sum and total occurrences for each keyword
#         for keyword, weight in keyword_weights.items():
#             keyword_lower = keyword.lower()
#             occurrences = text_lower.count(keyword_lower)
#             weighted_sum += weight * occurrences
#             total_occurrences += occurrences

#         # Calculate the weighted average for each keyword
#         weighted_averages = {keyword: (weighted_sum / total_occurrences) if total_occurrences > 0 else 0
#                              for keyword in keyword_weights}

#         # Print the results
#         print(f"\nWeighted Averages in {file_path}:")
#         for keyword, average in weighted_averages.items():
#             print(f"'{keyword}': {average}")

#     except Exception as e:
#         print(f"Error: {e}")

# # Example usage:
# pdf_file_path = "/home/melanee/Downloads/resume.pdf"
# keyword_weights = {"python": 2, "programming": 1, "example": 3}

# calculate_weighted_average(pdf_file_path, keyword_weights)


#-------------------------------------------------------------------

# import os
# import PyPDF2

# def search_keywords_in_pdfs(folder_path, keywords):
#     try:
#         # Iterate over each file in the specified folder
#         for filename in os.listdir(folder_path):
#             if filename.endswith(".pdf"):
#                 file_path = os.path.join(folder_path, filename)
#                 print(f"\nSearching in file: {file_path}")

#                 # Open the PDF file in binary mode
#                 with open(file_path, 'rb') as file:
#                     # Create a PDF reader object
#                     pdf_reader = PyPDF2.PdfReader(file)

#                     # Iterate through each page and search for keywords
#                     for page_num in range(pdf_reader.numPages):
#                         page = pdf_reader.getPage(page_num)
#                         text = page.extractText()

#                         # Check if any of the keywords are present on the page
#                         if any(keyword.lower() in text.lower() for keyword in keywords):
#                             print(f"Keyword(s) found on page {page_num + 1} of {filename}")

#     except Exception as e:
#         print(f"Error: {e}")

# # Example usage:
# pdf_folder_path = "/home/melanee/Downloads"
# search_keywords = ["python", "programming", "example"]

# search_keywords_in_pdfs(pdf_folder_path, search_keywords)


