[Link to the lecture note](http://www.scipy-lectures.org/intro/language/python_language.html)

* type(VAR) tells the type of the variable, such as ___int___, ___str___, __etc__
* Scalar types: __int__, __float__, __complex__, __boolean__

# 1.2.2.2 Containers
## Lists
* Slicing list[start:stop:stride]. Therefore, a way to reverse a list would be list[::-1], alternatively use list.reverse(). Using __%timeit__ in ipython, I found out that list.reverse() is about 40% faster than list[::-1]. Note that list[::-1] gives a new object, while list.reverse() reverses in place.
* Sorting with __sorted__ gives a new object, while list.sort() will sort in place

## Strings
* Tripling the quotes with \'\'\' allows the string to span more than one line
* Strings are immutable; to change particular characters, use str.replace()
* Use help(str) to search for new methods

## Dictionaries
Dictionary, in the form of {key1:value1, key2:value2}, is unordered. To fetch the value of a key, use dict[key]

Notice the notation of defining the dictionary, which uses braces, and of retrieving values, which uses square brackets.

## Tuples
Tuples, in the form of (item1, item2, item3) or simply item1, item2, item3, are immutable lists.

## Sets
Sets are unordered, unique items.

set.union, set.difference and set.intersection perform the operation of __union__, __setdiff__ and __intersect__ in R, respectively.

# 1.2.2.3 Assignment operator

It works in two steps.

1. An expression on the right hand side is evaluated, the corresponding object is created or obtained.
2. A ___name___ on the left hand side is assigned, or bound, to the r.h.s. (right-hand side) object.

* A simple object can have several names bound to it
  * obj1 is obj2 tests whether the two variables point to the same object
* Use index or slice to change in place
  * __id__ returns the identity of an object.

# 1.2.3 Control Flow

## if/elif/else

```{python if}
if 2**2 == 4:
	print('That is obvious!')


```{python condition}
%run condition.py
```

## for and range

```{python for}
for day in range(4):
	for term in ('great', 'interesting', 'not that slow'):
		print("day {}: python is {}".format(day, term))

```

The following code calculates the GC content in a sequence using for loop and __in__ 

```{python gc}
gc = 0
total = 0
seq = 'ATGCGGGTCTTGAGGGATTTTAGTGTTGT'
for n in seq:
	if (n in ('G','C')):
		gc += 1;
	total += 1

print("GC content = {gc:1.2f} ({gcCount}/{totalCount})".format(gc=gc/float(total), gcCount=gc, totalCount=total))
```

Iterate over any sequence

```{python vowel}
vowels = 'aeiou'
for i in 'powerful':
	if i in vowels:
		print(i)
```

```{python split}
message = "Life is beautiful"
message.split()
for word in message.split():
	print(word)
```

Use __enumerate__ to iterate over a sequence while keeping track of the item number

```{python enumerate}
words = ('cool', 'powerful', 'readable')
for index,item in enumerate(words):
	print((index, item))	
```
Use __items__ to loop over a dictionary

```{python items}
bundesliga = {'FCB':18, 'BVB':15, 'HSV':13, 'VFB':6}

for key, val in sorted(bundesliga.items()):
	print("%s has score: %d" % (key, val))
```

Note in the example above how to use __sorted__ to sort keys in a dictionary

List comprehension: like __sappy__ in R

```{python listComprehension}
[i**2 for i in range(4)]
```

Three ways to generate WallisPi

```{python WallisPi}
pi = 1
for i in range(1,1000000):
	fi2 = 4*(i**2)
	pi *= fi2/(fi2-1)
pi = pi*2
print('pi = {:1.9f}'.format(pi))
```

```{python WallisPi2}
wall = [i**2*4/(i**2*4-1) for i in range(1,100000)]
pi = 1.0
for p in wall:
	pi = pi * p
pi = pi*2
print('pi = {:1.9f}'.format(pi))
```

Finally, we set a epislon value and make sure that the pi value compared to the last iterator differ less than that threshold.

```{python WallisPi3}
pi = 1.0 * 4/(4-1)
i = 2
oldpi = 1.0
while pi-oldpi>1E-12:
	oldpi = pi
	pi = pi * 4*i**2/(4*i**2-1)
	i = i+1;
pi = pi*2
print("After {:d} iterators, pi = {:1.9f}".format(i, pi))
```
# 1.2.4 Functions

Use __def__ to define a function

```{python func}
def gc_content(seq):
	gc=0;
	for n in seq.lower():
		if n in ('g','c'):
			gc = gc + 1
	return(gc/len(seq))	

gc_content('ATGC')
gc_content('ATTGGCTGTTGAGCT')
```
If the value passed in a function is immutable, the function cannot modify the caller's variable. If the value is mutable, the function may modify the caller's variable in place.

```{python mutfunc}
def try_to_modify(x,y,z):
	"""A simply function to show the difference between mutable and immutable variables

	Extended summary which can contain multi-line comments
	"""
	x = 23
	y.append(42)
	z = [99]
	print(x)
	print(y)
	print(z)

a = 77 # immutable
b = [88] # mutable
c = (28)
try_to_modify(a,b,c)

print(a)
print(b)
print(c)
```

The docstring allows user to call __try_to_modify?__ to learn how to use the function.

```{python fib}
def fib(n):
	if(n==0):
		return(1)
	if(n==1):
		return(1)
	return fib(n-1)+fib(n-2)

for i in range(20):
	print("fib({})={}".format(i, fib(i)))
```

The function below implements the Quicksort algorithm. Notice how the lists are concatenated by __+__. One could also use list.extend() and list.append() but this way below is much simpler.

```{python quicksort}
def quicksort(array):
	less = []
	greater = []
	if(len(array)<2):
		return array
	pivot=array[0]
	for v in array[1:]:
		if(v < pivot+1):
			less.append(v)
		else:
			greater.append(v)
	res = quicksort(less)+[pivot]+quicksort(greater)
	return res

quicksort((7,8,3,0,-1,2,4))
```
# 1.2.5 Scripting

A script can be executed interactively inside the Ipython interpreter. The variables will become visible.

```{python message}
%run message.py

message
```
__sys.argv__ can be used to retrieve command-line arguments

```{bash arg}
python argv.py these are arguments
```

Import module ___os___ and list files in the directory with __os.listdir__
```{python import}
ìmport os
os.listdir('.')

## alternative
from os import listdir
listdir('.')
```

Import a module with alias with __import MODULE as ALIAS__
```{python np}
import numpy as np
np.linspace(0, 10, 12)
```

## 1.2.5.3 Creating modules

```{python gcmod}
import gcmod

myseq = 'AATTCGGCTTAGTG'

gcmod.gc_count(myseq)

gcmod.gc_perc(myseq)
```

Several techniques for introspection

```{python introspection}
gcmod?

who ## show variables in the environment (like ls() in R)
whos ## with details

dir(gcmod) ## list members of a module

## import objects from modules into the main namespace
from gcmod import gc_count, gc_perc

whos

## to reload a module in python3, use
from importlib import reload
reload(gcmod)
```

With a simple trick of __name__, one can use a module both by importing and by executing

```{python rungcmod}
%run gcmod
```

List of directories searched by python can be obtained by __sys.path__, which can be specified by the environment variable __PYTHONPATH__
```{python syspath}
import sys

sys.path
```

## 1.2.5.6 Packages

A directory that contains many modules is called a __package__.

Usse PACKAGE.__file__ to find where the init file is.

# 1.2.6 Input and output

```{python stringio}
f = open('test-outfile', 'w')
type(f)

f.write("Hello world\na new line")
f.close()

with open('test-outfile', 'a') as f:
	f.write("\nYet another line")

## notice that f2 is automatically closed
with open('test-outfile', 'r') as f2:
	s = f2.read()
	print(s)
```

Use 'r+' to do read and write.
