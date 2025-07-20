#Q1: Detect outliers in the 'Salary' column using the IQR method.

#data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]}

import pandas as pd 
import numpy as np

def main():
    data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]}

    df = pd.DataFrame(data)

    Q1 = df['Salary'].quantile(0.25)
    Q3 = df['Salary'].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5*IQR)
    upper_bound = Q3 + (1.5*IQR)

    Outliers = df[(df['Salary']<lower_bound) | (df['Salary']>upper_bound)]

    print("The Detected Outliers are : \n",Outliers)
    


if __name__ == "__main__":
    main()