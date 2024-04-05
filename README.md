
# Caesar Cipher with 1-dimension Fibonacci Key Shift Encryption/Decryption Program

## Description
This is a simple encryption/decryption program that utilizes the Caesar cipher and incorporates a key + Fibonacci sequence shift instead of a single key shift.

## Note

This Caesar Cipher with 1-dimension Fibonacci Key Shift Encryption/Decryption Program is my submission for Harvard's [CS50P(2024)](https://cs50.harvard.edu/python/2022/) course Final Project.

## Author

- Jayvee Abellon - [kw4k](https://www.github.com/kw4k) / [jayvee_abellon](https://profile.edx.org/u/jayvee_abellon)

## How it works

The cipher operates similarly to a traditional Caesar Cipher. The key distinction lies in the fact that each character is shifted by the assigned key shift value, following the corresponding Fibonacci sequence according to the formula:

> K = k + Fn

where:

- **K**: represents the Fibonacci Key Shift.
- **k**: represents the integer value of the key shift.
- **Fn**: represents the nth Fibonacci number, starting from zero (0). The maximum value of n corresponds to the total count of alphabetic characters to be ciphered.

For example, if we encrypt the string "Hello, World!" with a key shift value of 3, the output would be "Kipqu, Ezhjo!". The Fibonacci sequence Fn would have a maximum value of 10. Non-alphabetic characters are not counted.

**Plaintext:**
> *Hello, World!*

**Using the formula K = k + Fn:**

> 3, 4, 4, 5, 6, 8, 11, 16, 24, 37

**Resulting shifted characters:**

> K, i, p, q, u, E, z, h, j, o

**Resulting ciphertext:**

> *Kipqu, Ezhjo!*


## Usage

```python project.py [-h] [-e] [-d] [-t TEXT] [-f FILE] [-k KEY_SHIFT]```

## Arguments
- `-e, --encrypt`: Encrypt mode.
- `-d, --decrypt`: Decrypt mode.
- `-k, --key`: Key shift value.
- `-t, --txt`: Text to be encrypted or decrypted.
- `-f, --file`: File to be encrypted or decrypted.

## Examples

```python project.py -e -t "Hello, World!" -k 3```

![Text Encrypt](https://i.imgur.com/CYVjV9j.png)

```python project.py -d -t "Kipqu, Ezhjo!" -k 3```

![Text Decrypt](https://i.imgur.com/5miluRt.png)

```python project.py -e -f file2.txt -k 9```

![CLI](https://i.imgur.com/j07B4ew.png)

Original File:

![File original](https://i.imgur.com/6dhYOXq.png)

Output File:

![File output](https://i.imgur.com/QSxeS6l.png)


## Dependencies

- Python 3

## Installation

Simply download the `project.py` python file.

## References

- [Fibonacci Sequence - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_sequence)
- [Fibonacci Number - Wolfram MathWorld](https://mathworld.wolfram.com/FibonacciNumber.html)
- [Caesar Cipher - Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
Special thanks to the [CS50P(2024)](https://cs50.harvard.edu/python/2022/) course for inspiration and guidance.
