
* type(VAR) tells the type of the variable, such as ___int___, ___str___, __etc__
* Scalar types: __int__, __float__, __complex__, __boolean__

## List
* Slicing list[start:stop:stride]. Therefore, a way to reverse a list would be list[::-1], alternatively use list.reverse(). Using __%timeit__ in ipython, I found out that list.reverse() is about 40% faster than list[::-1]. Note that list[::-1] gives a new object, while list.reverse() reverses in place.
* Sorting with __sorted__ gives a new object, while list.sort() will sort in place

## Strings
* Tripling the quotes with \'\'\' allows the string to span more than one line
* Strings are immutable; to change particular characters, use str.replace()
* Use help(str) to search for new methods

## Dictionaries
