from Gemini import Gemini
from file_system import PDFFileHandler, TextFileHandler, TextFormatter
from promts import BloomTaxonomy

gemini = Gemini()

print(gemini.generate_response("What is the capital of philippines" ))

PDF = PDFFileHandler()
writer = TextFileHandler()
format = TextFormatter()

sample_reviewer = PDF.read_file("C:/Users/ethan/Downloads/ICS-2606-Module-5.pdf")
promt = BloomTaxonomy()

promt_design =promt.remembering(sample_reviewer)

output_file_path = r"D:\Test Files\output.pdf"  # Specify a file name in the path
PDF.write_lines_to_pdf(output_file_path, format.bulleted_format(gemini.generate_response(promt_design)))