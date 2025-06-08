
def next_higher_with_same_ones(n: int) -> int:
    """
    Returns the next higher integer with the same number of 1s in the binary representation.

    Args:
        n (int): Input integer

    Returns:
        int: Next higher integer with same count of binary 1s
    """
    c = n
    c0 = c1 = 0

    # Count trailing 0s
    while ((c & 1) == 0) and (c != 0):
        c0 += 1
        c >>= 1

    # Count 1s after trailing 0s
    while (c & 1) == 1:
        c1 += 1
        c >>= 1

    # Error case: no larger number with same number of 1s
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    pos = c0 + c1  # Position of rightmost non-trailing 0

    n |= (1 << pos)              # Flip rightmost non-trailing 0
    n &= ~((1 << pos) - 1)       # Clear all bits to the right
    n |= (1 << (c1 - 1)) - 1     # Insert (c1-1) ones on the right

    return n


def run_tests():
    """
    Run sample test cases
    """
    print("=== Bitwise Matching Pattern: Sample Test Cases ===\n")
    test_cases = [
        {"input": 5, "expected": 6},       # 101 -> 110
        {"input": 6, "expected": 9},       # 110 -> 1001
        {"input": 7, "expected": 11},      # 111 -> 1011
        {"input": 1, "expected": 2},       # 1 -> 10
        {"input": 0, "expected": -1},      # No 1s to match
        {"input": 15, "expected": 23},     # 1111 -> 10111
    ]

    for idx, case in enumerate(test_cases, 1):
        result = next_higher_with_same_ones(case["input"])
        print(f"Test Case {idx}: Input = {case['input']}")
        print(f"Binary: {bin(case['input'])} => {bin(result) if result != -1 else 'No match'}")
        print(f"Expected: {case['expected']}, Got: {result}")
        print("Result:", "✅ Passed\n" if result == case["expected"] else "❌ Failed\n")

if __name__ == "__main__":
    run_tests()
