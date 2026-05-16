# Python basics
## Variables
x=1
x=x+1
** power (number ** power level)
% remainder (division but only gives the remainder)

int (integers)
floating point number (any number with a decimal part, e.g. 1.2; 1234.932746; 3.0)

float() <- turns int into a floating number
int () <- does the opposite
you can use these two functions to also convert between strings and integers

input() <- returns a string (a respose from a user)

## Conditional statements
Comparison (logical) operators - they look at variables, but don't change them
">" Greater than
">=" Greater than or equal to
"!=" Not equal
"==" Equal to

indentation (usualy 4 spaces) always after colon

if __ :
    what should the code do?
elif __ : (else if)
else :

Preventing tracebacks:
try:
    if the code fails...
except:
    ...do this

## Definitions

Kinda like a variable but for code

def ___ ():
    function a
    function b
    etc.

only stores whatever's inside, doesn't automatically invoke the code

## Loops and iterations 

Key words:

While  ___ :
	Logic statement inside __

For __ in [some collection]:
	Some variable (e.g. i)

Iteration variables are necessary, so that the code doesn’t run forever. They need to be put inside a loop functions.

Break <- statement word to end a loop (skips out of the loop)
Continue <- statement word to end this iteration and go to the next (run the loop from the beginning) (skips to the top of the loop)

Example collection (list):
Friends = [‘adam’, ‘mark’, ‘bob’]

Boolean variable <- a variable with only True/False values
None variable <- no asssigned value (flag value)
...is True/False/None

## Lists, tuples, sets
### Lists
mutable

e.g.
courses = ['History', 'Math', 'Physics', 'CompSci']

len(courses) <- number of values inside (4)
courses[0] <- [index], starts from 0, allows us to access a value (here: 'History') using it's location (total length - 1), we can also count the other way, -1 being the last variable and so on
[0:2] allows us to access all values starting at position 0, until 2 (but not including the two) <), 0 can be omitted [:2] and python will count from the first value (0), same works the other way: [2:] takes all values from the 3rd until the last one

modifying lists:

courses.append('Art') <- adds 'Art' value to the courses list
courses.insert(0, 'Art') <- adds 'Art' value to the position 0 (1st) in the courses list
    another list could be inserted instead of a value, resulting in a list within a list (that takes a position of one of the variables)

    courses_2 = ['PE', 'Music']
courses.extend(courses_2) <- adds values from courses_2 to the courses list

other methods:
.remove() <- removes a value from a list
.pop() <- removes a value (last one if stock), if we add a variable before the command (e.g. popped = list.pop()) we can assign it with the value popped
.reverse() <- reverses the order of values in a list
.sort() <- sorts values contained inside a list (strings are sorted alphabetically, numerical values in an ascending order)
.sort(reverse=True) <- reverses
.index() <- returns the position of whathever we search for (e.g. print(courses.index('CompSci')) would return a 3 (4th position))

functions:
sorted() <- doesn't change the order inside a list, only returns it in a sorted order
min() <- returns the minimum value within a list
max() <- returns the maximum value within a list
sum() <- returns the sum of all values contained within a list
enumerate() <- returns the position and value (e.g. for index, course in enumerate(courses):    print(index, course); we can add', start=1' after courses to start counting from 1, instead of 0)

print('Art' in courses) <- returns a value False, as 'Art' is not in the list
variable = ', '.join(courses) <- turns all the values inside a list into a string
    can also do ' - ', etc.
variable_2 = variable.split(' - ') <- splits a string into a list of values basased on ' - '

empty_list = []
empty_list = list()

### Tuples
immutabble 
basically same as a list, only can't be modified
uses parenthesis () instead of square brackets []

empty tuple = ()
empty tuple = tuple()

### Sets
values have no order, removes duplicates
uses curly braces {}
optimised for finding values and removing duplicates

set_1.intersection(set_2) <- finds values shared by both courses
.difference(set_2) <- set_1 - set_2
.union() <- +

empty_set = set() <- creates an empty set
empty_set = {} <- wrong! creates a dictionary 
## Dictionaries

key-value pairs

e.g. 
student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}

"name", "age", "courses" here are keys  
keys can be strings, or integers 

student(["name"]) 
student.get("name")

print(student.get("phone"))
None  <- key doesn't exist

print(student.get("phone", "Not found"))
Not found

student["phone"] = "555-555-555"
student.update({"name": "Jane", "age": 26, "phone": "222-222-222"})
both of these add or update values set to given keys 

del student["age"]
removes a key

age = student.pop("age")
removes a key from a dictionary, and creates a variable "age" that contains whatever the key did

len(student)
3  <- amount of keys inside a dictionary

print(student.keys())   <- prints out the keys inside
same for .values 
and .items , which shows both keys and values 

for key, value in student.items():
    print(key, value)