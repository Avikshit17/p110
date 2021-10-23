import pandas as pd
import plotly.figure_factory as pf
import random
import statistics as st
df=pd.read_csv("medium_data.csv")
rt=df["reading_time"].tolist()
finalList=[]
def sampleData():
    sd=[]
    for i in range(0,100):
        pos=random.randint(0,len(rt)-1)
        data=int(rt[pos])
        sd.append(data)
    mean=st.mean(sd)
    finalList.append(mean)
for i in range(0,1000):
    sampleData()
pstd=st.stdev(rt)
samplestd=st.stdev(finalList)
print(pstd)
print(samplestd)
