import collections


def find_longest_word_in_string(letters, words):
    letter_positions = collections.defaultdict(list)
    for index, letter in enumerate(letters):
        letter_positions[letter].append(index)
    for word in sorted(words, key=lambda w: len(w), reverse=True):
        pos = 0
        for letter in word:
            if letter not in letter_positions:
                break
            possible_positions = []
            for p in letter_positions[letter]:
                if p >= pos:
                    possible_positions.append(p)
                    pos = possible_positions[0] + 1
            if not possible_positions:
                break
            else:
                return word

S = "abppplee"
D = {"able", "ale", "apppple", "bale", "kangaroo"}

if __name__ == '__main__':
    print(find_longest_word_in_string(S, D))