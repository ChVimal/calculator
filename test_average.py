import average


class TestAverage:
    def test_average(self):
        assert 5 == average.average([4, 5, 6])
