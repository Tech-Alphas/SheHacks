import pandas as pd

pip install pandas

df=pd.read_csv("books_new.csv")
df.drop("Height",axis=1,inplace=True)
mood=input()
if(mood=='Neutral'):
    df1=df[df['Genre']=='tech']
    df2=df[df['Genre']=='philosophy']
    df3=df[df['SubGenre']=='autobiography']
    df4=df[df['SubGenre']=='misc']
    df5=df1.append([df2,df3,df4])
elif(mood=='Surprise'):
    df5=df[df['Genre']=='science']
elif(mood=='Happy'):
    df1=df[df['SubGenre']=='trivia']
    df2=df[df['SubGenre']=='classic']
    df3=df[df['SubGenre']=='novel']
    df4=df[df['SubGenre']=='comic']
    df5=df1.append([df2,df3,df4])
elif(mood=='Sad'):
    df1=df[df['SubGenre']=='history']
    df2=df[df['SubGenre']=='psychology']
    df5=df1.append(df2)
else:
    print("No books for this mood")
df5
