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
  * __id__ returns the identity of an object
