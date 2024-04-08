def calculate_word_scores(lines):
    word_scores = {}

    for line in lines:
        missing_index = line.index('_')
        possible_words = set()

        for letter in 'abcdefghijklmnopqrstuvwxyz':
            possible_word = line[:missing_index] + \
                letter + line[missing_index+1:]
            possible_words.add(possible_word)

        for word in possible_words:
            if word in word_scores:
                word_scores[word] += 1
            else:
                word_scores[word] = 1

    return word_scores


lines_quantify = int(input())
lines = [input() for _ in range(lines_quantify)]

word_scores = calculate_word_scores(lines)

max_score = max(word_scores.values())
fake_string = max(
    (word for word, score in word_scores.items() if score == max_score), key=len)

print(fake_string, max_score)
