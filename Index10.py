def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x1 = int(s[0])
    x2 = int(s[1])
    x3 = int(s[2])
    x4 = int(s[3])
    x5 = int(s[4])
    a = x1 + x2 + x3 + x4 + x5
    return a
print(main("23532"))