from typing import List

WORDS = set()

with open("polish_words.txt") as f:
    for line in f:
        WORDS.add(line.strip())


def find_sentences(sentence: str, valid_seq: set) -> List[str]:
    sentences = []
    for i in range(1, len(sentence)):
        if sentence[:i] in WORDS:
            next_seq = []
            if sentence[i:] not in valid_seq:
                if len(sentence[i:]) != 0:
                    next_seq = find_sentences(sentence[i:], valid_seq)
                    valid_seq[sentence[i:]] = next_seq
            else:
                next_seq = valid_seq[sentence[i:]]
            
            seq = [sentence[:i]] + next_seq
            sentences.append(seq)
        else:
            continue
    
    max_sum_of_squares = 0
    max_seq = []
    for seq in sentences:
        sum = 0
        for text in seq:
            sum += len(text) * len(text)
        if sum > max_sum_of_squares:
            max_sum_of_squares = sum
            max_seq = seq
    
    return max_seq


def valid_sentence(sentence: str) -> str:
    valid_seq = {} # dictionary
    valid = find_sentences(sentence, valid_seq)
    seq = ''
    for i in valid:
        seq += i + ' '
    return seq


sentences = []

with open("zad2_input.txt") as f:
    for line in f:
        sentences.append(line.strip())

f = open('zad2_output.txt', 'a')

for sentence in sentences:
    f.write(valid_sentence(sentence) + '\n')

f.close()