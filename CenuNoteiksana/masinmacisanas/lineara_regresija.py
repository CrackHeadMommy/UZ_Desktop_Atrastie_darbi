import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pickle

from termcolor import colored as cl

from sklearn.model_selection import train_test_split

#Modeļi
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import ElasticNet
from sklearn import ensemble #Labāki algoritmi

#Modeļu analīze
from sklearn.metrics import explained_variance_score as evs
from sklearn.metrics import r2_score as r2



def sagatavot_datus(datne, kolonna_x, kolonna_y):
    datu_fails = pd.read_csv(datne)
    datu_fails.dropna(inplace=True)
    X_var = datu_fails[kolonna_x].values
    y_var = datu_fails[kolonna_y].values

    X_train, X_test, y_train, y_test = train_test_split(X_var, y_var, test_size=0.2, random_state=0)
    return (X_train, X_test, y_train, y_test)

def parverst_kolonnu(df, kolonna):
    df[kolonna] = pd.to_numeric(df[kolonna])
    df[kolonna] = df[kolonna].astype('int64')
    return df

def modela_kvalitate(y_test, results):
    print(cl('Dispersija:{}'.format(evs(y_test, results)), 'red', attrs=['bold']))
    print(cl('Kvadrātiskā novirze:{}'.format(r2(y_test, results)), 'red', attrs=['bold']))

def trenet_modeli(modelis, X_train, y_train, X_test):
    modelis.fit(X_train, y_train)
    result = modelis.predict(X_test)
    return modelis, result

def prognozejam_rezultatu(modelis, dati):
    rezultats = modelis.predict(dati)
    return rezultats

datne1 = "masinmacisanas/dati/auto_simple.csv"
kol_x1 = ['Volume', 'Weight']
kol_y1 = ['CO2']

datne2 = "masinmacisanas/dati/auto_imports.csv"
kol_x2 = ['horsepower', 'highway-mpg', 'length']
kol_y2 = ['price']

datne3 = "masinmacisanas/dati/sslv.csv"
kol_x3 = []
kol_y3 = []

#Sagatavot datus
# X_train, X_test, y_train, y_test = sagatavot_datus(datne1, kol_x1, kol_y1)
# X_train, X_test, y_train, y_test = sagatavot_datus(datne2, kol_x2, kol_y2)
X_train, X_test, y_train, y_test = sagatavot_datus(datne3, kol_x3, kol_y3)


#Sagatavot modeli
# modelis = LinearRegression()
# modelis = Ridge()
# modelis = Lasso()
# modelis = BayesianRidge()
# modelis = ElasticNet()

modelis = ensemble.GradientBoostingRegressor()

modelis, rezultats = trenet_modeli(modelis, X_train, y_train, X_test)

modela_kvalitate(y_test, rezultats)

dati1 = ['1600', '1390']
dati1_rez = 108

dati2 = ['111','27','168']
dati2_rez = 13495

dati3 = []
dati3 = 0000

# prognoze = prognozejam_rezultatu(modelis, [dati1])
# prognoze = prognozejam_rezultatu(modelis, [dati2])
prognoze = prognozejam_rezultatu(modelis, [dati3])


# print(prognoze, dati1_rez)
# print(prognoze, dati2_rez)
print(prognoze, dati3_rez)


    





