def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x1 = s[0]
    x2 = s[1]
    x3 = s[2]
    x4 = s[3]
    x5 = s[4]
    a = f'{x1+x2+x3+x4+x5}'
    return a
print(main("23532"))
