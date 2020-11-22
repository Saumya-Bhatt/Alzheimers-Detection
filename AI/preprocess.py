import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler 


def clean(filename):
    df=pd.read_csv(filename)

    df = df.loc[df['Visit']==1] # consider only patients with 1 visit. 
    
    df['M/F'] = df['M/F'].replace(['F','M'], [0,1]) # represent Male as 1 and Female as 0.
    df['Group'] = df['Group'].replace(['Converted'], ['Demented']) # some patients converted to Demented.
    df['Group'] = df['Group'].replace(['Demented', 'Nondemented'], [1,0]) # represent Demented as 1 and Non as 0.

    df=df.dropna(axis=0,how='any') # drop rows with missing SES(socio-economic status) value.
    df = df.drop(['MRI ID', 'Visit', 'Hand'], axis=1) # Drop unnecessary columns
    df = df.reset_index(drop=True)
    return df
    
def split(df):

    Y = df['Group'].values # Logistic target for model
    X = df[['M/F', 'Age', 'EDUC', 'SES', 'MMSE', 'eTIV', 'nWBV', 'ASF']] # Features used for prediction.

    X_train,X_test,Y_train,Y_test = train_test_split(X, Y, random_state=0)

    # feature scaling
    scaler = MinMaxScaler().fit(X_train) # scales values between 0 and 1.
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled  = scaler.transform(X_test)

    return X_train_scaled,X_test_scaled,Y_train,Y_test
    

if __name__=='__main__':
    print(clean('oasis_longitudinal.csv').head())    
