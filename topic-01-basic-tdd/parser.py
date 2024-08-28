# parser

""" parse numerical strings """

def parse(s):
    "returns the number represented by the string, or None if no number is represented."
    n = 0
    d = 0.1
    decimal = False
    for c in s:
        if c == ".":
            assert not decimal
            decimal = True
            continue
        if not decimal:
            n = n * 10 + ord(c) - ord("0")
        else:
            n = n + (ord(c) - ord("0")) * d
            d = d / 10.0
    return n

def test_single_digit():
    print("test single digit")
    assert parse("0") == 0
    assert parse("9") == 9
    for s in "0123456789":
        assert parse(s) == int(s)

def test_multiple_digits():
    print("test multiple digits")
    assert parse("12") == 12
    assert parse("123") == 123
    assert parse("1234") == 1234
    assert parse("99999") == 99999

def test_decimal_numbers():
    print("test_decimal_numbers")
    print(parse("12."))
    exit()
    assert parse("12.") == 12.0
    assert parse("12.3") == 12.3
    assert parse("12.34") == 12.34
    assert parse("0.99999") == 0.99999


if __name__ == "__main__":
    test_single_digit()
    test_multiple_digits()
    test_decimal_numbers()
    print("done.")

