#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os
import sys
import unittest
import pandas as pd
import pandas.api.types as ptypes
from pandas.api import types

sys.path.append(os.path.abspath(os.path.join('../scripts')))


# In[12]:


from df_clean import DfCleaner 
from df_handle import FileHandler


# In[13]:


class TestDfCleaner(unittest.TestCase):


    def setUp(self) -> pd.DataFrame:
        self.cleaner = DfCleaner()
        self.file_handle = FileHandler()


    def test_convert_to_integer(self):
        df = pd.DataFrame({'col1': ["1", "2"]})
        df = self.cleaner.convert_to_integer(df, ['col1'])
        self.assertTrue(types.is_int64_dtype(df['col1']))


    def test_convert_to_datetime(self):
        df = pd.DataFrame({'col1': ["2018-01-05", "2018-01-06"]})
        df = self.cleaner.convert_to_datetime(df, ['col1'])
        self.assertTrue(type(df['col1'].dtype == ptypes.DatetimeTZDtype))


    def test_read_csv(self):
        df = self.file_handle.read_csv('data/test.csv')
        df2 = pd.read_csv('data/test.csv')
        self.assertEqual(df.shape, df2.shape)


if __name__ == '__main__':
    unittest.main()


# In[ ]:




