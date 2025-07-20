#Q4: Apply One-Hot Encoding to a 'Department' column.
#data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}

import pandas as pd
from sklearn.preprocessing import LabelEncoder
def main():
    data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}

    df = pd.DataFrame(data)

    #df['Department'] = ['HR', 'IT', 'Finance', 'HR', 'IT']         Label Encoding
    #df['Department'] = df['Department'].map({'HR':100, 'IT':200, 'Finance':300})
    #print(df.head())
    
    One_Hot = pd.get_dummies(df['Department'])

    df_encoded = pd.concat([df,One_Hot],axis=1)

    print(df_encoded)
if __name__ == "__main__":
    main()