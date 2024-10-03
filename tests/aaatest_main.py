import pytest

from contextlib import nullcontext as does_not_raise
from src.main import Calculator

@pytest.mark.parametrize('x,y,res, expectation',
[
    (1, 2, 0.5, does_not_raise()),
    (3, 2, 1.5, does_not_raise()),
    (4, 2, 2, does_not_raise()),
    (3, '2', 1.5, pytest.raises(TypeError)),
    (5, 0, 5, pytest.raises(ZeroDivisionError)),
    ('3', '2', 1.5, pytest.raises(TypeError)),
    ('3', 2, 1.5, pytest.raises(TypeError)),
    ('a', 2, 1.5, pytest.raises(TypeError)),
    (3, 'a', 1.5, pytest.raises(TypeError)),


])
def test_divide(x, y, res, expectation):
    with expectation:
        assert Calculator().divide(x, y) == res

        

@pytest.mark.parametrize('x,y,res, expectation',
[
    (1, 2, 3, does_not_raise()),
    (4, 5, 9, does_not_raise()),
    ('1', 2, 3, pytest.raises(TypeError)),
    (1, '2', 3, pytest.raises(TypeError)),
    ('1', '2', 3, pytest.raises(TypeError)),
    ('a', 2, 2, pytest.raises(TypeError)),
    (2, 'a', 2, pytest.raises(TypeError)),
    ('a', 'b', 2, pytest.raises(TypeError))



])
def test_add(x, y, res, expectation):
    print('Helloooooooo')
    with expectation:
        assert Calculator().add(x, y) == res



@pytest.mark.parametrize('x,y,res, expectation',
[
    (5, 2, 3, does_not_raise()),
    (9, 2, 7, does_not_raise()),
    ('4', 2, 2, pytest.raises(TypeError)),
    (4, '2', 2, pytest.raises(TypeError)),
    ('4', '2', 2, pytest.raises(TypeError)),
    ('a', 2, 2, pytest.raises(TypeError)),
    (2, 'a', 2, pytest.raises(TypeError)),
    ('a', 'b', 2, pytest.raises(TypeError))

])


def test_subtraction(x, y, res, expectation):
    with expectation:
        assert Calculator().subtraction(x,y) == res


@pytest.mark.parametrize('x,y,res, expectation',
[
    (5, 2, 10, does_not_raise()),
    (8, 3, 24, does_not_raise()),
    (5, 5, 25, does_not_raise()),
    ('3', 3, 9, pytest.raises(TypeError)),
    (3, '3', 9, pytest.raises(TypeError)),
    ('3', '3', 9, pytest.raises(TypeError))

])

def test_multiplication(x, y, res, expectation):
    with expectation:
        assert Calculator().multiplication(x, y) == res