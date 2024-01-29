# Calculator App

This is a simple calculator app developed using the Kivy framework in Python. The calculator supports binary addition and subtraction, as well as the display of 1s complement of a binary number.

## Features
- Binary addition and subtraction.
- Display of 1s complement of a binary number.

## Requirements
- Python 3
- Kivy library

## Usage
1. Install the required library using the following command:
    ```bash
    pip install kivy
    ```

2. Run the calculator app using the provided Python script:
    ```bash
    python calculator.py
    ```

## How to Use
- Enter binary numbers using the provided buttons.
- Use the "+" and "-" buttons for binary addition and subtraction.
- Press the "=" button to calculate the result.
- Press the "C" button to clear the input.
- Press the "1s" button to display the 1s complement of the binary number.

## Code Overview
- The main logic is implemented in the `MainApp` class.
- Binary calculations are performed in the `on_solution` method using regular expressions to extract numbers and operators.
- The app uses Kivy's `TextInput`, `BoxLayout`, and `Button` for the user interface.

## Future Improvements
- Support for 2s complement calculation.
- Improved error handling and validation.

Feel free to contribute to the project and make it even better!
