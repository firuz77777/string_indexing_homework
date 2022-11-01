def main(s):
    """
    The s string variable is given. Return three characters from the beginning.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    a = s[0]
    b = s[1]
    c = s[2]
    return a+b+c
print(main("hello"))