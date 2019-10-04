"""Validator are functions to validate input values.

Validators should not return anything rather raise an exception
if the inputs do not meet expected conditions.
"""


def int_gt_0(value: int):
    """Integer value greater than zero."""
    if type(value) is not int or value < 1:
        raise ValueError("Value should be integer and greater than 0.")
