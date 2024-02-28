import random
import string
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", type=int,
                    help=" length of the password")
args = parser.parse_args()


def generate_random_string(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def main():
    if args.length:
        no_of_characters = args.length
    else:
        no_of_characters = 10
    password = generate_random_string(no_of_characters)
    print(password)


main()
