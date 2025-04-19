from abc import ABC, abstractmethod
import PyPDF2
from reportlab.pdfgen import canvas  # Import ReportLab for PDF writing
import os  # Import os for terminal download functionality
import shutil  # Import shutil for file operations
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class FileHandler(ABC):
    @abstractmethod
    def read_file(self, filepath: str) -> str:
        pass

    @abstractmethod
    def write_file(self, filepath: str, content: str):
        pass


class TextFileHandler(FileHandler):
    def read_file(self, filepath: str) -> str:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()

    def write_file(self, filepath: str, content: str):
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)


class PDFFileHandler(FileHandler):
    def read_file(self, filepath: str) -> str:
        """
        Read the content of a PDF file and return it as a string.
        """
        from textwrap import fill
        with open(filepath, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            full_text = ""
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                formatted_text = fill(text if text else "[No extractable text]", width=80)
                full_text += f"\n\n--- Page {i + 1} ---\n\n{formatted_text}"
            return full_text

    def write_file(self, filepath: str, content: str):
        """
        Write a string of content to a PDF file using ReportLab.
        """
        # Split the content into lines and write to PDF
        lines = content.splitlines()
        self.write_lines_to_pdf(filepath, lines)

    def write_lines_to_pdf(self, filepath: str, lines: list):
        """
        Write a list of lines to a PDF file using ReportLab.
        Key terms (text before the first hyphen) are rendered in bold.
        """
        # Register the Arial font and its bold variant
        pdfmetrics.registerFont(TTFont("Arial", "arial.ttf"))
        pdfmetrics.registerFont(TTFont("Arial-Bold", "arialbd.ttf"))

        pdf = canvas.Canvas(filepath)
        pdf.setFont("Arial", 12)  # Set font to Arial

        # Define margins and spacing
        left_margin = 50
        top_margin = 800
        line_spacing = 25  # Adjust this value to change the line spacing
        max_width = 500  # Maximum width for text wrapping

        y_position = top_margin

        for line in lines:
            # Split the line into key term and the rest of the text
            if " - " in line:
                key_term, rest_of_line = line.split(" - ", 1)
            else:
                key_term, rest_of_line = line, ""

            # Render the key term in bold
            pdf.setFont("Arial-Bold", 12)
            key_term_width = pdf.stringWidth(key_term + " ", "Arial-Bold", 12)
            pdf.drawString(left_margin, y_position, key_term)

            # Render the rest of the line in regular font
            pdf.setFont("Arial", 12)
            pdf.drawString(left_margin + key_term_width, y_position, f"- {rest_of_line}")

            # Move to the next line
            y_position -= line_spacing
            if y_position < 50:  # Prevent writing outside the page
                pdf.showPage()
                pdf.setFont("Arial", 12)  # Reset font on new page
                y_position = top_margin
        pdf.save()

    @staticmethod
    def _wrap_text(text: str, pdf: canvas.Canvas, max_width: int) -> list:
        """
        Wrap text to fit within the specified max_width.
        Returns a list of wrapped lines.
        """
        words = text.split()
        wrapped_lines = []
        current_line = ""

        for word in words:
            # Check if adding the word exceeds the max_width
            if pdf.stringWidth(current_line + " " + word, "Helvetica", 12) > max_width:
                wrapped_lines.append(current_line.strip())
                current_line = word
            else:
                current_line += " " + word

        # Add the last line if it exists
        if current_line:
            wrapped_lines.append(current_line.strip())

        return wrapped_lines

    @staticmethod
    def download_file(filepath: str, target_directory: str = "."):
        """
        Simulate terminal download by copying the file to a target directory.
        If no target directory is specified, the current directory is used.
        """
        if os.path.exists(filepath):
            target_path = os.path.join(target_directory, os.path.basename(filepath))
            shutil.copy(filepath, target_path)
            print(f"File has been downloaded to: {os.path.abspath(target_path)}")
        else:
            print("File does not exist.")


class FileHandlerFactory:
    @staticmethod
    def get_file_handler(file_type: str) -> FileHandler:
        if file_type == "text":
            return TextFileHandler()
        elif file_type == "pdf":
            return PDFFileHandler()
        else:
            raise ValueError(f"Unsupported file type: {file_type}")


class TextFormatter:
    """
    A utility class for formatting and designing text.
    """
    @staticmethod
    def bulleted_format(text: str, bullet: str = "\u2022") -> list:
        """
        Convert a string into a bulleted format, separating lines by bullets.
        Returns a list of formatted lines.
        """
        lines = text.splitlines()  # Split the input string into lines
        return [f"{bullet} {line.strip()}" for line in lines if line.strip()]

