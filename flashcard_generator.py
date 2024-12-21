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

    def parse_study_guide(self, file_path: str) -> str:
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
            Q1:
            [Escribe la primera pregunta aquí]
            
            A1:
            [Escribe la primera respuesta aquí]
            
            Q2:
            [Escribe la segunda pregunta aquí]
            
            A2:
            [Escribe la segunda respuesta aquí]
            
            [Continuar con pares adicionales de Q/A según sea necesario]
            
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
        contents = self.parse_study_guide(file_path)

        if not contents:
            print("Study guide parsing failed. Please check the file type.")
            return

        # Generate flashcards
        flashcards = self.generate_flashcards(contents)
        print("#" * 50)
        print("Flashcards generated successfully.")
        print(flashcards)
        print("#" * 50)

        if not flashcards:
            print("Flashcards generation failed. Please try again.")
            return

        # Save plain text response
        self.save_response(flashcards, "/app/flashcards/flashcards.txt")

        parsed_flashcards = self.parse_flashcards(flashcards)

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
