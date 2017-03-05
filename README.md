# ukkonen
Ukkonen's suffix tree construction in python which takes $$ O(n) $$ time for constant-sized alphabets.

## Functions
***
This module features basic functionalities of suffix tree. Assume that we initially constructed a suffix tree with string *mississippi*.

```python
st = SuffixTree('mississippi')
```

### SuffixTree.substring(*string*)

Check if a string *string* is a substring of the given string in $$ O(m) $$ time, where m is the length of *string*.

```python
st.substring('issi')

>>> True

st.substring('sipi')

>>> False
```
