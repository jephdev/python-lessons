# Steps
# 1. Split the text into words
# 2. Clean each word
# 3. Check whether the word is interesting or not
# 4. Populate the dictionary

def cleaned_text(text):
    cleaned_text = ""
    for character in text:
        if str(character).isalpha():
            cleaned_text += character
        else:
            cleaned_text += " "
    return cleaned_text


def word_dictionary(words, uninteresting_words):
    result = {}
    for word in words:
        if word not in uninteresting_words:
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
    return result


uninteresting_words = set(
    ["a", "an", "be", "if", "to", "of", "in", "on", "at", "i", "the", "is", "you", "for", "as"])


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    result = {}
    words = file_contents.split()
    for word in words:
        cleaned_word = ""
        for character in word:
            if character not in punctuations:
                cleaned_word += character
        cleaned_word_lower = cleaned_word.lower()
        if cleaned_word_lower.isalpha() and cleaned_word_lower not in uninteresting_words:
            if cleaned_word_lower in result:
                result[cleaned_word_lower] += 1
            else:
                result[cleaned_word_lower] = 1
    return result


# with open('sample3.txt') as file:
#     words = []
#     for line in file:
#         line = cleaned_text(line.lower())
#         words.extend(line.split())
#     word_dictionary = word_dictionary(words, uninteresting_words)
#     print(word_dictionary)

with open('sample3.txt') as file:
    file_contents = file.read()
    print(calculate_frequencies(file_contents))
