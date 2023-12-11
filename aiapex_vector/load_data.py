```python
"""
AI Apex Vector - Load Data

This module provides functions for loading high-dimensional data.

"""

import pandas as pd

def load_data(file_path):
    """
    Load high-dimensional data from a CSV file.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - data (pd.DataFrame): The loaded data as a pandas DataFrame.
    """
    data = pd.read_csv(file_path)
    return data
```
