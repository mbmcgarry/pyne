import numpy as np
from pyne.endf import Library
import nose 
from nose.tools import assert_equal, assert_not_equal, assert_raises, raises, assert_in
import warnings


library = Library('endftest_small.txt')    

def test_mats():
    for mat_id in library.mats:
        assert_in(mat_id, [128, 131, 419])

def test_get():
    result = library.get(419, 4, 2)
    print result
    expected = np.array([4.898421e+3, 6.768123e+0, 0, 1, 0, 0, 2.123124e+6, 8.123142e-6, 2.123212e+6, 8.231231e-6, -2.231211e+6, 8.123421e-6])    
    badkey = library.get(111, 1, 1)
    assert (np.array_equal(result, expected))
    assert_equal(badkey, False)

def test_write():
    # write library to test.txt
    # library.write('test.txt', 'txt')
    result = library.write('test.txt', 'txt')
    # written = Library('test')
    # result = written.get(419, 4, 2)
    # expected = library.get(419, 4, 2)
    expected = 'test.txt'
    assert_equal(result, expected)

if __name__ == "__main__":
    nose.main()