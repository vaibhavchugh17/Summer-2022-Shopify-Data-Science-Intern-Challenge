import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.parsers import read_csv

df_orig = pd.read_csv("2019 Winter Data Science Intern Challenge Data Set.csv")
df = df_orig.copy()

#Grouping the df by shop_ids so as to calculate AOV for each shop
grouped = df.groupby("shop_id") 
revenues_by_shop = grouped.sum()["order_amount"]
no_of_orders_by_shop = grouped.count()["user_id"]
aov_by_shop = pd.concat([revenues_by_shop,no_of_orders_by_shop],axis=1).rename(columns={"order_amount" : "Total_amount","user_id" : "Total_#_orders"})
aovs= aov_by_shop["Total_amount"] / aov_by_shop["Total_#_orders"]
aov_by_shop["AOV"] = aovs

#Plotting AOV for each shop
plt.plot([i for i in range(1,101)],aov_by_shop["AOV"])
plt.xlabel("shop_id")
plt.ylabel("AOV")
plt.title("AOV by Shops")
plt.show()

#Sorting by AOV in descending order
print(aov_by_shop.sort_values("AOV",ascending=False))

#Calculating new AOV
new_df = df.drop(df[(df["shop_id"] == 42) | (df["shop_id"] == 78)].index)
new_aov = new_df["order_amount"].sum() / new_df.shape[0]
print(new_aov)

#Calculating median
print(df_orig["order_amount"].median())

