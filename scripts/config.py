#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path


class Config:
  RANDOM_SEED = 27
  ASSETS_PATH = Path("../")
  REPO = "https://github.com/yonamg/Pharmaceutical-Sales-Prediction"
  STORE_PATH = ASSETS_PATH / "data/store.csv"
  TRAIN_PATH = ASSETS_PATH / "data/train.csv"
  TEST_PATH = ASSETS_PATH / "data/test.csv"
  DATASET_PATH = ASSETS_PATH / "data"
  FEATURES_PATH = ASSETS_PATH / "features"
  MODELS_PATH = ASSETS_PATH / "model"
  METRICS_FILE_PATH = ASSETS_PATH / "metrics"
  IMAGE_PATH = ASSETS_PATH / "img"


# In[ ]:




