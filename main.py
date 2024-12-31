import math

def calculate_square_root(number):
  """Calculates the square root of a number.

  Args:
    number: The number to calculate the square root of.

  Returns:
    The square root of the number.
  """
  return math.sqrt(number)

if __name__ == "__main__":
  number = float(input("Enter a number: "))
  square_root = calculate_square_root(number)
  print(f"The square root of {number} is {square_root}")