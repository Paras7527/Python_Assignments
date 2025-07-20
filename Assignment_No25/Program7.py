#Q7: Normalize 'Age' column using Min-Max Scaling.

#data = {'Age': [18, 22, 25, 30, 35]}

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
def main():
    data = {'Age': [18, 22, 25, 30, 35]}

    df = pd.DataFrame(data)

    Scale = MinMaxScaler()
    df['Age'] = Scale.fit_transform(df[['Age']])
    print(df)


if __name__ == "__main__":
    main()