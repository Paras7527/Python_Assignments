#Q1: Create a DataFrame for student marks and print basic information like shape, columns, and data types.
#data = {
#    'Name': ['Amit', 'Sagar', 'Pooja'],
#    'Math': [85, 90, 78],
#    'Science': [92, 88, 80],
#    'English': [75, 85, 82]}

import pandas as pd

def main():
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)
    print("Dataframe is : ",df)

    print("The shape of the data is :",df.shape)

    print(df['Name'])
    print(df['Math'])
    print(df['Science'])
    print(df['English'])

    print("Columns are : \n",df.columns.to_list())
    print("Data types are : \n",df.dtypes)

if __name__ == "__main__":
    main()