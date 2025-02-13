# Search Algorithms in array
Simple Python project to analyze the execution time of different search algorithms in a fair and experimental way.


## 📌 Problem Statement

The goal is to compare the efficiency of different search algorithms in arrays by measuring their execution time and analyzing their complexity. The implemented algorithms will be tested on different datasets to evaluate their performance under various conditions.

## 📊 Implemented Search Algorithms

The repository includes implementations for the following search algorithms:

Linear Search (O(n)) - Sequentially searches for the target element.

Search using in Operator (O(n)) - Python’s built-in operator for searching.

Binary Search (O(log n)) - Works on sorted arrays, divides the search range in half.

Ternary Search (O(log₃ n)) - Similar to binary search but splits into three parts.

## Current Coverage

Ensure you have coverage installed (pip install coverage) and run the following commands:
``` coverage run -m unittest discover ```
``` coverage report ```

```
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
Palindrome\__init__.py            0      0   100%
Search\__init__.py                0      0   100%
Search\algorithms.py             32      2    94%   43, 64
Search\constants.py               2      0   100%
Search\data_generator.py          8      0   100%
Test\__init__.py                  0      0   100%
Test\test_algorithm.py           23      1    96%   36
Test\test_data_generator.py      30      1    97%   36
-----------------------------------------------------------
TOTAL                            95      4    96%

```

## 🎨 Code Beautifier

This code is formatted using black:```  https://github.com/psf/black. ```
Run the following command to format the code:

``` black . -l 120 ```

