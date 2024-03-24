import pandas as pd
import numpy as np
import scipy.stats

def feedbackmeal(breakfastlst):
    
    #instead of path add your code to import from sql
    dfb=pd.read_csv('/media/lonewolf/DEN/Practise-Flask/Test4/Project_be_25_6/myproject/data/Breakfast.csv')  
    # dfb=pd.read_csv('Breakfast.csv')  
    dfl=pd.read_csv('/media/lonewolf/DEN/Practise-Flask/Test4/Project_be_25_6/myproject/data/LunchDinner.csv')
    # dfl=pd.read_csv('LunchDinner.csv')
    
    dfb.drop(columns=['Keywords', 'soup'], inplace=True)
    dfl.drop(columns=['Keywords', 'soup'], inplace=True)
    
    dfm = dfb2.loc[dfb2['ID'] == breakfastlst[0]]
    
    for i in range(1,len(breakfastlst)):
        dfm = dfm.append(dfl2.loc[dfl2['ID'] == breakfastlst[i]])
    lstDoc = dfm.to_dict('records')
    return lstDoc
#     return breakfastlst