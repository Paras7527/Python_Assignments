#Q6: Replace multiple values in a column using a dictionary.
#data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}

#Replace as:
#'A+': 'Excellent'  
#'A': 'Very Good'  
#'B+': 'Good'  
#'B': 'Average'  
#'C': 'Poor'

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
def main():
    data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}

    df = pd.DataFrame(data)
    
    df['Grade'] = df['Grade'].replace({'A+': 'Excellent', 'B+': 'Good', 'A': 'Very Good','C': 'Poor','B': 'Average'})
    print(df)


if __name__ == "__main__":
    main()