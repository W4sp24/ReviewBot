from Gemini import Gemini
from file_system import PDFFileHandler, TextFileHandler, TextFormatter
from promts import BloomTaxonomy
import os

gemini = Gemini()

PDF = PDFFileHandler()
writer = TextFileHandler()
format = TextFormatter()
Bloom = BloomTaxonomy()

# Hardcoded file path
file_path = r"D:\Google downloads\TOP-PT.-5-6.pdf"

file_contents = PDF.read_file(file_path)

full_promnt = Bloom.remembering(file_contents)


response = gemini.generate_response(full_promnt)
# Hardcoded output path
output_file_path = r"D:\Test Files\output-ni-khen-3.pdf"

PDF.write_lines_to_pdf(output_file_path, format.bulleted_format(response))

