PseudoCool
==========

PseudoCool - Simple Sudoku Solver

Will most likely only solve puzzles of medium difficulty or below.

As of 2/23/2013, the code fragment can solve (at least some) very easy and easy puzzles. 

Types of inference performed:
  - for some cell, if there's only one possible value, assign value to that cell
  - for some square/row/column, if there exists some value that can only be assigned to one cell, assign that value to cell.


What it can't do (yet), that is needed for higher-level problems:
  - for some n, n > 2, for some r, r is a row/column/square:
    if there are n cells that share n possVals, and have no other poss values --> remove those vals from other cells in r

