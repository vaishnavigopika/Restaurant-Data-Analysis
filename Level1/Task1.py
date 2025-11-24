import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
script_dir = Path(__file__).resolve().parent
df = pd.read_csv(script_dir.parent / 'Dataset' / 'Dataset.csv')

cuisine=df["Cuisines"].fillna('')
print(cuisine)

def createlist(cuisine):
  newlist=[]
  for i in cuisine:
    l=i.split(",")
    for j in l:
      j=j.strip()
      newlist.append(j)
  return newlist

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
plt.bar(name,counts)
plt.xlabel("Cuisine")
plt.ylabel("Count")
plt.title("Top 3 cuisine")
plt.show()