## Student Name: Beckham Gahirwa
## Student ID: 220043782

"""
Public test suite for the meeting slot suggestion exercise.

Students can run these tests locally to check basic correctness of their implementation.
The hidden test suite used for grading contains additional edge cases and will not be
available to students.
"""
from solution import is_allocation_feasible
import pytest


def test_infeasible_when_all_resources_exactly_consumed():
    # New requirement: allocation is invalid if all capacity is used
    resources = {'cpu': 10}
    requests = [{'cpu': 3}, {'cpu': 4}, {'cpu': 3}]
    assert is_allocation_feasible(resources, requests) is False


def test_feasible_when_some_resource_leftover():
    # Feasible if at least one resource has unused capacity
    resources = {'cpu': 10}
    requests = [{'cpu': 4}, {'cpu': 3}]
    assert is_allocation_feasible(resources, requests) is True


def test_multi_resource_feasible_if_one_leftover():
    # One resource fully used, another still has leftover
    resources = {'cpu': 10, 'mem': 20}
    requests = [{'cpu': 10, 'mem': 5}]
    assert is_allocation_feasible(resources, requests) is True


def test_multi_resource_infeasible_if_all_exactly_used():
    # All resources exactly consumed => infeasible
    resources = {'cpu': 10, 'mem': 20}
    requests = [{'cpu': 10, 'mem': 20}]
    assert is_allocation_feasible(resources, requests) is False


def test_zero_capacity_cannot_satisfy_leftover_requirement():
    # Zero capacity means no resource can remain unused
    resources = {'cpu': 0}
    requests = [{'cpu': 0}]
    assert is_allocation_feasible(resources, requests) is False
