import os
import time
import requests  # pyright: ignore
import pandas as pd  # pyright: ignore
from typing import List, Dict


class FlashcardGenerator:
    def __init__(self, ollama_url: str = "http://ollama:11434/api/generate"):
        """
        Initialize the Flashcard Generator with Ollama API endpoint

        :param ollama_url: URL of the Ollama API for generating flashcards
        """
        self.ollama_url = ollama_url
        self.model = "tinyllama"  # Default model, can be changed

    def test_ollama_connection(self) -> bool:
        """
        Test connection to Ollama and generate a sample flashcard

        :return: Boolean indicating successful connection and flashcard generation
        """
        try:
            # Test connection
            test_response = requests.get(
                f"{self.ollama_url.replace('/generate', '')}/version"
            )
            # print(test_response.text)
            test_response.raise_for_status()

            print("Ollama Connection Test:")
            print("✅ API Version Check: Success")

            return True

        except requests.exceptions.RequestException as e:
            print(f"❌ Ollama Connection Failed: {e}")
            return False

    def pull_model(self):
        """
        Pull a model from the Ollama API
        """
        try:
            print(f"Pulling model: {self.model}")
            response = requests.post(
                f"{self.ollama_url.replace('/generate', '')}/pull",
                json={"model": self.model, "stream": False},
            )
            # print(response.json())
            response.raise_for_status()
            print(f"Model {self.model} pulled successfully")
        except Exception as e:
            print(f"Error pulling model: {e}")

    def check_model(self) -> bool:
        """
        check if the model is already pulled from the Ollama API
        """
        try:
            print(f"Checking model: {self.model}")
            response = requests.get(
                f"{self.ollama_url.replace('/generate', '')}/tags",
            )
            # print(response.json())
            response.raise_for_status()
            for model in response.json().get("models", []):
                if self.model in model["name"]:
                    print(f"Model {self.model} already pulled")
                    return True
            print(f"Model {self.model} not pulled")
            return False
        except Exception as e:
            print(f"Error checking model: {e}")
            return False

    def parse_study_guide(self, file_path: str) -> List[str]:
        """
        Parse study guide from different file types

        :param file_path: Path to the study guide file
        :return: List of content sections
        """
        # Support multiple file types
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == ".txt":
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read().split("\n\n")  # Split by paragraphs

        elif file_extension == ".docx":
            import docx  # pyright: ignore

            doc = docx.Document(file_path)
            return [para.text for para in doc.paragraphs if para.text.strip()]

        elif file_extension == ".pdf":
            import PyPDF2  # pyright: ignore

            with open(file_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                return [page.extract_text() for page in reader.pages]

        else:
            raise ValueError(f"Unsupported file type: {file_extension}")

    def generate_flashcard(self, content: str) -> Dict[str, str]:
        """
        Generate a flashcard using Ollama API

        :param content: Content section to generate flashcard from
        :return: Dictionary with question and answer
        """
        prompt = f"""
        Create a detailed flashcard from the following study material:
        
        Material: {content}
        
        Please provide:
        1. A clear, concise question that tests understanding
        2. A comprehensive answer that covers key points
        3. Ensure the question cannot be answered with a simple yes/no
        
        Format your response as:
        Question: [Your question here]
        Answer: [Detailed answer here]
        """

        try:
            response = requests.post(
                self.ollama_url,
                json={"model": self.model, "prompt": prompt, "stream": False},
            )
            print(response.json())
            response.raise_for_status()

            generated_text = response.json()["response"]

            # Parse the generated text into question and answer
            parts = generated_text.split("Answer:", 1)
            question = parts[0].replace("Question:", "").strip()
            answer = parts[1].strip() if len(parts) > 1 else "No answer generated"

            return {"Question": question, "Answer": answer}

        except Exception as e:
            print(f"Error generating flashcard: {e}")
            return {
                "Question": f"Error processing: {content[:50]}...",
                "Answer": str(e),
            }

    def generate_flashcards(self, file_path: str, output_file: str = "flashcards.xlsx"):
        """
        Generate flashcards from a study guide and save to Excel

        :param file_path: Path to the study guide
        :param output_file: Path to save the Excel file
        """
        # Parse study guide
        sections = self.parse_study_guide(file_path)

        # Generate flashcards
        flashcards = []
        for section in sections:
            if len(section.strip()) > 50:  # Ignore very short sections
                flashcard = self.generate_flashcard(section)
                flashcards.append(flashcard)

        # Create DataFrame and save to Excel
        df = pd.DataFrame(flashcards)
        df.to_excel(output_file, index=False)
        print(f"Flashcards generated and saved to {output_file}")


def main():
    # wait 30 seconds for ollama to start
    time.sleep(10)

    # Create generator instance
    generator = FlashcardGenerator()

    # Test Ollama connection first
    if not generator.test_ollama_connection():
        print("Cannot proceed. Ollama connection test failed.")

    # Check if the model is already pulled
    if not generator.check_model():
        # Pull the model
        generator.pull_model()


if __name__ == "__main__":
    main()
