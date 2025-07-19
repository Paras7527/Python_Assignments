#Q9: Create a DataFrame with missing values and fill them with column mean.
#data2 = {
#    'Name': ['Amit', 'Sagar', 'Pooja'],
#    'Math': [np.nan, 76, 88],
#    'Science': [91, np.nan, 85]
#}
import pandas as pd
import numpy as np

def main():
    data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]}

    df = pd.DataFrame(data2)
    print("The Dataframe is : \n",df)

    #data2['Math'] = data2['Math'].fillna(data2['Math'].mean())

    col_mean = df[['Math','Science']].mean()
    print("Column mean : \n",col_mean)

    df_Fill = df.fillna(col_mean)
    print("The Updated Dataframe is : \n",df_Fill)

    print(data2)

if __name__ == "__main__":
    main()