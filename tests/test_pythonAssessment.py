import sys
import pytest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from pythonAssessment import (
    count_specific_word,
    identify_most_common_word,
    calculate_average_word_length,
    count_paragraphs,
    count_sentences,
)

# Load the article to be used for analysis
file_path = Path("News Article for Python Assessment.txt")
text = file_path.read_text(encoding="utf-8")


# 1. count_specific_word()

def test_count_specific_word():
    assert count_specific_word(text, "ACME") == 10


# 2identify_most_common_word()

def test_identify_most_common_word():
    assert identify_most_common_word(text) == "the"


# 3. calculate_average_word_length()

def test_average_word_length():
    average = calculate_average_word_length(text)
    assert isinstance(average, float)

    assert average > 0
    assert average < 10  # Assuming the average word length is less than 10 characters
    assert calculate_average_word_length(text) == pytest.approx(5.22, abs=0.01)  # Adjust the expected value based on the actual average word length

def test_average_word_length_empty():
    assert calculate_average_word_length("") == 0



# 4. count_paragraphs()

def test_count_paragraphs():
    assert count_paragraphs(text) == 19

# 5. count_sentences()

def test_count_sentences():
    assert count_sentences(text) == 32


# Edge cases tests
def test_empty_specific_word():
    assert count_specific_word("", "ACME") == 0


def test_empty_common_word():
    assert identify_most_common_word("") is None


def test_empty_average():
    assert calculate_average_word_length("") == 0


def test_empty_paragraphs():
    assert count_paragraphs("") == 1


def test_empty_sentences():
    assert count_sentences("") == 1