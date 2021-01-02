import numpy as np
import numpy.random as random
import pandas as pd
import scipy as sp
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
hier_df = DataFrame(
    np.arange(9).reshape(3, 3),
    index=[
        ['a', 'a', 'b'],
        [1, 2, 2]
    ],
    columns=[
        ['Osaka', 'Tokyo', 'Osaka'],
        ['Blue', 'Red', 'Red']
    ]
)

# Name indices
hier_df.index.names = ['key1', 'key2']
# Name columns
hier_df.columns.names = ['city', 'color']
# print(hier_df)

# Sum by level
# print(hier_df.sum(level='key1', axis=0))
# print(hier_df.sum(level='color', axis=1))
# print(hier_df.drop(['b']))

# Practice 6-1
hier_df1 = DataFrame(
    np.arange(12).reshape(3, 4),
    index=[
        ['c', 'd', 'd'],
        [1, 2, 1]
    ],
    columns=[
        ['Kyoto', 'Nagoya', 'Hokkaido', 'Kyoto'],
        ['Yellow', 'Yellow', 'Red', 'Blue']
    ]
)
hier_df1.index.names = ['key1', 'key2']
hier_df1.columns.names = ['city', 'color']
print(hier_df1)
# Get average by city
hier_df1_2 = hier_df1.mean(level='city', axis=1)

# Get average only by city
hier_df1_3 = hier_df1_2.mean(level=None)
print(hier_df1_3)
print('something else')