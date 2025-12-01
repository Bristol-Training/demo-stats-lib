"""
A simple library for calculating basic statistics.

© 2025 Pau Erola, University of Bristol
"""

from typing import List, Union


def mean(data: List[Union[int, float]]) -> float:
    """
    Calculate the mean (average) of a list of numbers.
    
    Args:
        data: A list of numbers
        
    Returns:
        The mean as a float
        
    Example:
        >>> mean([1, 2, 3, 4, 5])
        3.0
    """
    # Filter out None values
    data = [x for x in data if x is not None]
    return sum(data) / len(data)


def variance(data: List[Union[int, float]]) -> float:
    """
    Calculate the variance of a list of numbers.
    
    Args:
        data: A list of numbers
        
    Returns:
        The variance as a float
        
    Example:
        >>> variance([1, 2, 3, 4, 5])
        2.0
    """
    data = [x for x in data if x is not None]

    avg = mean(data)
    return sum((x - avg) ** 2 for x in data) / len(data)
