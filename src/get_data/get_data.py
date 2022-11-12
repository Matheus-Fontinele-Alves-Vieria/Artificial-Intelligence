import pandas as pd

class GetData(object):
    def __init__(self):
        pass
    
    def open_csv(self):
        return pd.read_csv('../data/Air-pollution/death-rates-total-air-pollution.csv')