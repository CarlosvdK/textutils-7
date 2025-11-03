# textutils-7

Small Python package for text utilities — group assignment. These are the steps we have followed in order to succesfully implement our features.

## Team

Team 7 — Python for Data Science (Term 1)

- Sara Fibla 
- Ella Magdic 
- Georgii Runko
- Alexander Schumacher
- Carlos Van der Kooij

Delivery Date: November 6, 2025

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/CarlosvdK/textutils-7.git
    cd textutils-7
    ```

2. Create the environment (with micromamba):

    ```bash
    micromamba create -f environment.yml -y
    micromamba activate textutils
    ```

3. Install the package in editable mode:

    ```bash
    pip install -e .
    ```

## Running Tests

To run all tests and check coverage:

```bash

pytest
```

To see detailed coverage information:

```bash
pytest --cov=src/textutils --cov-report=term-missing

```
## Features

- word_count(text) — case-insensitive counts.
- top_n(counts, n) — top-N by frequency, ties alphabetical.
- normalize_whitespace(text) — collapse runs of whitespace, trim ends.
- remove_punctuation(text) — strip punctuation while keeping spaces and letters.
- is_palindrome(text) — check if text reads the same backwards (ignore case and spaces).
- unique_words(text) — return a sorted list of distinct words (case-insensitive).
- reverse_words(text) — reverse the order of words, not characters.
- capitalize_sentences(text) — ensure each sentence starts with a capital letter.
- word_lengths(text) — return a dict mapping words to their lengths.
- strip_accents(text) — remove accents from characters (e.g., café → cafe).
- slugify(text) — convert text to lowercase, hyphen-separated safe string.
- count_vowels(text) — count vowels in the given text.
- camel_to_snake(text) — convert CamelCase identifiers to snake_case.
- truncate(text, n) — shorten text to n characters, adding “...” if needed.
- collapse_duplicates(text, char) — replace runs of the same char with one.
- is_anagram(a, b) — check if two texts are anagrams (ignore case and spaces).
- compare_texts(text1, text2) — compute similarity based on common word ratio.
- replace_numbers(text) — replace digits with their word equivalents (2 → two).
- sentence_count(text) — count number of sentences in text.
- average_word_length(text) — compute mean length of words in text.


## Project Description

This package was developed as a group assignment for Python for Data Science. We initially handled different features separately, resolving merge conflicts individually with each commit to the master branch (demonstrating individual knowledge). Afterward, we transitioned to working collaboratively on the compare_texts, contributing to both its testing and core functionality. Finally, we implemented the remaining features and the documentation update.

## Development Workflow

Each team member worked in their own branch to implement an assigned feature, committing frequently and merging changes into the main branch through pull requests.
Merge conflicts were intentionally resolved by individuals during integration to demonstrate understanding of Git workflows. Once the base functionalities were stable, we collaborated on a shared feature (average_word_length) and collectively refined both the implementation and its associated tests.

## Testing & Coverage

Unit tests were written for every function within src/textutils/core.py to ensure correctness and robustness.
Integration tests validated how multiple functions interacted together.
We used pytest for testing and pytest-cov to measure coverage, aiming for 100% line coverage across the package.

The command:
```bash
pytest --cov=src/textutils --cov-report=term-missing
```
was used regularly to monitor coverage and maintain testing standards.

## Collaboration Reflection
This project emphasized effective teamwork through Git-based collaboration. Each member contributed independently, reviewed peers’ code, and participated in resolving issues collaboratively. Working together on a shared feature helped us align on coding conventions, testing practices, and documentation style. The experience strengthened our understanding of version control, modular code design, and test-driven development (TDD) in a group context.

## Project Structure
The final repository follows the expected structure:

```text
textutils-7/
├─ src/textutils/__init__.py
├─ src/textutils/core.py
├─ tests/unit/test_core.py
├─ tests/integration/test_end_to_end.py
├─ environment.yml
├─ pyproject.toml
├─ README.md
```

**Explanation of the structure:**

* **`src/textutils/`** – this folder contains the actual **Python package code**.
  Inside it:

  * `__init__.py` marks the directory as a package, allowing imports like `import textutils`.
  * `core.py` is where you will implement the main functionality of the project.

* **`tests/`** – this folder contains all the **automated tests** for your code.
  It is divided into:

  * `tests/unit/` → short, focused tests for individual functions (TDD work happens here).
  * `tests/integration/` → tests that check how different parts of the code work together.

* **`environment.yml`** – defines the **micromamba environment** (Python version, dependencies, etc.) so everyone on the team can reproduce the same setup easily.

* **`pyproject.toml`** – contains **project configuration**, including pytest and coverage settings.

* **`README.md`** – the **documentation** of your project: describe what the package does, how to install dependencies, and how to run the tests.

