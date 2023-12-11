"""
AI Apex Vector - t-SNE Dimensionality Reduction

This module provides functions for performing dimensionality reduction using t-SNE (t-Distributed Stochastic Neighbor Embedding).

"""

from sklearn.manifold import TSNE

def tsne_dimensionality_reduction(data):
    """
    Perform dimensionality reduction using t-SNE.

    Parameters:
    - data (pd.DataFrame): The high-dimensional data as a pandas DataFrame.

    Returns:
    - reduced_data (pd.DataFrame): The reduced data as a pandas DataFrame.
    """
    tsne = TSNE(n_components=2)
    reduced_data = tsne.fit_transform(data)
    return reduced_data
"""
