Here's a problem statement that you can work on to improve your string operations in Python, inspired by Attack on Titan:

**Problem Statement:**

In the world of Attack on Titan, the Scout Regiment is searching for a way to infiltrate the walls to reclaim their world. They've discovered a cryptic message etched into the wall, which reads: "The Titans' weakness lies in the patterns of their roar."

The message is encrypted using a Caesar Cipher, where each letter is shifted by a certain number of positions. The Scout Regiment has found a few decrypted letters, but they still need to figure out the pattern to crack the code.

**Task:**

Write a Python function that takes a string as input, representing the encrypted message. The function should return the decrypted message, using the Caesar Cipher technique.

**Test Cases:**

1. `input_string = "GUR PENML XRL VF ZL FRPERG"` should return `output_string = "THE WALL IS OUR FUTURE"`
2. `input_string = "FURRQ CVYYRQ VF ZL ZRQF"` should return `output_string = "THE TITANS ARE OUR ENEMY"`
3. `input_string = ""` should return `output_string = ""`

**Constraints:**

* The input string will contain only uppercase letters and spaces.
* The decrypted message should be in English.
* The Caesar Cipher shift is a single fixed number (you can assume it's 3, for simplicity).

**Hint:**

You can use the `ord` and `chr` functions to manipulate the ASCII values of the characters. You can also use a dictionary or a list comprehension to create a mapping of the encrypted characters to their decrypted counterparts.

Take your time to work on this problem, and don't hesitate to ask for help if you get stuck!