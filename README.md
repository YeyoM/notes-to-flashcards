# Flashcard Generator

Flashcard Generator is a Python-based tool designed to create question-answer flashcards from study material. This project leverages the Ollama API to transform structured content, such as Markdown files, into comprehensive flashcards, making learning more efficient.

---

## Features

- **Ollama API Integration**: Connects to the Ollama API to generate flashcards from your content.
- **Model Management**: Automatically pulls and verifies models for processing.
- **Markdown Parsing**: Reads, cleans, and processes study guides in Markdown format.
- **Section Division**: Splits study material into manageable sections for better flashcard generation.
- **Customizable Outputs**: Generates flashcards in English or Spanish, adhering to strict formatting rules.

---

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/YeyoM/notes-to-flashcards.git
   cd notes-to-flashcards
   ```

2. Place your study material in the `study_guides` directory with the name `study_guide.md`:

   ```plaintext
   notes-to-flashcards
   ├── study_guides
   │   └── study_guide.md
   ```

   Note 1: The study guide should be in Markdown format.
   Note 2: For better results, use headings to divide the content into sections. (e.g., `# Chapter 1: Basics`)

3. Run docker-compose:

   Using docker compose, you can run the following command:

   ```bash
   docker-compose up # or docker-compose up --build to rebuild the images
   ```

---

## Configuration

- **Model**: By default, the generator uses the `mistral` model. You can modify this in the `FlashcardGenerator` class.
- **Content Parsing**: Only Markdown files are currently supported. Other formats will return an empty string.

---

## Example Output

### Input

```markdown
# Chapter 1: Basics

- Python is a programming language.
- It is used for web development, data analysis, and more.
```

### Output

```plaintext
Q1:
What is Python?

A1:
Python is a programming language used for web development, data analysis, and other applications.
```

Note: You will see that before running the script, there are already some flashcards generated in the `flashcards` directory, these are some examples of the output and will be overwritten when you run the script.

---

## Contributions

Contributions are welcome! Feel free to fork the repository and submit pull requests with enhancements or bug fixes.

---

## License

This project is licensed under the [MIT License](LICENSE).
