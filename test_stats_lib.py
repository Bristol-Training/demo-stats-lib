"""
Test suite for the statistics library.

© 2025 Pau Erola, University of Bristol
"""

import pytest
from stats_lib import mean, variance


# Tests for mean function


def test_mean_basic():
    """Test mean with simple numbers."""
    assert mean([1, 2, 3, 4, 5]) == 3.0


def test_mean_floats():
    """Test mean with floating point numbers."""
    assert mean([1.5, 2.5, 3.5]) == 2.5


def test_mean_negative():
    """Test mean with negative numbers."""
    assert mean([-2, -1, 0, 1, 2]) == 0.0


def test_mean_single():
    """Test mean with a single element."""
    assert mean([42]) == 42.0


# Tests for variance function


def test_variance_basic():
    """Test variance calculation."""
    result = variance([1, 2, 3, 4, 5])
    assert result == 2.0


def test_variance_identical():
    """Test variance when all values are the same."""
    assert variance([5, 5, 5, 5]) == 0.0


def test_variance_two_values():
    """Test variance with two values."""
    result = variance([1, 3])
    assert result == 1.0
