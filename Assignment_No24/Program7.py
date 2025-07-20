#Q7: Export the final DataFrame to a CSV file

import pandas as pd
import numpy as np

def main():
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
    
    df = pd.DataFrame(data)

    df.to_csv('Dataframe.csv',index=False)
    

    

if __name__ == "__main__":
    main()