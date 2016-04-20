# https://pytest.org/latest/getting-started.html
#	Name must be test_****.py

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4
