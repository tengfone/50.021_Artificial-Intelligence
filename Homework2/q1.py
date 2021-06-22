"""
Phang Teng Fone 1003296 A.I Coding Hw1 Question 1
This is a graph problem, unweighted. So use Preprocessing + BFS.
The time complexity of this code is:
O(mn^2) where n is total number of words, m is max length of the word
Edited Version of Attempt 1
"""
from collections import deque
import copy
from typing import Tuple

WORDS = set(i.lower().strip() for i in open('./words2.txt'))
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


def word_ladder(start_word, end_word) -> Tuple[list, int]:
    """
    Returns a list of words traversed to the goal state minimally and 
    the min number of transformation required.
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
    queue.append(([start_word], 1))
    visited = set()

    while queue:
        current, counter = queue.popleft()
        currentWord = current[len(current)-1]
        if currentWord == end_word:
            return current, counter
        if currentWord not in visited:
            visited.add(currentWord)
            for i in range(len(currentWord)):
                wildcards = currentWord[:i] + "*" + currentWord[i+1:]
                for wildcard in processedWords[wildcards]:
                    tmpList = copy.deepcopy(current)
                    tmpList.append(wildcard)
                    queue.append([tmpList, counter + 1])

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
        output = word_ladder(start_word, end_word)
        if output == 0:
            print("Error, Words cannot be formed")
        else:
            levelDepth = output[1]
            outputString = ' -> '.join([str(elem) for elem in output[0]])
            print(
                f"Start Word: {start_word}, End Word: {end_word}\nShortest Transformation: {levelDepth}\nWord Traversed: {outputString}")


if __name__ == '__main__':
    main()


# def main():
#     pass


# if __name__ == '__main__':
#     main()


################################################################
################### ATTEMPT 1 (WRONG ANSWER) ###################
## Reason: Never keep track of visited Nodes, unable to print ##
########################## visited nodes #######################


# from collections import deque

# WORDS = set(i.lower().strip() for i in open('./words2.txt'))
# start_word = 'test'
# end_word = 'warm'


# def preprocess(WORDS) -> dict:
#     """
#     [hot,dot,dog,hat...]
#     *ot: [hot,dot]
#     h*t: [hot,hat]
#     """
#     output_dict = {}
#     for word in WORDS:
#         for c in range(len(word)):
#             wildcard = word[:c] + "*" + word[c+1:]
#             if wildcard not in output_dict:
#                 output_dict[wildcard] = []
#             output_dict[wildcard].append(word)
#     return output_dict


# def word_ladder(start_word, end_word) -> int:
#     """
#     Returns the shortest transformation required.
#     cold => warm
#     - cold
#     - cord
#     - card
#     - ward
#     - warm
#     Total Count: 5
#     """
#     # Preprocess
#     processedWords = preprocess(WORDS)
#     # BFS (Queue)
#     queue = deque()
#     queue.append([start_word, 1])
#     visited = set()
#     totalWord = ''

#     while queue:
#         current, counter = queue.popleft()
#         for c in range(len(current)):
#             print(current)
#             # Convert to current wildcard: eg. cold = *old
#             wildcard = current[:c] + "*" + current[c+1:]
#             if wildcard in processedWords:
#                 # retrieving all *old = [hold,told...]
#                 for word in processedWords[wildcard]:
#                     if word == end_word:
#                         return (counter + 1, totalWord)
#                     if word not in visited:
#                         visited.add(word)
#                         queue.append([word, counter+1])
#     return 0


# def is_valid_word(word):
#     return word in WORDS


# def main():
#     if (len(start_word) != len(start_word)) or not start_word or not end_word:
#         print("Error, Check Input Word(s)")
#     elif not is_valid_word(end_word):
#         print(
#             f"Start Word: {start_word}, End Word: {end_word}\nERROR: Output word does not exist in WordList")
#     else:
#         totalIteration, totalWords = word_ladder(start_word, end_word)
#         print(
#             f"Start Word: {start_word}, End Word: {end_word}\nShortest Transformation: {totalIteration}\nWord Traversed: {totalWords}")


# if __name__ == '__main__':
#     main()

################################################################
################### ATTEMPT 2 (WRONG ANSWER) ###################
### Reason: does not cover all cases, not visiting all nodes ###
################################################################


# WORDS = set(i.lower().strip() for i in open('./words2.txt'))
# start_word = 'test'
# end_word = 'warm'


# def is_valid_word(word):
#     return word in WORDS


# def word_ladder(start_word, end_word):
#     def backtrack(word, counter, parent, output):
#         """
#         Recursion replace each character (exclude current word) of start word
#         till finds goal state.
#         Explored set in output.
#         """
#         if word == end_word:
#             output.append([word, counter])
#             return output

#         for i, letter in enumerate(end_word):
#             checkAlpha = list(word)
#             if letter != checkAlpha[i]:
#                 newWord = word[:i] + letter + word[i+1:]
#                 if is_valid_word(newWord):
#                     output.append([word, counter])
#                     return backtrack(newWord, counter + 1, word, output)

#     result = backtrack(start_word, 1, '', [])
#     if result:
#         counter = 0
#         outString = ''
#         for i in range(len(result)):
#             outString += ''.join(result[i][0]) + ' -> '
#             counter = result[i][1]
#         return outString,counter
#     else:
#         raise Exception ("ERROR: Cannot be found")


# def main():
#     if (len(start_word) != len(start_word)) or not start_word or not end_word:
#         print("Error, Check Input Word(s)")
#     elif not is_valid_word(end_word):
#         print(
#             f"Start Word: {start_word}, End Word: {end_word}\nERROR: Output word does not exist in WordList")
#     else:
#         totalWords, totalIteration = word_ladder(start_word, end_word)
#         print(
#             f"Start Word: {start_word}, End Word: {end_word}\nShortest Transformation: {totalIteration}\nWord Traversed: {totalWords}")


# if __name__ == '__main__':
#     main()
