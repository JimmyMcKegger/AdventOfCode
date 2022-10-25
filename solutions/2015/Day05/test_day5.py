

class TestClass:
    def test_rex_1(self):
        str = "ugknbfddgicrmopn"
        disallowed = ['ab', 'cd', 'pq', 'xy']
        func = lambda a : a not in str
        assert all(map(func, disallowed))

"""     def test_rex_2(self, str):
        x = "this"
        assert "h" in x

    def test_rex_3(self, str):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check") """