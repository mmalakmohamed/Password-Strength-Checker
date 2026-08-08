# Password Strength Checker

A Python-based Password Strength Checker developed as part of my cybersecurity internship at DecodeLabs.

## Project Description

This project evaluates the strength and validity of a password based on different characteristics.

The program checks:

- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Symbols

It then calculates a password score and determines whether the password is **Valid or Invalid** and whether its strength is **Weak, Medium, or Strong**.

## Features

- Checks password length
- Detects uppercase letters
- Detects lowercase letters
- Detects numbers
- Detects symbols
- Calculates a password score
- Determines password validity
- Classifies password strength as Weak, Medium, or Strong

## Technologies Used

- Python
- Visual Studio

## How to Run

1. Download the `password_strength_checker.py` file.
2. Open the file using Python or Visual Studio.
3. Run the program.
4. Enter a password when prompted.
5. The program will display the password validity, score, and strength.

## Testing

The program was tested using different password examples, including:

| Test | Input | Expected Result |
|---|---|---|
| 1 | hello | Invalid / Weak |
| 2 | helloooo | Valid / Weak |
| 3 | Hello123 | Valid / Medium |
| 4 | Hello@1234567 | Valid / Strong |

Detailed test cases are available in `test_cases.txt`.

Screenshots of the test results are also included in this repository.

## Project Files

- `password_strength_checker.py` — Main Python program
- `test_cases.txt` — Test cases used to evaluate the program
- Test screenshots — Screenshots showing the program's results

## Internship

This project was developed as part of my cybersecurity internship at **DecoLabs**.
