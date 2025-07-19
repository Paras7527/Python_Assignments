#Q6: Sort the DataFrame by 'Total' marks in descending order.

import pandas as pd

def main():
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)
    print("The Data frame is : ")
    print(df,"\n")

    df['Total'] = df[['Math','Science','English']].sum(axis=1)
    df_Dsc = df.sort_values(by='Total',ascending=False)
    print("The Updated data frame is : ")
    print(df_Dsc)

if __name__ == "__main__":
    main()