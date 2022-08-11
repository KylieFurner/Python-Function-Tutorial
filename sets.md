# Sets
[Link Back To Welcome Page](welcome.md)

## Introduction
The first section I wrote was about stacks. One thing that matters with stacks
is the order. However, a set is a data structure where the order does not matter.
Another difference between a stack and set is that a set won't allow for duplicate
data to be entered. Because order doesn't matter and duplicate data can't be 
entered sets are a very efficient way to find data. Using hashing sets can add, 
remove, and test for membership in O(1) time.

## Hashing
Let's consider a simple example of how to use a set to achieve O(1) operation.
If we want to store a set of all the single digit numbers (0-9) we would need a
set with an index of 10. An easy way to achieve O(1) would be to use a function
such as ```index(n) = n``` 
This function means that the value would be equal to it's place on the index
For example:
index | 0 | 1 | 2 | 3 | 4 | 5  
----- | - | - | - | - | - | -
n | - | 1 | 2 |  - | 4 |  -

Notice how this list isn't filled in completely. This is called a sparse list. 
Only sets can be a sparse list and this ability is one of the things that makes 
sets unique, they don't have to be filled in from left to right. And because each
place can only be filled by a specific value sets are able to avoid duplicate data.

### A More Complicated Problem
The example above is pretty straightforward, but what if we wanted to accomplish
something a little bigger or more complicated such as storing every number from 
(0- 999,999,999) If we tried to make a set with a billion bits that would take 
up way to much data. We can accomplish a storing large numbers with a technique 
called hashing. Python has a built in hash function hash(n). 
*Hashing can also be used with floats and strings but not on lists*
Using a sparse list of 10 and hashing we can store large numbers using the general
function: ```index(n) = n % sparse_list_size```
With our example problem of storing large numbers our equation would look like
this: ```index(n) = n % 10``` 
This means that (788899965) = 788899965 % 10 = index 5
and (645372812) = 645372812 % 10 = index 2
There is only one problem with this method and that is conflicts. Above we have a
number that fits into index 5, but there can be several numbers that fit into that
same index for example (988765435)

## Dealing With Conflicts
There are two ways programmers often deal with conflicts. The first is to use a 
technique called **open addressing**. Open addressing means that when a conflict is
found the program will move to the right of the index until an open space is found
to place the data into. However, there are a few problems with this technique the main
problem is that it can create a build up of conflicts. If a number is placed in an
index different from the one it was supposed to be in originally, it might displace
a future number that does belong to that index.
![Open Addressing](https://byui-cse.github.io/cse212-course/lesson05/set_10digit_open_addressing.jpeg)

The second way to deal with conflicts is a technique called **chaining**. Chaining means
that we create a list for all values that would occupy the same space instead of moving the
value around. This technique will create small clusters of data
![Chaining Example](https://byui-cse.github.io/cse212-course/lesson05/set_10digit_chaining.jpeg)

The thing to look out for with both of these techinques is that they can affect our O(1)
performance. If there are too many conflicts the O(1) performance can begin to look more
like an O(n) performance. To fix this we would have to increase the size of the sparse list
and then run the index function again with the new sparse list.

## Example
To create a set use curly braces and you can put whatever you want into your set and
it will automatically discard duplicates
```
set = {1,2,3,4,4,5,5,6,6,6,6}
print(set)
'''outputs {1,2,3,4,5,6}'''

print(set.pop())
print(set)
'''shows the value removed and then prints the set: 1 {2,3,4,5,6}'''

set.clear()
'''clears the set: if you print the set it outputs set()'''

You can also create union sets and intersecting sets using the and(&) or(|) functions
Ex:
set1 = {1,2,3,4,5,6}
set2 = {1,3,5,7,8,9}
union = {set1 | set2}
'''outputs {1,2,3,4,5,6,7,8,9}'''
intersecting = {set1 & set2} 
'''outputs {1,3,5}
```
Try solving both a union and an intersecting sets with for loops (solutions below)

Union:
```
    for n in set1:
        if n not in set2:
            set2.add(n)   
    return set2
```
Intersecting:
```
    intersecting_set = set()
    for n in set1:
        if n in set2:
            intersecting_set.add(n)
    return intersecting_set
```
## Problem to Solve
With all these examples on how sets work lets solve a problem
Above there is an example of how to find intersecting and union sets. Now lets try making 
a set from the differences.
Ex:
```
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
#Find the difference for s1 - s2 which would be {1,2,3}
```

## Solution
Try using loops.
[Solution](solution2.py)
