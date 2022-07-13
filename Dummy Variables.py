# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 08:04:33 2022

@author: Rakesh
"""

##importing package
import pandas as pd

##Loading dataset##

animal = pd.read_csv('D:/DATA SCIENCE ASSIGNMENT/DataSets-Data Pre Processing/DataSets/animal_category.csv')

animal.shape #now shape is 30 , 4
animal.info() ## no null value in data set 
animal.describe() ## to check mean,median,IQR##

##let drops index columns ##
animal.drop(animal.columns[0], axis= 1 , inplace = True)
##creating Dummy variable using dummies ##
##create dunnies in categorical columns##

#Method 1##
df_new= pd.get_dummies(animal)

##method 2##
from sklearn.preprocessing import OneHotEncoder

##Creating instances for onehot encoder##

enc= OneHotEncoder(handle_unknown='ignore')
enc_animal = pd.DataFrame(enc.fit_transform(animal).toarray())

##now dummies has been created for categorical columns#

#method 3##

from sklearn.preprocessing import LabelEncoder

labelencoder = LabelEncoder()

animal.columns
animal['Animals'] = labelencoder.fit_transform(animal['Animals'])
animal['Gender'] = labelencoder.fit_transform(animal['Gender'])
animal['Homly'] = labelencoder.fit_transform(animal['Homly'])
animal['Types'] = labelencoder.fit_transform(animal['Types'])