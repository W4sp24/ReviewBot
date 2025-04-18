from Gemini import Gemini
from file_system import PDFFileHandler

gemini = Gemini()

print(gemini.generate_response("What is the capital of philippines" ))

reader = PDFFileHandler()

sample_reviwer = reader.read_file("C:/Users/ethan/Downloads/ICS-2606-Module-5.pdf")

print(gemini.generate_response(sample_reviwer + "Create A study Guide for this document"))