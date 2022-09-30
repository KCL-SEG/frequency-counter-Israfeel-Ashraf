"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    
    frequencies = {}
    
    # Your code goes here
    for item in items:

        x = str(item)

        if frequencies.get(x) == None:
            frequencies[x] = 1

        else:
            frequencies[x] += 1
    
    return frequencies



