# Analyze The Contents of a News Article

## 🚀Project Overview

This project is a Python application that analyzes a news article stored in a text file. It demonstrates the use of Python functions, regular expressions, loops, conditionals, and file handling to extract valuable insights from the text. The analysis in this project has been performed on the following text file [News Article for Python Assessment.txt](News%20Article%20for%20Python%20Assessment.txt)

The program prompts the user to enter a word to search for, then performs several text analysis tasks on the article.

---

## 🏠Features

The application performs the following analyses:

1. Counts the number of occurrences of a user-specified word.
2. Identifies the most common word in the article.
3. Calculates the average word length.
4. Counts the number of paragraphs based on blank lines between blocks of text.
5. Counts the number of sentences while correctly handling abbreviations and quoted text.

---

## 🛠️Technologies Used

- Python 3
- Regular Expressions (`re`)
- Collections (`Counter`)
- pathlib
- pytest (for unit testing)

---

## 📁Project Structure

```
analyze-a-news-article/
│
├── pythonAssessment.py
├── News Article for Python Assessment.txt
├── tests/
│   └── test_pythonAssessment.py
├── README.md
└── .gitignore
```

---

## ⚙️Installation

1. Clone the repository:

```bash
git clone https://github.com/KayteNjeri/analyze-a-news-article
```

2. Navigate to the project directory:

```bash
cd analyze-a-news-article
```

3. Ensure Python 3 is installed.

---

## 📦Running the Program

Run the application using:

```bash
python3 pythonAssessment.py
```

When prompted, enter a word to search for in the article.

Example:

```
Enter the word you want to search for: ACME
```

Example output:

```
The word 'ACME' appears 10 times in the News Article.
```

---

## 🧪Running the Tests

Install pytest if necessary:

```bash
pip install pytest
```

Run the test suite:

```bash
pytest
```

---

## ⚛️Functions

### `count_specific_word(text, search_word)`

Counts how many times a specified word appears in the text.

**Parameters**

- `text` (str)
- `search_word` (str)

**Returns**

- `int`

---

### `identify_most_common_word(text)`

Determines the most frequently occurring word in the article.

**Parameters**

- `text` (str)

**Returns**

- `str`

---

### `calculate_average_word_length(text)`

Calculates the average length of all words in the article.

**Parameters**

- `text` (str)

**Returns**

- `float`

---

### `count_paragraphs(text)`

Counts the number of paragraphs in the article.

Paragraphs are defined using blank lines between blocks of text.

**Parameters**

- `text` (str)

**Returns**

- `int`

---

### `count_sentences(text)`

Counts the number of sentences in the article.

The function recognizes sentence-ending punctuation while preventing abbreviations (such as `Inc.` and `Dr.`) and quoted text from being counted incorrectly.

**Parameters**

- `text` (str)

**Returns**

- `int`

---

## 🛠️Edge Cases

The application handles the following edge cases:

- Empty text returns one paragraph.
- Empty text returns one sentence.
- Empty search words return a count of zero.
- Empty articles return `None` when identifying the most common word.
- Articles with no words return an average word length of zero.
- Common abbreviations are ignored when counting sentences.

---

## 🔄Sample Results

Using the supplied news article:

| Analysis | Result |
|----------|--------|
| Search word **ACME** | 10 occurrences |
| Most common word | the |
| Average word length | 5.22 |
| Paragraphs | 19 |
| Sentences | 32 |

---

## 🎯Learning Outcomes Demonstrated

This project demonstrates:

- Functions
- File handling
- Regular expressions
- String manipulation
- Lists
- Loops (`for` and `while`)
- Conditional statements (`if/else`)
- Exception handling
- Unit testing with pytest

---

## 🔮Future Improvements

Possible enhancements include:

- Ignore common stop words when identifying the most common word.
- Support additional document formats such as DOCX and PDF.
- Visualize word frequencies using charts.

---

## 👩🏽‍💻 Author

This project has been built as part of a Python assessment project to demonstrate backend development concepts and practices.

---

## 📄 License

This project is licensed under the MIT License.