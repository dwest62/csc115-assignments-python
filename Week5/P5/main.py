FILEPATH = r"HmongWords.txt"

def main():
    english_to_mong = load_dictionary(FILEPATH)
    word_count = dict()
    translate_loop(english_to_mong, word_count)

def translate_loop(english_to_mong: dict, word_count: dict):
    sentence = input("\nType your English sentence: ")
    words_to_translate = get_words_to_translate(sentence)
    count_words(word_count, words_to_translate)
    translation = translate(words_to_translate, english_to_mong)
    print("\nHmong:",translation)
    cont = prompt_continue("\nAnother translation (Y/N): ")
    if cont:
        translate_loop(english_to_mong, word_count)
    else:
        print()
        print_word_frequency(word_count)

def count_words(word_count: dict, words_to_count: list):
    for word in words_to_count:
        word_count[word] = word_count.get(word, 0) + 1

def load_dictionary(filename: str) -> dict:
    with open(filename, "r") as f:
        lst = f.read().splitlines()
    lst = [line.split(",") for line in lst]
    d = {}
    for word in lst:
        translation = word[1]
        d[word[2]] = translation
    return d

def translate(sentence: list, lang_to_lang: dict) -> str:
    translation = ""
    for word in sentence:
        d_item = lang_to_lang.get(word, "?") + " "
        translation += d_item
    return translation

def get_words_to_translate(sentence: str) -> list:
    accum = []
    curr_word = ""
    for c in sentence:
        if not c.isalpha():
            if curr_word:
                accum.append(curr_word.lower())
                curr_word = ""
        else: curr_word += c
    if curr_word: accum.append(curr_word.lower())
    return accum

def print_word_frequency(word_count: dict) -> None:
    fmt = lambda s: "{: <12}".format(s)
    title = f"{fmt('Word')}{fmt('Frequency')}"
    bar = "-" * 23
    print(title)
    print(bar)
    for k,v in word_count.items():
        print(f"{fmt(k)}{fmt(v)}")

def prompt_continue(prompt) -> str:
        read = lambda: input(prompt)
        cont = read()
        while cont not in ["Y", "y", "N", "n"]:
            print(f"Invalid input. You entered {cont}.")
            cont = read()
        return cont in ["Y", "y"]

if __name__ == "__main__":
    main()