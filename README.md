PseudoCool
==========

PseudoCool - Simple Sudoku Solver

The solver implements simple inferential strategies/heuristics modeled after human strategies for solving sudoku puzzles.

Each strategy is run independently in order of complexity. (higher-order strategies to be added, see list of strategies below.)

Inferences or constraints from one strategy/level are *not* explicitly carried forward/available to the next strategy.
As a result, some of the higher-level reasoning required for more complicated puzzles isn't possible.

The solver outputs a puzzle (finished or otherwise) when it assesses that it can make no more changes.

###############################
Degree of confidence in the solver's ability to complete puzzles of a given level of difficulty:

Very Easy -- 100% Confident
Easy -- 95% Confident
Medium -- 50% Confident
Hard -- 25% Confident
Very Hard -- 0-5% Confident


###############################


Types of inference performed:
  - for some cell, if there's only one possible value, assign value to that cell
  - for some square/row/column, if there exists some value that can only be assigned to one cell, assign that value to cell.


What it can't do (yet), that is needed for higher-level problems:
  - for some n, n > 2, for some r, r is a row/column/square:
    if there are n cells that share n possVals, and have no other poss values --> remove those vals from other cells in r

