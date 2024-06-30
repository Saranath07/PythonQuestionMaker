Here's a problem statement that involves string operations in Python, which might be challenging for you to solve:

**Problem Statement:**

The Scout Regiment from Attack on Titan is on a mission to clear the Titans from the city. They have received a message from their leader, Captain Levi, that contains a list of Titan names and their corresponding strengths. The message is encrypted and can only be decrypted by finding the substrings in the message that match the Titan names.

Write a Python function that takes a string as input, which is the encrypted message, and returns a list of substrings that correspond to the Titan names. The function should return the substrings in the order they appear in the message.

**Test Cases:**

1. Input: "Eren Yeager 100, Mikasa Ackerman 90, Armin Arlert 80, Sasha Braus 70"
Output: ["Eren Yeager", "Mikasa Ackerman", "Armin Arlert", "Sasha Braus"]

2. Input: "Reiner Braun 100, Bertholdt Fuber 90, Erwin Smith 80, Annie Leonhart 70"
Output: ["Reiner Braun", "Bertholdt Fuber", "Erwin Smith", "Annie Leonhart"]

3. Input: "Levi Ackerman 100, Erwin Smith 90, Hange Zoë 80, Conny Springer 70"
Output: ["Levi Ackerman", "Erwin Smith", "Hange Zoë", "Conny Springer"]

4. Input: "Some random text that does not contain Titan names"
Output: an empty list []

**Constraints:**

* The input string will only contain letters, spaces, and digits.
* The Titan names will always be in the format "First Name Last Name" separated by a space.
* The strengths will always be integers.
* The function should return the substrings in the order they appear in the message.

**Bonus Challenge:**

Can you modify the function to also return the strengths of the Titans along with their names? For example, the output for the first test case could be `[("Eren Yeager", 100), ("Mikasa Ackerman", 90), ("Armin Arlert", 80), ("Sasha Braus", 70)]`.