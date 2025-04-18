from abc import ABC, abstractmethod
import PyPDF2

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
        from textwrap import fill  # Import for paragraph formatting
        with open(filepath, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            full_text = ""
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                formatted_text = fill(text if text else "[No extractable text]", width=80)
                full_text += f"\n\n--- Page {i + 1} ---\n\n{formatted_text}"
            return full_text

    def write_file(self, filepath: str, content: str):
        raise NotImplementedError("Writing to PDF files is not supported.")


class FileHandlerFactory:
    @staticmethod
    def get_file_handler(file_type: str) -> FileHandler:
        if file_type == "text":
            return TextFileHandler()
        elif file_type == "pdf":
            return PDFFileHandler()
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
