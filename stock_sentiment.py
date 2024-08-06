import pandas as pd
df=pd.read_csv('stock_data.csv',encoding="ISO-8859-1")
df.head()
train = df[df['Date'] < '20150101']
test = df[df['Date'] > '20141231']
# Removing punctuations
data=train.iloc[:,2:27]
data.replace("[^a-zA-Z]"," ",regex=True, inplace=True)

# Renaming column names for ease of access
list1= [i for i in range(25)]
new_Index=[str(i) for i in list1]
data.columns= new_Index
data.head(5)