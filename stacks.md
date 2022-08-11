# Stacks
[Link Back To Welcome Page](welcome.md)

## Introduction
Stacks are very similar to the python function lists.
One of the differences is that stacks are very particular
about the order information is added and taken out.
This is often represented by the phrase:
*"Last in First Out" or "LIFO"*

## A Stack of Pancakes
A great comparison to the stack function is a stack of pancakes.
This example is also great for demonstrating LIFO
When pancakes are being made the first one ready goes on the plate first
As more pancakes are added they are added on top making the first
pancake the bottom of the stack. Because it is at the bottom it will be 
the last pancake selected from the stack because if someone wanted the
bottom pancake the whole pile would fall over! This is the same thing 
for stacks in python, the first bit of information would be the
last bit removed.

![Stack Diagram](https://byui-cse.github.io/cse212-course/lesson03/pancake_stack.jpeg)

## The Undo Function

Another great comparison to the function of a stack is the Undo
function that can be seen all over. For example if we added five
words to a stack 
*"The little boy ran home"* 
by pressing undo the first word to be removed, or popped, from 
the stack would be "home" 
*"The little boy ran"*
If we pressed undo again the next to be removed would be 
"ran" 
*"The little boy"*
Let's say we then decided to add more to the sentence and
we typed "has blonde hair"
*"The little boy has blonde hair"*
Even though the first three words have been in the stack for
a longer period of time pressing undo would still remove the last word
which in this example would be "hair" leaving us with
*"The little boy has blonde"*

### How to Undo
So we now have two examples of how stacks would work but how do
we implement a stack in python?

Operation | Description | Code in Python 
--------- | ----------- | ----------------
Create a Stack | We create stacks the same way we creat lists | ``` stack = [] ```
push(value) | This is how we add a value into the back of the stack | ``` stack.append(value) ```
pop() | To remove from a stack we use the pop function and remember this will remove whatever was last entered into the stack | ``` value = stack.pop() ```
size | To check the length of a stack | ``` length = len(stack) ```

Each of these functions have a performance of O(1)


## Example
Below is a basic program using a stack
The purpose of the program is to reverse the order of the entered
text. The word entered would be "Racecar" and the result would be racecaR

    def mystery_1(text):
        stack = []
        for letter in text:
            stack.append(letter)
        result = ""
        while len(stack) > 0:
            result += stack.pop()
        return result

    print(mystery_1("Racecar"))

## Problem to Solve
Try writing a program in which the user inputs each TV show or movie
they have watched. The final program will output the order of what they
watched from most recent to latest similar to how Netflix gives its users 
a most recently watched section.
Also like Netflix lets set a limit as to how many shows or movies are displayed

Ex: Lets say the user inputs that they watched these five movies in this order
    1. Beauty and The Beast
    2. Sleeping Beauty
    3. Cinderella
    4. The Little Mermaid
    5. Frozen
    6. Moana

    If we set a limit to show their five most recently watched programs we would display:

    "Your 5 most recently watched programs:
        1. Moana
        2  Frozen
        3. The Little Mermaid
        4. Cinderella
        5. Sleeping Beauty"


## Solution
[An Example Solution](solution1.py)