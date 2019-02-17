# Sudoku Solver
## What? 
This project implements a sudoku solver.

## Why did you do this?
I got bored on an airplane and I saw a kid struggling to solve a sudoku. Boom! Opportunity to make a cool CS project.

## How?
I explored the concept of recursive backtracking using Python to solve this problem!

## Recursive back... what?
Per Wikipedia, recursion is when a function calls itself in a program, and backtracking is "a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ('backtracks') as soon as it determines that the candidate cannot possibly be completed to a valid solution."
Recursive backtracking is tackling a smaller, self-similar part of a larger problem at a time, trying out most of (or all) possible possibilities for that solution, and backtrack once an inconsistency is found.

## How does that apply to sudoku?
A computer is great at doing dumb, fast tasks. A good way to tackle a sudoku is to start at the first available cell, check the numbers in the same box, column, and line, and then make a guess for what value could be in that cell.
E.g.: let's say the top-left cell is available. Numbers (2,3,6), (2,8,9), and (3,5,7) are on the same line, columns and box, respectively. It is wise to guess that that cell could only be filled with numbers 1 or 4. We then fill the number one and, recursively, advance to the next cell. If we realize that there are no feasible possibilities for the next cell, then we found an inconsistency, and we need to backtrack. We could then guess the number 4 for the first cell and then again, recursively advance to analyzing the next cells.

## Liked it?
Star the repo and suggest updates! 
