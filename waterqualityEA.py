# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:32:08 2020

@author: Elisa Coraggio
"""
import os
import glob
import pandas as pd

#----------information you have to modify-------------
station='SW-50010208'
path =r'C:\Users\Elisa Coraggio\Desktop\Master_Project'

#---------code that you don't need to modify----------
os.makedirs(station, exist_ok=True)

filenames = glob.glob(path + "/*.csv")
dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename))
# Concatenate all data into one DataFrame
    rawdata = pd.concat(dfs, ignore_index=True, sort=True)
rawdata.iloc[:,4].fillna(rawdata.iloc[:,7])
rawdata.drop(rawdata.columns[[0, 1, 2, 7, 9, 10]], axis = 1, inplace = True) #not sure is equal for each file
rawdata.columns=rawdata.columns.str.replace(".", "_",regex=True)
rawdata=rawdata[rawdata.result != 0]

    
location=rawdata[rawdata['sample_samplingPoint_notation'].str.match(station)]
    
grouped = location.groupby(['determinand_definition'])
l_grouped = list(grouped)

for i in range(len(l_grouped)):

    df=l_grouped[i][1]
    parameter=df['determinand_definition'].unique()
    df.to_csv(station + '/' + station + '_' + str(parameter) + '.csv')