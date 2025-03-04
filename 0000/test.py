import sys

from test_cases import TEST_CASES
from solution import max_accordion_length

def run_tests() -> int:
  n = len(TEST_CASES)
  incorrect = []
  for test_input, test_output in TEST_CASES:
    if max_accordion_length(test_input) != test_output:
      incorrect.append((test_input, test_output))
  if not incorrect:
    print(f'All test cases passed! ({n}/{n})')
    return 0
  print(f'Test cases passed: ({n - len(incorrect)}/{n})')
  return 1

if __name__ == '__main__':
  exit_code = run_tests()
  sys.exit(exit_code)
