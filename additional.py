import time


def print_text_slowly(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    return "> "

def press_any_key_to_continue():
    input("Press Enter to continue...")