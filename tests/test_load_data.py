```python
"""
AI Apex Vector - Load Data Tests

This module provides unit tests for the load_data function in aiapex_vector/load_data.py.

"""

import unittest
import pandas as pd
from aiapex_vector.load_data import load_data

class LoadDataTestCase(unittest.TestCase):
    def test_load_data(self):
        # Create a temporary CSV file with test data
        test_data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
        test_data.to_csv('test_data.csv', index=False)

        # Load the data using the load_data function
        data = load_data('test_data.csv')

        # Check if the loaded data matches the test data
        self.assertTrue(data.equals(test_data))

        # Clean up the temporary CSV file
        import os
        os.remove('test_data.csv')

if __name__ == '__main__':
    unittest.main()
```
