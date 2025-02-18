"""
Python Coding Challenges on Strings
-----------------------------------
1.Write a function in Python to check duplicate letters. It must accept a string, i.e., a sentence. The function should return True if the sentence has any word with duplicate letters, else return False.
2.Write a code in Python to create a Morse code translator. You can take a string with alphanumeric characters in lower or upper case. The string can also have any special characters as a part of the Morse code. Special characters can include commas, colons, apostrophes, exclamation marks, periods, and question marks. The code should return the Morse code that is equivalent to the string.
3.Write a function to detect 13th Friday. The function can accept two parameters, and both will be numbers. The first parameter will be the number indicating the month, and the second will be the year in four digits. Your function should parse the parameters, and it must return True when the month contains a Friday with the 13th, else return False.
4.Write a function to find the domain name from the IP address. The function will accept an IP address, make a DNS request, and return the domain name that maps to that IP address while using records of PTR DNS. You can import the Python socket library.
5.Write a function in Python to parse a string such that it accepts a parameter- an encoded string. This encoded string will contain a first name, last name, and an id. You can separate the values in the string by any number of zeros. The id will not contain any zeros. The function should return a Python dictionary with the first name, last name, and id values. For example, if the input would be “John000Doe000123”. Then the function should return: { “first_name”: “John”, “last_name”: “Doe”, “id”: “123” }
6.Write a function in Python to convert a decimal to a hex. It must accept a string of ASCII characters as input. The function should return the value of each character as a hexadecimal string. You have to separate each byte by a space and return all alpha hexadecimal characters as lowercase.
7.Write a code in Python to find out whether a given string S is a valid regex or not.
"""
import datetime
import socket
import re

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/', 
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}


def check_dup_letters(str):
    """
    Function in Python to check duplicate letters. It must accept a string, i.e., a sentence.

    :return : True if the sentence has any word with duplicate letters, else return False.
    """
    check_str = str.lower().split()
    seen = set()
    for word in check_str:
        if word in seen:
            return True
        seen.add(word)

    return False


def morse_code_translator(word):
    """
    2. Part I. Create a Morse code translator. You can take a string with alphanumeric characters in lower or upper case. \
    The string can also have any special characters as a part of the Morse code.
    Special characters can include commas, colons, apostrophes, exclamation marks, periods, and question marks.

    :return : The code should return the Morse code that is equivalent to the string.
    """

    if word is not None:
        return ' '.join(MORSE_CODE_DICT.get(char.upper(),'') for char in word)


def morse_code_to_text(word):
    """
    2. Part II.Translate Morse code to text
    """
    REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}
    word = word.split('/')
    decoded_word = []
    for str in word:
        decoded_word.append(''.join(REVERSE_MORSE_CODE_DICT.get(char, '')for char in str.split(' ')))
    return ' '.join(decoded_word)


def detect_friday_13(month, year):
    """
    Detect 13th Friday. The function can accept two parameters, and both will be numbers.
    The first parameter will be the number indicating the month, and the second will be the year in four digits.

    :return : True when the month contains a Friday with the 13th, else return False.
    """
    return datetime.date(year, month, 13).weekday() == 4


def detect_domain_name(ip_address):
    """
    Function to find the domain name from the IP address. The function will accept an IP address, make a DNS request,

    :return : the domain name that maps to that IP address while using records of PTR DNS. You can import the Python socket library.

    """
    try:
        return socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        return "No domain find for this ip"


def parse_encoded_string(encoded_string):
    """
    Function in Python to parse a string such that it accepts a parameter- an encoded string.
    This encoded string will contain a first name, last name, and an id. You can separate the values in the string by any number of zeros.
    The id will not contain any zeros. The function should return a Python dictionary with the first name, last name, and id values.
    For example, if the input would be “John000Doe000123”. Then the function should return: { “first_name”: “John”, “last_name”: “Doe”, “id”: “123” }

    :return : dict
    """

    match = re.search(r"([^\w\d]+)", encoded_string)
    sep = match.group(1) if match else None
    print(sep)
    if not sep:
        return "Invalid input parameter "

    parts = encoded_string.split(sep)
    if len(parts) < 3:
        return "Invalid input parameter"
    return {"first_name": parts[0],
            "last_name" : parts[1],
            "id" : sep.join(parts[2:])}


def convert_dec_to_hex(ascii_char):
    """
    Function in Python to convert a decimal to a hex. It must accept a string of ASCII characters as input.
    The function should return the value of each character as a hexadecimal string.
    You have to separate each byte by a space and return all alpha hexadecimal characters as lowercase.

    """
    # for octal
    #  ' '.join(format(ord(char),'03o') for char in ascii_char)
    return ' '.join(format(ord(char),'02x') for char in ascii_char)



def check_valid_regex(s):
    """
    Function to find out whether a given string S is a valid regex or not.
    """
    try:
        re.compile(s)
        return True
    except re.error:
        return False

    
if __name__ == '__main__':
    test_str = 'There is a boy named Hans'
    bool_check = check_dup_letters(test_str)
    print(bool_check)
    morse_code = morse_code_translator("Hello")
    print(morse_code)
    morse_text = morse_code_to_text(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
    print(morse_text)
    is_friday = detect_friday_13(5, 1994)
    print(is_friday)
    dns_name = detect_domain_name('127.56.1.3')
    print(dns_name)
    enc_word = parse_encoded_string("John000Doe000123")
    print(enc_word)
    hex_value = convert_dec_to_hex("Hi!")
    print(hex_value)
    print(check_valid_regex(r"^[a-z]+$"))
    