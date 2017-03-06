# ukkonen
Ukkonen's suffix tree construction in python which takes O(n) time for constant-sized alphabets.

## Functions

This module features basic functionalities of suffix tree. Assume that we initially constructed a suffix tree with string *mississippi*.

```python
st = SuffixTree('mississippi')
```

### SuffixTree.substring(*pattern*)

Checks if a string *pattern* is a substring of the given string in O(m) time, where m is the length of *string*.

```python
st.substring('issi')

>>> True

st.substring('pipi')

>>> False
```

### SuffixTree.search(*pattern*)

Finds all occurences of *pattern*. A list of indices from which *pattern* starts in  the given string is returned. If *pattern* is not a substring of the given string, empty list is returned.

```python
st.search('issi')

>>> [1, 4]

st.search('pipi')

>>> []
```