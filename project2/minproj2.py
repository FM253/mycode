#!/usr/bin/env python3

#using Lilian's code and modfying for use in different file

#importing pandas
import pandas as pd

#creating header list
header_list= ["Issue", "Number", "Arc", "Distributor", "ID", "Contributor"]


df = pd.read_csv('brett_comics.txt', index_col="Contributor")
i = int(input("Please enter as shown either Andy Kubert or Fabian Nicieza: "))
comics_df= df.loc[i]

comics_df.drop(comics_df.columns.difference(header_list), 1, inplace=True)
print(comics_df.head(15))         
