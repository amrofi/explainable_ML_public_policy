import numpy as np
import pandas as pd
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from restapi.models import MlModel

#preparing training and testing data
def preparedata(df):
    y, X = dmatrices('G3_class ~ C(school) + age + C(sex) + C(address) + \
                  C(famsize) + C(Pstatus) + C(Medu ) + C(Fedu)+ C(Fjob)+C(traveltime)+C(studytime)+failures+\
                  C(schoolsup)+ C(famsup)+C(reason)+C(guardian)+C(paid)+C(activities)+C(nursery)+C(higher)+\
                  C(internet)+C(romantic)+C(famrel)+C(freetime)+C(goout)+C(Dalc)+C(Walc)+C(health)+absences',
                  df, return_type="dataframe")
    y = np.ravel(y)
    return y,X

#preparing list of coefficents
def preparelist(coefdata, cols):
    factors = pd.DataFrame(coefdata)  #valiable name changed
    coeflist= []
    for col in cols:
        if col == 'Intercept':
            #coeflist.append(0.366298367)
            activemodel = MlModel.objects.filter(active=True)
            coeflist.append(activemodel[0].intercept)
        else:
            # print(factors)
            # print("factors[factors.name == col]['weight']", factors[factors.name == col]['weight'].values)
            values = factors[factors.name == col]['weight'].values
            if len(values) > 0:
                coeflist.append(values[0])
            # TODO: this is a hack to make it work
            elif col == "C(activities)[T.yes]":
                coeflist.append(0)
            else:
                print("did not find ", col)
    return coeflist
    
#rebuilding model
def logreg(coefdata): 
    df_math = pd.read_csv('df_math_cleaned.csv')
    y, X = preparedata(df_math)
    coeflist = preparelist(coefdata, X.columns)
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=.9, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train) # It would be nice if we didn't have to do this
    model.coef_ = np.array([coeflist])
    return model.score(X_test, y_test) # Average accuracy of cross vaidated logistic regression model
