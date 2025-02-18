"""
Problem
Given an array dockLayout representing the docking spots in a harbor, 
where 0 indicates an empty spot and 1 indicates an occupied spot, 
and an integer newBoats representing the number of boats attempting to dock, 
determine if it is possible to dock all new boats under the condition that no two boats are adjacent to each other.

Examples
canDockBoats([0,1,0,0,0,1,0], 1)
// returns true
// We can dock one boat
// between the two already docked boats
 
canDockBoats([1,0,0,0,1,0,0], 2)
// returns true
// There's space to dock
// two new boats at the available spots
 
canDockBoats([1,0,1,0,1,0,1], 1)
// returns false
// No suitable space to dock a
// new boat without it being next to another
"""

from typing import List


def canDockBoats(dockLayout: List[int], newBoats: int) -> bool:
    if newBoats <= 0:
        return False

    i = prev_boat = next_boat = 0

    while newBoats > 0 and i < len(dockLayout):
        curr_boat = dockLayout[i]

        if i < len(dockLayout) - 1:
            next_boat = dockLayout[i + 1]
        else:
            next_boat = 0

        if prev_boat == curr_boat == next_boat == 0:
            newBoats -= 1
            curr_boat = 1

        if newBoats == 0:
            return True

        prev_boat = curr_boat
        i += 1

    return False
