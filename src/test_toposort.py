from itertools import permutations
from nose.tools import assert_in, assert_true, raises, assert_list_equal
from toposort import toposorted

def test_simple_case():
    a = []
    b = [a]
    c = [a, b]
    for perm in permutations([a, b, c]):
        result = list(toposorted(perm, lambda x: x))
        assert_list_equal([a, b, c], result)

def test_disjoint_case():
    a = []
    b = [a]
    c = [a]
    d = []
    abcd = [a, b, c, d]
    for perm in permutations(abcd):
        result = list(toposorted(perm, lambda x: x))
        for x in abcd:
            assert_in(x, abcd)
        assert_true(result.index(a) < result.index(b))
        assert_true(result.index(a) < result.index(c))

@raises(ValueError)
def test_cyclical_case():
    a = ('a', [])
    b = ('b', [a])
    a[1].append(b)
    toposorted([a, b], lambda x: x[1])
