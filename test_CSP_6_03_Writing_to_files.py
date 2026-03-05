import CSP_6_03_Writing_to_files as HW

def test_write_file():
    assert HW.writeFile(["apple", 197, True, "hello"], "CSP_6_03_writeFile.txt") == 'apple\n197\nTrue\nhello\n'


def test_sort_names():
    assert HW.sortNames("CSP_6_03_names.txt","CSP_6_03_namesNew.txt") == '0\n12\n347\n856\nNate\nXavier\nmax\n'


def test_high_score():
    assert HW.highScore(10) == 88
