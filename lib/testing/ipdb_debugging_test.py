import pytest
from ipdb_debugging import plus_two

class TestIpdbDebugging:
    '''Test case for ipdb_debugging.py'''

    def test_adds_two(self):
        '''adds_two() adds 2 to input arg and returns sum.'''
        import ipdb; ipdb.set_trace()  # Debugging point
        result = plus_two(3)
        assert result == 5
