from random import *
import os

TRIES = 7


class Cl:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    ORANGE = "\033[38;5;214m"
    UNDERLINE = "\033[4m"
    ITALIC = "\033[3m"
    LIGHT_PURPLE = "\033[38;5;141m"
    END = "\033[0m"


def get_word():
    return choice(word_list).upper()


def display_person(tries):
    return stages[tries]


def open_letters(ltr, original_word, hidden_word):
    for i, letter in enumerate(original_word):
        if letter == ltr:
            hidden_word[i] = ltr


def play(word):
    hid_word = list(word)
    word_completion = ["_"] * len(word)
    guessed_letters, guessed_words = [], []
    cur_tr = 0
    text = ""

    print(
        Cl.LIGHT_PURPLE
        + Cl.ITALIC
        + "\nLet's play the game "
        + Cl.END
        + Cl.BOLD
        + Cl.RED
        + "'GALLOWS'"
        + Cl.END
    )
    print(
        Cl.LIGHT_PURPLE
        + Cl.ITALIC
        + "Number of letters in the hidden word: "
        + Cl.END
        + Cl.YELLOW
        + str(len(hid_word))
        + Cl.END
    )
    while True:
        if text != "":
            if len(text) == len(hid_word):  # Проверка на слово полностью
                if text in guessed_words:
                    print(
                        Cl.LIGHT_PURPLE
                        + Cl.ITALIC
                        + "\nYou've already tried word "
                        + Cl.END
                        + Cl.CYAN
                        + text
                        + Cl.END
                        + Cl.LIGHT_PURPLE
                        + Cl.ITALIC
                        + ". It's not it!"
                        + Cl.END
                    )
                else:
                    guessed_words.append(text.upper())
                    if text.upper() == "".join(
                        hid_word
                    ):  # Проверка на ввод слова полностью
                        print(
                            Cl.LIGHT_PURPLE
                            + Cl.ITALIC
                            + "Hooray! You win! "
                            + Cl.END
                            + "\U0001F911"
                        )
                        break
                    else:
                        print(
                            Cl.LIGHT_PURPLE
                            + Cl.ITALIC
                            + "\nUnfortunately, you guessed wrong! "
                            + Cl.END
                            + "\U0001F618"
                        )
                        cur_tr += 1

            elif not text.isalpha() or len(text) != 1:
                print(Cl.RED + Cl.BOLD + "\nWrong input!" + Cl.END)

            elif text in guessed_letters:
                print(
                    Cl.LIGHT_PURPLE
                    + Cl.ITALIC
                    + "\nYou've already tried letter "
                    + Cl.END
                    + Cl.CYAN
                    + text
                    + Cl.END
                    + Cl.LIGHT_PURPLE
                    + Cl.ITALIC
                    + ". It's not it!"
                    + Cl.END
                )

            else:
                guessed_letters.append(
                    text
                )  # Добавляем букву в список уже названных букв
                if text in hid_word:  # Если буква была угадана
                    open_letters(text, hid_word, word_completion)
                    if (
                        word_completion == hid_word
                    ):  # Проверка на случай угадывания слова по одной букве
                        print(
                            Cl.LIGHT_PURPLE
                            + Cl.ITALIC
                            + "Hooray! You win! "
                            + Cl.END
                            + "\U0001F911"
                        )
                        break
                    else:
                        print(
                            Cl.LIGHT_PURPLE
                            + Cl.ITALIC
                            + "\nYou guessed! The letter "
                            + Cl.END
                            + Cl.CYAN
                            + text
                            + Cl.END
                            + Cl.LIGHT_PURPLE
                            + Cl.ITALIC
                            + " is in the word."
                            + Cl.END
                        )

                else:
                    print(
                        Cl.LIGHT_PURPLE
                        + Cl.ITALIC
                        + "\nUnfortunately, you guessed wrong! "
                        + Cl.END
                        + "\U0001F618"
                    )
                    cur_tr += 1

        if cur_tr == TRIES:
            break

        print("\n" + Cl.YELLOW + display_person(cur_tr) + Cl.END)
        print(
            Cl.LIGHT_PURPLE
            + Cl.ITALIC
            + "Word: "
            + Cl.END
            + Cl.CYAN
            + " ".join(word_completion)
            + Cl.END
        )

        print(
            Cl.LIGHT_PURPLE
            + Cl.ITALIC
            + "\nEnter letter or the whole word: "
            + Cl.END
            + Cl.CYAN,
            end="",
        )
        text = input().upper()
        print(Cl.END, end="")
        os.system("cls")

    if cur_tr == TRIES:
        print(Cl.RED + Cl.BOLD + "\n    GAME_OVER" + Cl.END)
        print("\n" + Cl.YELLOW + display_person(TRIES) + Cl.END)
    print(
        Cl.LIGHT_PURPLE
        + Cl.ITALIC
        + "Hidden word: "
        + Cl.END
        + Cl.CYAN
        + " ".join(hid_word)
        + Cl.END
    )


# ------------------------- Main ------------------------------------
f_words = open("words.txt", "r", encoding="utf-8")
word_list = []
while True:
    buffer = f_words.readline()[:-1]
    if not buffer:
        break
    word_list.append(buffer)
f_words.close()

f_person = open("person(1).txt", "r", encoding="utf-8")
stages = []
while True:
    buffer = f_person.readline()[:-1]
    if buffer == "#":
        break
    if not buffer:
        cur_part = ""
        while True:
            picture = f_person.readline()[:-1]
            if not picture:
                break
            cur_part += picture + "\n"
    stages.append(cur_part)
f_person.close()

play(get_word())

while True:
    print(
        Cl.LIGHT_PURPLE
        + Cl.ITALIC
        + "\nDo you want to play again? "
        + Cl.END
        + Cl.GREEN
        + "YES <-> NO"
        + Cl.END
    )
    print(Cl.LIGHT_PURPLE + "> " + Cl.END + Cl.CYAN, end="")
    repeat = input().upper()
    print(Cl.END, end="")
    if repeat == "YES":
        os.system("cls")
        play(get_word())
    elif repeat == "NO":
        print(
            Cl.LIGHT_PURPLE
            + Cl.ITALIC
            + "\nThanks for playing! See you! "
            + Cl.END
            + "\U0001F609\n"
        )
        break
    else:
        print(
            Cl.LIGHT_PURPLE
            + Cl.ITALIC
            + "\nDon't understand, please repeat "
            + Cl.END
            + "\U0001F644"
        )
