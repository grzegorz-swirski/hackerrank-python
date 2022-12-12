import unittest

if __name__ == '__main__':
    unittest.main()


def convert_to_military(s):
    am_pm = s[-2:]
    time = s[:-2]

    hours = time.split(':')[0]
    minutes = time.split(':')[1]
    seconds = time.split(':')[2]

    if am_pm == 'AM' and hours == '12':
        return f"00:{minutes}:{seconds}"
    elif am_pm == 'PM' and hours != '12':
        return f"{str(int(hours) + 12)}:{minutes}:{seconds}"
    else:
        return time


class TestTimeConversion(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual('00:00:00', convert_to_military('12:00:00AM'))
        self.assertEqual('00:01:00', convert_to_military('12:01:00AM'))
        self.assertEqual('01:00:00', convert_to_military('01:00:00AM'))
        self.assertEqual('11:00:00', convert_to_military('11:00:00AM'))
        self.assertEqual('11:59:00', convert_to_military('11:59:00AM'))
        self.assertEqual('12:00:00', convert_to_military('12:00:00PM'))
        self.assertEqual('12:30:00', convert_to_military('12:30:00PM'))
        self.assertEqual('13:00:00', convert_to_military('01:00:00PM'))
        self.assertEqual('23:00:00', convert_to_military('11:00:00PM'))


