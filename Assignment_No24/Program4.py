#Q4: Plot a pie chart of subject marks for 'Sagar'.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
    df = pd.DataFrame(data)

    Sagar_df = df[df['Name']=='Sagar'][['Math','Science','English']].values.flatten()
    
    plt.pie(Sagar_df,labels=['Math','Science','English'],startangle=90,autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()


    

if __name__ == "__main__":
    main()