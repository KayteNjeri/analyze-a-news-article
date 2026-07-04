import re
from collections import Counter
from pathlib import Path


file_path = Path("News Article for Python Assessment.txt")

try:
    text = file_path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
    

# Counting the number of times a specific word is used

def count_specific_word(text, search_word):
    """
    Counts the number of occurences of the specified search word and return the count as integer.
    """
    if not text.strip() or not search_word.strip():
        return 0

    words = re.findall(r"\b\w+\b", text.lower())
    return words.count(search_word.lower())

search_word = input("Enter the word you want to search for: ")

specific_word_count = count_specific_word(text, search_word)

print(f"The word '{search_word}' appears {specific_word_count} times in the News Article.")

# Identifying the most common word

def identify_most_common_word(text):
    """
    Identifies the most common word in the article and returns the most common word as a string.
    """
    if not text.strip():
        return None

    words = re.findall(r"\b\w+\b", text.lower())
    word_counts = Counter(words)

    most_common_word, count = word_counts.most_common(1)[0]
    return most_common_word

# Calculating the average length of words

def calculate_average_word_length(text):
    """
    Calculates the average length of words in the article and returns the average word length as a float.
    """
    words = re.findall(r"\b\w+\b", text)
    if not words:
        return 0

    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    return average_length

# Counting the number of paragraphs

def count_paragraphs(text):
    """
    Counts the number of paragraphs in the article and returns the number of paragraphs as an integer.
    """

    #count = 0
   # for para in doc_reader.paragraphs:
      #  if para.text.strip() == "":
        #    count += 1
   # return count
    if not text.strip():
        return 1

    text = text.strip()

    # Count groups of one or more blank lines
    blank_lines = re.findall("\n\n", text)
    #print(len(blank_lines))
    #for i, match in enumerate(blank_lines, 1):
        #print(f"Blank line group {i}: '{repr(match)}'")

    return len(blank_lines)
    

# Counting the number of sentences in the text.

def count_sentences(text):
    """
    Counts the number of sentences in the article and returns the number of sentences as an integer.
    """
    if not text.strip():
        return 1

    abbreviations = ["Inc.", "Dr."]

    for abbr in abbreviations:
        text = text.replace(abbr, abbr.replace(".", "<DOT>"))
    
    def protect_quotes(match):
        quoted = match.group(0)
        return quoted.replace(".", "<DOT>")

    text = re.sub(r'“[^”]*”|"[^"]*"', protect_quotes, text)
    
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s for s in sentences if s.strip()]

    
    return len(sentences)
    
    

# Call the functions and print the results
specific_word_count = count_specific_word(text, search_word)
most_common_word = identify_most_common_word(text)
average_word_length = calculate_average_word_length(text)
paragraph_count = count_paragraphs(text)
sentence_count = count_sentences(text)

# Display the results
print(f"The count of '{search_word}': {specific_word_count}")

if most_common_word is None:
    print("Most common word: None")
else:
    print(f"Most common word in the article is: '{most_common_word}'")

print(f"Average word length in the article is: {average_word_length:.2f}")
print(f"Number of paragraphs in the article: {paragraph_count}")
print(f"Number of sentences in the article: {sentence_count}")