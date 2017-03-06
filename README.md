# ukkonen
Ukkonen's suffix tree construction in python which takes O(n) time for constant-sized alphabets.

## Functions

This module features basic functionalities of suffix tree. Assume that we initially construct a suffix tree with string *mississippi*.

```python
st = SuffixTree('mississippi')
```

### SuffixTree.substring(*pattern*)

Checks if a string *pattern* is a substring of the given string in O(m) time, where m is the length of *pattern*.

```python
st.substring('issi')

>>> True

st.substring('pipi')

>>> False
```

### SuffixTree.search(*pattern*)

Finds all occurences of *pattern*. A list of indices from which *pattern* starts in  the given string is returned. If *pattern* is not a substring of the given string, an empty list is returned.

```python
st.search('issi')

>>> [1, 4]

st.search('pipi')

>>> []
```

### SuffixTree.longest_repeated_substring(*k=2*)

Finds the longest repeated substring among the substrings that appears in the given string at least *k* times. If there exist more than one longest repeated substrings, then it just returns one of them.

```python
st.longest_repeated_substring()

>>> 'issi'

st.longest_repeated_substring(k=3)

>>> 's'
```