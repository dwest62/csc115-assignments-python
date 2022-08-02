FILEPATH = r"HmongWords.txt"

def main():
    english_to_hmong = load_dictionary(FILEPATH)
    word_count = dict()
    translate_loop(english_to_hmong, word_count)

def load_dictionary(filename: str) -> dict:
    with open(filename, "r") as f:
        lst = f.read().splitlines()
    lst = [line.split(",") for line in lst]
    d = {}
    for word in lst:
        translation = word[1]
        d[word[2]] = translation
    return d

def translate_loop(english_to_hmong: dict, word_count: dict):
    words_to_translate = get_words_to_translate(input("\nType your English sentence: "))
    translation = translate(words_to_translate, english_to_hmong)
    count_words(word_count, words_to_translate)
    print_hmong_text(translation)
    handle_continue(
        yes_f = translate_loop(english_to_hmong, word_count),
        no_f = print_word_frequency(word_count),
        prompt="Another translation (Y/N): "
    )

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

def translate(sentence: list, lang_to_lang: dict) -> str:
    translation = ""
    for word in sentence:
        d_item = lang_to_lang.get(word, "?") + " "
        translation += d_item
    return translation

def count_words(word_count: dict, words_to_count: list):
    for word in words_to_count:
        word_count[word] = word_count.get(word, 0) + 1


def print_hmong_text(text:str) -> None:
    print("\nHmong:",text)

def handle_continue(yes_f, no_f, prompt):
    cont = prompt_continue(prompt)
    if cont:
        print()
        yes_f()
    else:
        print()
        no_f()

def prompt_continue(prompt) -> str:
        read = lambda: input(prompt)
        cont = read()
        while cont not in ["Y", "y", "N", "n"]:
            print(f"Invalid input. You entered {cont}.")
            cont = read()
        return cont in ["Y", "y"]

def print_word_frequency(word_count: dict) -> None:
    fmt = lambda s: "{: <12}".format(s)
    title = f"{fmt('Word')}{fmt('Frequency')}"
    bar = "-" * 23
    print(title)
    print(bar)
    for k,v in word_count.items():
        print(f"{fmt(k)}{fmt(v)}")

if __name__ == "__main__":
    main()