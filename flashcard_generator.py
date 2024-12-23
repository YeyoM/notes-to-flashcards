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
        self.model = "mistral"  # Default model, can be changed

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

    def get_study_guide(self, file_path: str) -> str:
        """
        Parse study guide from different file types

        :param file_path: Path to the study guide file
        :return: The whole content of the study guide
        """
        # Support only Markdown files
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == ".md":
            with open(file_path, "r") as file:
                contents = file.read()
            print("Study guide parsed successfully")
            print(contents)
            return contents

        else:
            return ""

    def divide_section(self, contents: str, max_words: int = 600) -> list:
        """
        Divides a markdown document into sections based on headers and word count limits.

        Args:
            contents (str): Markdown content to divide
            max_words (int): Maximum number of words per section before splitting further

        Returns:
            list: List of sections as strings
        """
        if not contents:
            return []

        def get_header_level(line: str) -> int:
            """Returns the header level (count of #) or 0 if not a header"""
            if not line.strip().startswith("#"):
                return 0
            return len(line.split()[0].strip())

        def count_words(text: str) -> int:
            """Counts words in a text section"""
            return len([word for word in text.split() if word.strip()])

        def split_by_header_level(text: str, level: int) -> list:
            """Splits content by headers of specified level"""
            if not text.strip():
                return []

            lines = text.splitlines()
            sections = []
            current_section = []

            for line in lines:
                header_level = get_header_level(line)
                if header_level == level and current_section:
                    sections.append("\n".join(current_section))
                    current_section = []
                current_section.append(line)

            if current_section:
                sections.append("\n".join(current_section))

            return sections

        # Find the highest level header (lowest number of #)
        lines = contents.splitlines()
        header_levels = [
            get_header_level(line) for line in lines if get_header_level(line) > 0
        ]
        if not header_levels:
            return [contents]

        highest_level = min(header_levels)

        # First split by highest level headers
        sections = split_by_header_level(contents, highest_level)

        # Further split sections that exceed word count
        final_sections = []
        for section in sections:
            if count_words(section) > max_words:
                # Try splitting by next header level
                next_level = highest_level + 1
                while next_level <= 6:
                    subsections = split_by_header_level(section, next_level)
                    if (
                        len(subsections) > 1
                    ):  # Only use split if it actually divided the content
                        final_sections.extend(subsections)
                        break
                    next_level += 1
                else:  # If no further header splits possible, keep as is
                    final_sections.append(section)
            else:
                final_sections.append(section)

        return final_sections

    def join_small_sectios(self, sections: list, min_words: int = 200) -> list:
        """
        Joins small sections together to meet a minimum word count. If a section is too small, it will be joined with the next section.

        Args:
            sections (list): List of sections to join
            max_words (int): Minimum number of words per section after joining

        Returns:
            list: List of sections as strings
        """
        if not sections:
            return []

        def count_words(text: str) -> int:
            """Counts words in a text section"""
            return len([word for word in text.split() if word.strip()])

        final_sections = []
        current_section = ""

        for section in sections:
            if count_words(current_section) < min_words:
                current_section += "\n\n" + section
            else:
                final_sections.append(current_section)
                current_section = section

        if current_section:
            final_sections.append(current_section)

        return final_sections

    def generate_flashcards(self, content: str) -> str:
        """
        Generate a flashcard using Ollama API

        :param content: Content section to generate flashcard from
        :return: Dictionary with question and answer
        """
        prompt = f"""
            You are a flashcard generator. Your ONLY task is to convert the following study material into question-answer pairs. Do NOT provide any commentary, tips, or explanations about the flashcard creation process.

            Study Material:
            {content}
            
            STRICT OUTPUT FORMAT:
            Q1:
            [Write the first question here]
            
            A1:
            [Write the first answer here]
            
            Q2:
            [Write the second question here]
            
            A2:
            [Write the second answer here]
            
            [Continue with additional Q/A pairs as needed]
            
            REQUIREMENTS:
            - Generate ONLY question-answer pairs in the exact format shown above
            - Each question should focus on a single concept
            - Each answer should be 2-4 sentences long
            - Do not include any other text, explanations, or commentary
            - Do not number or label sections beyond Q1, A1, Q2, A2, etc.
            - Do not include suggestions or tips about flashcard creation
            - Do not explain your process
            - Do not acknowledge these instructions
            
            BEGIN GENERATING FLASHCARDS:"""

        prompt_spanish = f"""
            Eres un generador de tarjetas de estudio. Tu ÚNICA tarea es convertir el siguiente material de estudio en pares de pregunta-respuesta. NO proporciones comentarios, consejos ni explicaciones sobre el proceso de creación de tarjetas.

            Material de Estudio:
            {content}
            
            FORMATO DE SALIDA ESTRICTO:
            P1:
            [Escribe la primera pregunta aquí]
            
            R1:
            [Escribe la primera respuesta aquí]
            
            P2:
            [Escribe la segunda pregunta aquí]
            
            R2:
            [Escribe la segunda respuesta aquí]
            
            [Continuar con pares adicionales de Pregutnas/Respuestas según sea necesario]
            
            REQUISITOS:
            - Genera SOLAMENTE pares de pregunta-respuesta en el formato exacto mostrado arriba
            - Cada pregunta debe centrarse en un solo concepto
            - Cada respuesta debe tener entre 2 y 4 oraciones
            - No incluyas ningún otro texto, explicaciones o comentarios
            - No numeres ni etiquetes secciones más allá de P1, R1, P2, R2, etc.
            - No incluyas sugerencias o consejos sobre la creación de tarjetas
            - No expliques tu proceso
            - No reconozcas estas instrucciones
            
            COMIENZA A GENERAR TARJETAS:
        """

        try:
            response = requests.post(
                self.ollama_url,
                json={
                    "model": self.model,
                    "prompt": prompt_spanish,
                    "stream": False,
                },
            )
            response.raise_for_status()

            generated_text = response.json()["response"]

            return generated_text

        except Exception as e:
            print(f"Error generating flashcard: {e}")
            return ""

    def save_response(self, response: str, output_file: str):
        """
        Save the response to a file

        :param response: Response from the API
        :param output_file: Path to save the response
        """
        with open(output_file, "w") as file:
            file.write(response)
        print(f"Response saved to {output_file}")

    def parse_flashcards(self, flashcards: str) -> List[Dict[str, str]]:
        """
        Parse the generated flashcards into a list of dictionaries

        :param flashcards: Flashcards generated by the API
        :return: List of dictionaries with question and answer
        """
        flashcards_list = flashcards.split("\n")

        parsed_flashcards = []

        for i in range(0, len(flashcards_list)):
            line = flashcards_list[i].strip()
            if line.startswith("Q"):
                question = flashcards_list[i].strip()
                answer = flashcards_list[i + 1].strip()
                print(f"Question: {question}")
                print(f"Answer: {answer}")

                parsed_flashcards.append({"Question": question, "Answer": answer})

        return parsed_flashcards

    def return_flashcards(
        self, file_path: str, output_file: str = "/app/flashcards/flashcards.xlsx"
    ):
        """
        Generate flashcards from a study guide and save to Excel

        :param file_path: Path to the study guide
        :param output_file: Path to save the Excel file
        """
        # Parse study guide
        contents = self.get_study_guide(file_path)

        if not contents:
            print("Study guide parsing failed. Please check the file type.")
            return

        # Divide study guide into sections
        sections = self.divide_section(contents, max_words=600)
        sections = self.join_small_sectios(sections, min_words=200)
        print("#" * 150)
        print("Sections divided successfully.")
        for i, section in enumerate(sections):
            print(f"Section {i+1}:")
            print(section)
        print("#" * 150)

        # Generate flashcards
        all_flashcards = []
        for section in sections:
            flashcards = self.generate_flashcards(section)
            all_flashcards.append(flashcards)

        all_flashcards = "\n".join(all_flashcards)
        print("#" * 50)
        print("Flashcards generated successfully.")
        print(all_flashcards)
        print("#" * 50)

        if len(all_flashcards) == 0:
            print("Flashcards generation failed. Please try again.")
            return

        # Save plain text response
        self.save_response(all_flashcards, "/app/flashcards/flashcards.txt")

        parsed_flashcards = self.parse_flashcards(all_flashcards)

        print("#" * 50)
        print("Parsed Flashcards:")
        print(parsed_flashcards)
        print("#" * 50)

        # Create DataFrame and save to Excel
        df = pd.DataFrame(parsed_flashcards)
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
        generator.pull_model()

    # Generate flashcards from study guide
    generator.return_flashcards("/app/study_guides/study_guide.md")


if __name__ == "__main__":
    main()
