# 1.3.1 The NumPy array object

```{python array}
import numpy as np
a = np.array([0,1,2,3,4.0])
a

## numerical operations are efficient
L = range(1000)
%timeit [i**2 for i in L]

a = np.arange(1000)
%timeit a**2 ## on my machine it's about 300 times faster
```

