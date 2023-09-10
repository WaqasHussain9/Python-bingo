import math


SAMPLE_INPUT_1 = [
  [
    8, 29, 35, 54, 65,
    13, 24, 44, 48, 67,
    9, 21, 'FREE', 59, 63,
    7, 19, 34, 53, 61,
    1, 20, 33, 46, 72
  ],
  [
    8, 24, 53, 72, 29, 44, 46, 72
  ]
]
SAMPLE_INPUT_2 = [
  [
    8, 29, 35, 54, 65,
    13, 24, 44, 48, 67,
    9, 21, 'FREE', 59, 63,
    7, 19, 34, 53, 61,
    1, 0, 33, 46, 72
  ],
  [
    1, 33, 53, 65, 29, 75
  ]
]


def check_for_bingo(bingo_cards, drawn_numbers):
  '''
  Checks if the card has achieved a win on provided drawn numbers.

  Parameters:
      bingo_cards (list): 25 elements
      drawn_numbers (list): Drawn numbers

  Returns:
      (boolean): True/False depending on achieved win in provided draw
  '''
  pattern = []
  grid_size = int(math.sqrt(len(bingo_cards) + 1))  # grid_size = 5 Here
  # Complexity = 25 x N , N = choices , boxes in bingo = 25
  for index, bingo_card in enumerate(bingo_cards):
    if str(bingo_card) == 'FREE':
      pattern.append(12)
      continue
    if bingo_card in drawn_numbers:
      pattern.append(index)

  # Code for column Bingo
  # Complexity = M , M = no of elements in pattern
  col_match = [0] * grid_size
  row_match = [0] * grid_size
  diagonal_match = [0, 0]
  for entry in pattern:
    col_match[entry % grid_size] += 1
    row_match[entry // grid_size] += 1
    if entry // grid_size == entry % grid_size:
      diagonal_match[0] += 1
    if entry // grid_size == (grid_size - 1) - (entry % grid_size):
      diagonal_match[1] += 1

  # Complexity = N , N = grid_size
  for entry in col_match:
    if entry == grid_size:
      return True

  # Complexity = N , N = grid_size
  for entry in row_match:
    if entry == grid_size:
      return True

  # Complexity = 2
  for entry in diagonal_match:
    if entry == grid_size:
      return True

  return False

if __name__ == '__main__':
  print(check_for_bingo(*SAMPLE_INPUT_1))
  print(check_for_bingo(*SAMPLE_INPUT_2))
