import random
import string


def main():
    N = 7
    letters = string.ascii_uppercase + string.ascii_lowercase
    password = ''.join(random.choices(letters, k=N))
    print(password)


main()
