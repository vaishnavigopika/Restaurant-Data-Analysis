#Task 1: To find the top 3 cuisines and their average percentage
#importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading the dataset and converting it into dataframe
df = pd.read_csv(r"E:\Cognifyz Data Analysis\Dataset\Dataset.csv")

#Selecting the cuisine column and filling the null values with empty string
cuisine=df["Cuisines"].fillna('')

#Function to create the cuisine column into a list
def createlist(cuisine):
  newlist=[]
  for i in cuisine:
    l=i.split(",")
    for j in l:
      j=j.strip()
      newlist.append(j)
  return newlist

#Main function which counts the top 3 cuisines and their average percentage.
def tops(mainlist):
  count={}
  sortedlist=[]
  name=[]
  counts=[]
  for i in mainlist:
    if i in count:
      count[i]+=1
    else:
      count[i]=1
  sortedlist=sorted(count.items(),key=lambda x:x[1],reverse=True)
  top=sortedlist[:3]
  print(top)
  for i in top:
    name.append(i[0])
    counts.append(i[1])
  totalcount = sum(count.values())
  for i in top:
    percentage=(i[1]/totalcount)*100
    print("The average percentage of",i[0],"cuisine is: ",percentage)
  return name,counts

mainlist=createlist(cuisine)
name,counts=tops(mainlist)

#plotting bar graph to show the top3 cuisines
plt.bar(name,counts)
plt.xlabel("Cuisine")
plt.ylabel("Count")
plt.title("Top 3 cuisine")
plt.show()