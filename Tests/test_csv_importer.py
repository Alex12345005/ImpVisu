import unittest
import tempfile

class TestCSVImporter(unittest.TestCase):
    # create example csv
    def create_temp_csv(self, content):
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        temp_file.write(content)
        temp_file.close()
        return temp_file.name
    # test open/read/write with valid file
    def test_import_csv_valid_file(self):
        content = "Lenzing,170447112,34.75,EUR,Vienna;\nAndritz,170447131,59.41,USD,New York;\nEVN,170447132,28.55,EUR,Vienna;\nEVN,170447133,31.18,USD,New York;"
        temp_file_path = self.create_temp_csv(content)

        with open(temp_file_path, 'r') as temp_file:
            data = [line.strip().split(',') for line in temp_file.readlines()]

        self.assertEqual(len(data), 10000)
    # test open/read/write with empty file
    def test_import_csv_empty_file(self):
        temp_file_path = self.create_temp_csv("")

        with open(temp_file_path, 'r') as temp_file:
            data = [line.strip().split(',') for line in temp_file.readlines()]

        self.assertEqual(len(data), 0)

if __name__ == '__main__':
    unittest.main()
