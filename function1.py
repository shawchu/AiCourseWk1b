# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 17:13:32 2017

@author: Shaw
"""

from utils import *

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    """
    
    newval = []
    
    for c in grid:
        if c == '.':
            newval.append('123456789')
        else:
            newval.append(c)
    
    if len(grid) == 81:
        sdict = dict(zip(boxes, newval))
        return sdict


def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    
    for key in values:
        if len(values[key])==1:
            dataval = values[key]
            for px in peers[key]:
                values[px] = values[px].replace(dataval, '')
    
    return values


def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
#    print(len(boxes))
#    
#    print(row_units[0])
#    print(column_units[0])
#    print(square_units[0])
#    
#    
#    print(len(unitlist))
#    print(unitlist[9])

#    print(len(units))
#    print(units['A1'])
#    print(peers['A1'])


    for unit in unitlist:
        
        #print(unit)
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            #print(str(digit) + " is at " + str(dplaces))
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
#        break

#    for unit in unitlist:
#        
#        print(unit)
#        for digit in '123456789':
#            dplaces = []
#            for ux in unit:
#                if digit in values[ux]:
#                    dplaces.append(ux)
#            print(str(digit) + " is at " + str(dplaces))
#            if len(dplaces) == 1:
#                values[dplaces[0]] = digit
#                print(digit)
#        #break

    return values
    
#    for key in values:
#        datavals = values[key]
#        #print(key)
#        #print(datavals)
#        for valx in datavals:
#            
#            # use a boolean "anyinothers" to see if number appears in any of its peers
#            anyinothers = False
#            for px in peers[key]:
#                if valx in values[px]:
#                    anyinothers = True
#                    #print(px)
#            if anyinothers == False:
#                values[key] = valx
#            anyinothers = False
                
def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        eliminate(values)
        only_choice(values)
        
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        
        if solved_values_after == len(values):
            return values
            if stalled:
                return values

        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    
    # copied from solution.py
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!

    # create a list of all the boxes with >1 value in box
    #boxes_gt = [box for box in values.keys() if len(values[box]) > 1]
    #print(boxes_gt)

    # syntax from solution.py 
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    print(n)
    print(s)
    
    # syntax from solution.py
    # Now use recurrence to solve each one of the resulting sudokus, and 
#    for value in values[s]:
#        #print(values[s])
#        new_sudoku = values.copy()
#        #print(new_sudoku)
#        new_sudoku[s] = value
#        attempt = search(new_sudoku)
#        #break
#        if attempt:
#            return attempt

unsolved1 = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
grid1 = grid_values(unsolved1)
#eliminate(grid1)
#display(grid1)
#only_choice(grid1)
reduce_puzzle(grid1)
#print("After is....")
#display(grid1)

unsolved2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
grid2 = grid_values(unsolved2)
reduce_puzzle(grid2)

print("Before Search is....")
display(grid2)


search(grid2)
#
#print("After is....")
#display(grid2)



