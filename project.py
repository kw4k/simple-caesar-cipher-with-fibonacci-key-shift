# Caesar Cipher with 1-dimension Fibonacci Key Shift Encryption/Decryption Program
# A simple encryption/decryption program that utilizes the Caesar cipher and incorporates a key + Fibonacci sequence shift instead of a single key shift.
# A CS50P(2024) Project
# by: kw4k
# github: https://github.com/kw4k
# edX Account: jayvee_abellon
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Encrypt/Decrypt with Fibonacci-Caesar Cipher.',
        usage='python %(prog)s [-h] [-e] [-d] [-t TEXT] [-f FILE] [-k KEY_SHIFT]',

        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
        Examples:
        python %(prog)s -e -t text -k Key Shift'          # Encrypt text
        python %(prog)s -d -f file -k Key Shift'          # Decrypt file
        ''')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the input text')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the input text')
    parser.add_argument('-k', '--key', type=int, required=True, help='Key shift value')
    parser.add_argument('-t', '--txt', type=str, required=False,
                        help='Text to be encrypted or decrypted')
    parser.add_argument('-f', '--file', type=str, required=False,
                        help='Text file to be encrypted or decrypted.')
    args = parser.parse_args()

    if args.txt: # for text option
        print(text_cipher(args.txt, args.key, args))
    elif args.file: # for file option
        print(file_cipher(args.file, args.key, args))
    else:
        raise ValueError("Unknown argument!")


def file_cipher(textfile, key, args):
    result = ""
    mode = ""
    with open(textfile, 'r') as file:
        contents = file.read()

    if args.encrypt:
        result = encrypt(contents, key)
        mode = "encrypt"
    elif args.decrypt:
        result = decrypt(contents, key)
        mode = "decrypt"
    else:
        raise ValueError("Unknown argument!")

    file_output = mode + "_" + str(key) + "_" + textfile  # example: encrypt_3_file.txt

    with open(file_output, 'w') as newfile:
        newfile.write(result)
    return f"\tProcessed file {colors.YELLOW}{textfile}{colors.RESET} with mode {colors.GREEN}{mode}{colors.RESET} and key shift of {colors.MAGENTA}{key}{colors.RESET} completed! Output is saved as {colors.RED}{file_output}{colors.RESET}."


def text_cipher(msg, key, args):
    if args.encrypt:
        return f"Plaintext: {colors.YELLOW}{msg}{colors.RESET}\nCiphertext: {colors.RED}{encrypt(msg, key)}{colors.RESET}\nKey Shift value: {colors.MAGENTA}{key}{colors.RESET}"
    elif args.decrypt:
        return f"Ciphertext: {colors.RED}{msg}{colors.RESET}\nPlaintext: {colors.YELLOW}{decrypt(msg, key)}{colors.RESET}\nKey Shift value: {colors.MAGENTA}{key}{colors.RESET}"
    else:
        raise ValueError("Unknown argument!")

def encrypt(msg, key):
    encoded = ""
    deflated = alphafy(msg)
    for i in range(len(deflated)):
        # fibonacci key shift
        n = int(key) + fibonacci(i)
        # placeholder
        ch = deflated[i]
        # if ch is uppercase
        if (ch.isupper()):
            encoded += chr((ord(ch) - 65 + n) % 26 + 65)
        # if ch is lowercase
        elif (ch.islower()):
            encoded += chr((ord(ch) - 97 + n) % 26 + 97)
        # if ch is non-alphabetic character
        else:
            encoded += ch
    return repack(msg, encoded)


def decrypt(msg, key):
    decoded = ""
    deflated = alphafy(msg)
    for i in range(len(deflated)):
        # fibonacci key shift
        n = int(key) + fibonacci(i)
        # placeholder
        ch = deflated[i]
        # if ch is uppercase
        if (ch.isupper()):
            decoded += chr((ord(ch) - 65 - n) % 26 + 65)
        # if ch is lowercase
        elif (ch.islower()):
            decoded += chr((ord(ch) - 97 - n) % 26 + 97)
        # if ch is non-alphabetic character
        else:
            decoded += ch
    return repack(msg, decoded)


def fibonacci(n):
    # Fn = [( (1 + √5)^n ) / (2^n × √5)]
    # switched formula to avoid overflow error
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

def alphafy(msg):
    # remove non-alphabetic characters
    result = ""
    for i in range(len(msg)):
        ch = msg[i]
        if (ch.isalpha()):
            result += ch
        else:
            result += ""
    return result

def repack(base, msg):
    # return non-alphabetic characters
    result = ""
    char_counter = 0
    for i in range(len(base)):
        ref = base[i]
        if (ref.isalpha()):
            result += msg[char_counter]
            char_counter += 1
        else: # if non-alphabetic character
            result += ref
            char_counter += 0
    return result

# for aesthetic
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'


if __name__ == "__main__":
    main()
