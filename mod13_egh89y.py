import unittest
from datetime import datetime

def capital(inputTest):
    result = inputTest.isalpha() and inputTest.isupper() and 1 <= len(inputTest) <= 7
    print(f"capital('{inputTest}') result: {result}")
    return result

def chart(inputTest2):
    result = any(char.isdigit() for char in inputTest2) and 1 <= len(inputTest2) <= 2
    print(f"chart('{inputTest2}') result: {result}")
    return result

def timeSeries(inputTest3):
    result = any(char.isdigit() for char in inputTest3) and 1 <= len(inputTest3) <= 4
    print(f"timeSeries('{inputTest3}') result: {result}")
    return result

def startD(inputTest4):
    try:
        result = datetime.strptime(inputTest4, "%Y-%m-%d")
        print(f"startD('{inputTest4}') result: {result}")
        return True
    except ValueError:
        print(f"startD('{inputTest4}') result: False")
        return False

def endD(inputTest5):
    try:
        result = datetime.strptime(inputTest5, "%Y-%m-%d")
        print(f"endD('{inputTest5}') result: {result}")
        return True
    except ValueError:
        print(f"endD('{inputTest5}') result: False")
        return False

class TestSymbol(unittest.TestCase):
    def test_symbol_upper(self):
        assert capital("T")

class TestChart(unittest.TestCase):
    def test_chart_num(self):
        assert chart("1a")

class TestTimeSeries(unittest.TestCase):
    def test_timeSeries_num(self):
        assert timeSeries("1a")

class TestStartD(unittest.TestCase):
    def test_startD_test(self):
        assert startD("1999-05-11")

class TestEndD(unittest.TestCase):
    def test_endD_test(self):
        assert endD("1999-05-11")

if __name__ == "__main__":
    unittest.main()
