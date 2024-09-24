### Practice Puzzles: Operators and Logical Comparisons

Start a new notebook for this exercise. Keep it neat and explain what you’re doing (which puzzle you’re on and whatever else you’d like to say!) using markdown cells.

---

To start, set the following variables in your notebook for this homework:

```python
ayy = 2
bee = 7
sea = 1
dee = 8
```
#### Use operators to answer the following riddles. 

For each riddle, use [f-strings](https://docs.python.org/3/tutorial/inputoutput.html) to print the output as a sentence – for example “The magic 8-ball declares that bee is greater than ayy!”

* Is ayy bigger than dee?
* Is ayy plus bee greater than dee?
* Is bee times ayy less than dee plus bee?
* Are **both** ayy less than bee **and** sea less than dee true?
* Are **both** bee plus sea equal to dee **and** ayy times bee plus ayy equal to ayy times dee true?

---

#### The `input()` function

To make our code interactive, we can give it the most basic of user interfaces: `input()`

#### input() function

To make our code interactive, we can give it the most basic of user interfaces: `input()`

Try this in a code cell. After you run it, a little box will appear somewhere for you to type in (sorry Liberal Arts majors, that should be “…in which for you to type.”). It might be right under or over your code cell, or it might be at the top of the browser window. Type your name and hit <return>.

```python
my_name = input("Hi! I'm your code! What's your name? \n")
print(f"Nice to meet you, {my_name}! \n I'm your code, so you can call my anything...")
```

**Before you move on**

- Check the `type()` of `my_name`!
- Can you figure out what the `\n` is doing in the strings above?

---

For each riddle below, use the `input()` function to get data from your user (which is you!). *Each riddle should operate on a new input!* As before, make sure the output is pretty (and perhaps witty).

* Are there 5 or more letters in your name?
* Have the user type a number (like “42”). Is the input greater than 11? *Make sure the answer is (mathematically) correct!*
* Return the square of an input number.
* Have the user enter their name again. Is the name, *left as a `str`*, greater than “Hello”? What do you think about this result? How can one letter be “greater than” another?
* Have the users type two numbers with a space in between. Tell the user the remainder when the first number is divided into the second. (Note: You’ll have to extract the two numbers out of the input string.)
* Have the user enter 4 numbers (you can use `input()` 4 times rather than trying to carve up a single input string). Is the first greater than the second `and` the third greater than the fourth?
* Write a little “adding machine” that adds two numbers from the user and prints the result.
* Have the user enter two single letters (you can have them enter just the numbers, the numbers with a space, or use `input()` twice). Which letter is greater? Now use the `ord()` function on each of the letters (e.g. `ord("h")`). Does the output from `ord()` agree with your “greater than” comparison.
* Write a `for()` loop to go through an input string (like your name) and print the `ord()` value of each letter. Print the `ord()` values from your name and from the string “Hello”? Try different names like “Zoe” and “Aaron” and see if you can figure out how Python determines if one string is “greater than” another.