import random
import string


def generate_random_string(length):
    letters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    random_string = ''.join(random.choices(letters, k=length))
    return random_string


def main():
    password = generate_random_string(7)
    print(password)


main()
