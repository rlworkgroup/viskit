import unittest

from viskit.misc import ext


class TestExt(unittest.TestCase):
    def test_compact_dict(self):
        foo = {'a': 1, 'b': None, 'c': 3, 'd': None}
        foo_compacted = ext.compact(foo)
        assert 'a' in foo_compacted and 'c' in foo_compacted
        assert 'b' not in foo_compacted and 'd' not in foo_compacted

    def test_compact_list(self):
        foo = ['a', None, 'c', None]
        foo_compacted = ext.compact(foo)
        assert 'a' in foo_compacted and 'c' in foo_compacted
        assert len(foo_compacted) == 2
