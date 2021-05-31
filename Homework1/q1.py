"""
Phang Teng Fone 1003296 A.I Coding Hw1 Question 1
This is a graph problem, unweighted. So use Preprocessing + BFS.

The time complexity of this code is:
O(mn^2) where n is total number of words, m is max length of the word
"""
from collections import deque

WORDS = set(i.lower().strip() for i in open('words2.txt'))
start_word = 'cold'
end_word = 'warm'


def preprocess(WORDS) -> dict:
    """
    [hot,dot,dog,hat...]
    *ot: [hot,dot]
    h*t: [hot,hat]
    """
    output_dict = {}
    for word in WORDS:
        for c in range(len(word)):
            wildcard = word[:c] + "*" + word[c+1:]
            if wildcard not in output_dict:
                output_dict[wildcard] = []
            output_dict[wildcard].append(word)
    return output_dict


def word_ladder(start_word, end_word) -> int:
    """
    Returns the shortest transformation required.
    cold => warm
    - cold
    - cord
    - card
    - ward
    - warm
    Total Count: 5
    """
    # Preprocess
    processedWords = preprocess(WORDS)
    # BFS (Queue)
    queue = deque()
    queue.append([start_word, 1])
    visited = set()

    while queue:
        current, counter = queue.popleft()
        for c in range(len(current)):
            # Convert to current wildcard: eg. cold = *old
            wildcard = current[:c] + "*" + current[c+1:]
            if wildcard in processedWords:
                # retrieving all *old = [hold,told...]
                for word in processedWords[wildcard]:
                    if word == end_word:
                        return counter + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append([word, counter+1])
    return 0


def is_valid_word(word):
    return word in WORDS


def main():
    if (len(start_word) != len(start_word)) or not start_word or not end_word:
        print("Error, Check Input Word(s)")
    elif not is_valid_word(end_word):
        print(
            f"Start Word: {start_word}, End Word: {end_word}\nERROR: Output word does not exist in WordList")
    else:
        print(
            f"Start Word: {start_word}, End Word: {end_word}\nShortest Transformation: {word_ladder(start_word,end_word)}")


if __name__ == '__main__':
    main()
