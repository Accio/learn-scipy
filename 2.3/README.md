Debugging
===

# Debug with python debugger

## Postmortem

In IPython, when getting a traceback,

* Use `%debug` to drop into the debugger
* Within debugger (ipdb)
  * list to show where the problem is
  * Run any python code to examine the local environment
  * `quit` to quit the debugger 
* On the command line, pdb can be invoked by `python -m pdb script.py` when running the script file `script.py`.

## Step by step

Used when one believes a bug exists in a module but not sure where

* Start with `%run -d script.py`
* Set break point at line 34 using `b 34`.
* Continue to the next breakpoint with `c(cont(inue))`
* Step into code with `n(ext)` and `s(step)`: `next` jumps to the next statement in the current execution context, and `step` will go across execution contexts, i.e. enable explorting inside function calls
* Use `np.seterr(all='raise')` to turn warnings into errors
* Use `help` to get interactive help
