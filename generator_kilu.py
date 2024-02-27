import random
import string


def generate_random_string(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def main():
    password = generate_random_string(7)
    print(password)


main()
