import pytest
from stack_queue_brackets.brackets import validateBrackets

# test valid string 
def test_valid1():
    actual = validateBrackets("()[[Extra Characters]]")
    expected = True
    assert actual == expected 

# test valid string 
def test_valid2():
    actual = validateBrackets("{}(){}")
    expected = True
    assert actual == expected 

# test valid string 
def test_valid3():
    actual = validateBrackets("{}")
    expected = True
    assert actual == expected

# test valid string 
def test_valid4():
    actual = validateBrackets("(){}[[]]")
    expected = True
    assert actual == expected  


# test valid string 
def test_valid5():
    actual = validateBrackets("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected  


# test invalid string 
def test_invalid1():
    actual = validateBrackets("[({}]")
    expected = False
    assert actual == expected 


# test invalid string 
def test_invalid2():
    actual = validateBrackets("(](")
    expected = False
    assert actual == expected 


# test invalid string 
def test_invalid3():
    actual = validateBrackets("{(})")
    expected = False
    assert actual == expected 


# test invalid string 
def test_invalid4():
    actual = validateBrackets("{")
    expected = False
    assert actual == expected 

# test invalid string 
def test_invalid5():
    actual = validateBrackets(")")
    expected = False
    assert actual == expected 


# test invalid string 
def test_invalid6():
    actual = validateBrackets("[}")
    expected = False
    assert actual == expected 


# test invalid string 
def test_invalid6():
    actual = validateBrackets("[}")
    expected = False
    assert actual == expected 

# test pass null string 
def test_nullSting():
    with pytest.raises(Exception):
        validateBrackets()