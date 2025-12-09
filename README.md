# 🧮 Python Console Calculator

This repository contains a simple Python console calculator that performs basic arithmetic operations: addition, subtraction, multiplication, and division.
The program allows the user to continue calculations using the previous result or start a new calculation at any time.

## ✨ Features

* ➕ Addition

* ➖ Subtraction

* ✖️ Multiplication

* ➗ Division

* 🔁 Continue calculating using the last result

* ♻ Restart the calculator with a new number

## 📌 How It Works
```
The program asks the user for the first number.

It displays the list of available operations (+, -, *, /).

The user chooses an operation and provides the second number.

The result is shown.

The user can:

Press 'y' to continue calculating with the current result

Press 'n' to start a new calculation

The process repeats indefinitely until the program is manually stopped.
```
## 📂 Code Overview

The calculator includes four function definitions:
```
def sum(first, second):
    return first + second

def minus(first, second):
    return first - second

def multiply(first, second):
    return first * second

def division(first, second):
    return first / second
```

The main logic is handled in the home() function, which manages user input, operation selection, result display, and calculator flow control.

## ▶️ Running the Program

Make sure you have Python 3.10+ (for match-case syntax).

Run the script using:

```python calculator.py```

## 📄 Example Usage
```
What's first number? 10
+
-
*
/
Pick an Operation: *
What's next number? 3
10.0 * 3.0 = 30.0
Type 'y' to continue calculationg with 30.0, or type 'n' to start a new calculation: y
+
-
*
/
Pick an Operation: -
What's next number? 5
30.0 - 5.0 = 25.0
```
