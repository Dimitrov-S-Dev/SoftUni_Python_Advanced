def words_sorting(*words):
    word_dict = {}
    total_sum = 0

    for word in words:
        word_sum = sum(ord(ch) for ch in word)
        word_dict[word] = word_sum
        total_sum += word_sum

    if total_sum % 2 == 0:
        s_dict = sorted(word_dict.items(), key=lambda x: x[0])
    else:
        s_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

    result = ""
    for k, v in s_dict:
        result += f"{k} - {v}\n"

    return result

