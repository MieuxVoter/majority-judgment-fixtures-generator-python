# majority-judgment-fixtures-generator-python

## Majority Judgment Data testing
A program to generate *.yml files 

### Specification format (example)

```
ballots:
- [0, 3, 2]
- [2, 5, 2]
- [1, 1, 5]
- [5, 3, 5]
max_vote_value: 5
nb_ballot: 4
nb_candidate: 3
ranking: {'1': 2, '2': 0, '3': 1}
tallies:
- [0, 2, 1, 5]
- [3, 5, 1, 3]
- [2, 2, 5, 5]
title: '"Simple usage with 4 ballots and 3 candidates"'

```

### majority_judgment.py
resolving ranking algorithm by PL

### MV_Generate_test.py
generating yml files
radomly votes
main with loop of nb ballots, nb candidates, max vote values
files test_bal<X>_cand<X>_voteval<X>_iter<X>.yml generated in Relesases subfolder --> to be changed for GIT release

### test_algo.py
simply to test majority_judgment