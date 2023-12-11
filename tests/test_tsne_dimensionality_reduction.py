"""
AI Apex Vector - t-SNE Dimensionality Reduction Tests

This module provides unit tests for the tsne_dimensionality_reduction function in aiapex_vector/tsne_dimensionality_reduction.py.

"""

import unittest
import pandas as pd
import numpy as np
from aiapex_vector.tsne_dimensionality_reduction import tsne_dimensionality_reduction

class TSNEDimensionalityReductionTestCase(unittest.TestCase):
    def test_tsne_dimensionality_reduction(self):
        # Create a test DataFrame with high-dimensional data
        test_data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]})
        
        # Perform dimensionality reduction using t-SNE
        reduced_data = tsne_dimensionality_reduction(test_data)
        
        # Check if the reduced data has the correct shape
        self.assertEqual(reduced_data.shape, (3, 2))
        
        # Check if the reduced data contains only numerical values
        self.assertTrue(np.issubdtype(reduced_data.dtype, np.number))
        
        # Check if the reduced data is not equal to the original data
        self.assertFalse(reduced_data.equals(test_data))

if __name__ == '__main__':
    unittest.main()
"""
