import torch
import numpy as np
import pandas as pd
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
import matplotlib
import matplotlib.pyplot as plt
import statistics

#matplotlib.interactive(True)

from torch import nn
import torch.optim as optim

import yfinance as yf 

data = pd.DataFrame(yf.download('SFY'))

short_window = 5
medium_window = 20
long_window = 50

data['short_mavg'] = data['Adj Close'].rolling(window=short_window).mean()
data['medium_mavg'] = data['Adj Close'].rolling(window=medium_window).mean()
data['long_mavg'] = data['Adj Close'].rolling(window=long_window).mean()


print(data)