import numpy as np

#Define função para calcular o MAPE
def mape(y_pred,y_true):

    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
