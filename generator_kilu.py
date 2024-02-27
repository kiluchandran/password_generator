import random
import string


def main():
    N = 7
    letters = string.ascii_uppercase
    print(random.choices(letters, k=N))


main()
