# MinHash

A simple but effective pure python implementation of Minhash + Banded LSH. Built for for finding the set of all similar strings in a large corpus in O(N) time. The entire dataset does not ever need to be in memory: the algorithm collects pairs in a single streaming pass. 

Designed for "fuzzy matching" strings to account for misspellings, it could also be used for finding similar documents from a web crawl by splitting strings along word boundaries rather than character boundaries.

Running Test:
```bash
>>> python MinHash.py
```

Usage:
```python
from MinHash import get_similar_docs

docs = ['aaaaab', 'aaaaac', 'xyz']
similar_docs = get_similar_docs(docs)
print similar_docs

> set([('aaaaab', 'aaaaac')])
```

Note that you may need to adjust the default parameters to best match your application.

## References
[Awesome Chapter about MinHash + LSH this algorithm comes from](http://infolab.stanford.edu/~ullman/mmds/ch3.pdf) 
[Awesome blog post about MinHash from a deveopers perspective](http://matthewcasperson.blogspot.com/2013/11/minhash-for-dummies.html)