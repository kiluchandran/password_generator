import random
import string


def main():
    N = 7
    letters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = ''.join(random.choices(letters, k=N))
    print(password)


main()
