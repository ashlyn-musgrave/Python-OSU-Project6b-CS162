# Author: Ashlyn Musgrave
# GitHub Username: ashlyn-musgrave
# Date: 7/26/2023
# Description: This program takes as its parameter a list of numbers and returns True if
# the elements of the list are strictly decreasing but returns False otherwise
def is_decreasing(numbers):
  """This method defines the base cases in the first two if statements.
   The recursive function is then called to cycle through the list and compare the values in
   decreasing order.
  """
  if len(numbers) <= 1:
    return True

  if numbers[0] <= numbers[1]:
    return False

  return is_decreasing(numbers[1:])

