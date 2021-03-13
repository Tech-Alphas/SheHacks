import pandas as pd
df=pd.read_csv("netflix_titles.csv")
mood=input()
Country=input()
if(mood=="Neutral"):
   df=df[df['country']=='Country'] 
   df1=df[df['listed_in']=='Documentaries']
   df2=df[df['listed_in']=='Drama']
   df3=df1.append(df2)
elif(mood=="Happy"):
   df=df[df['country']=='Country'] 
   df1=df[df['listed_in']=='Comedy']
   df2=df[df['listed_in']=='Romantic']
   df3=df1.append(df2)
elif(mood=="Sad"):
   df=df[df['country']=='Country'] 
   df3=df[df['listed_in']=='Crime shows'] 
elif(mood=="Surprise"):
   df=df[df['country']=='Country'] 
   df1=df[df['listed_in']=='Horror']
   df2=df[df['listed_in']=='Thriller']
   df3=df1.append(df2) 
else:
   df=df[df['country']=='Country'] 
   df3=df[df['listed_in']=='Action']
print(df3.head(10))
