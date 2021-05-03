   
import sys 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier 


def OpenClick():
    a = 165
    b = 61

    e=float(a)
    f=float(b)
 
    if e>1000 or f>1000:
        new_prediction="Invalid input"
        result.setText(str(new_prediction))
    else: 

        plt.style.use("ggplot")
        iris = pd.read_csv("shirt.csv")
        df= pd.DataFrame(iris)
            #print(df)
        y = df['T Shirt Size'].values
        X = df.drop('T Shirt Size', axis=1).values

        knn = knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(X,y)

        _=knn.predict(X)
            
        X_new=[[e,f]]

        new_prediction = knn.predict(X_new)

        print(new_prediction)
OpenClick()