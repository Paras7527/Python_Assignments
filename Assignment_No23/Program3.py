#Q4: Display students who scored more than 85 in Science.

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
    print("The Updated data frame is : ")
    print(df)

if __name__ == "__main__":
    main()