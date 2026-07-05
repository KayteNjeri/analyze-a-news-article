import re
from collections import Counter
from pathlib import Path

file_path = Path("News Article for Python Assessment.txt")

try:
    text = file_path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
    

# 1. Counting the number of times a specific word is used

def count_specific_word(text, search_word):
    """
    Counts the number of occurences of the specified search word and return the count as integer.
    """

    # Edge Case
    if not text.strip() or not search_word.strip():
        return 0

    # Convert the text to lowercase and use regex to find whole words only
    words = re.findall(r"\b\w+\b", text.lower())
    return words.count(search_word.lower())

# Input from the user for the word to search
search_word = input("Enter the word you want to search for: ")

while not search_word: #if the user enters an empty string, prompt them again
    search_word = input("Please enter the word you want to search for: ")

specific_word_count = count_specific_word(text, search_word)

# Display the result
print(f"The word '{search_word}' appears {specific_word_count} times in the News Article.")

# 2. Identifying the most common word

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

# 3. Calculating the average length of words

def calculate_average_word_length(text):
    """
    Calculates the average length of words in the article and returns the average word length as a float.
    """
    # Extract words only; ignore special characters
    words = re.findall(r"\b\w+\b", text)

    #Edge Case
    if not words:
        return 0

    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    return average_length

# 4. Counting the number of paragraphs

def count_paragraphs(text):
    """
    Counts the number of paragraphs in the article and returns the number of paragraphs as an integer.
    """

    # Edge Case
    if not text.strip():
        return 1

    # Count blank lines in the text
    blank_lines = len(re.findall("\n\n", text))
    
    return blank_lines + 1 #the document has n blank lines, hence the number of paragraphs is n+1
    

# 5. Counting the number of sentences in the text.

def count_sentences(text):
    """
    Counts the number of sentences in the article and returns the number of sentences as an integer.
    """

    # Edge case
    if not text.strip():
        return 1

    # Prevent abbreviations from being treated as sentence endings
    abbreviations = ["Inc.", "Dr."]

    for abbr in abbreviations:
        text = text.replace(abbr, abbr.replace(".", "<DOT>"))
    
    # Replace periods inside quoted text
    def protect_quotes(match):
        quoted = match.group(0)
        return quoted.replace(".", "<DOT>")

    text = re.sub(r'“[^”]*”|"[^"]*"', protect_quotes, text)
    
    # Count sentences by splitting punctuation marks.
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