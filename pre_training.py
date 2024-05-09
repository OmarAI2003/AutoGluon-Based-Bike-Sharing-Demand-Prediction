import pandas as pd
from fetch_data import fetch_data

def preprocess_data():
    # Fetching data using the fetch_data function
    train, test, submission = fetch_data()

    # Converting the 'datetime' column to datetime format in the training dataset
    train['datetime'] = pd.to_datetime(train['datetime'])

    # Extracting hour, day, month, and year from the 'datetime' column and creating new columns for them in the training dataset
    train[['hour', 'day', 'month', 'year']] = train['datetime'].apply(lambda x: pd.Series([x.hour, x.day, x.month, x.year]))

    # Converting the 'datetime' column to datetime format in the test dataset
    test['datetime'] = pd.to_datetime(test['datetime'])

    # Extracting hour, day, month, and year from the 'datetime' column and creating new columns for them in the test dataset
    test[['hour', 'day', 'month', 'year']] = test['datetime'].apply(lambda x: pd.Series([x.hour, x.day, x.month, x.year]))

    # Converting 'season' and 'weather' columns to categorical data type in both training and test datasets
    train["season"] = train['season'].astype('category')
    train["weather"] = train["weather"].astype('category')
    test["season"] = test['season'].astype('category')
    test["weather"] = test["weather"].astype('category')

    # Dropping 'casual' and 'registered' columns from the training dataset since they aren't present in the test set
    train = train.drop(['casual','registered'],axis=1)

    return train, test, submission

# Example of using the function to get the datasets




