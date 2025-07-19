#Q7: Create a bar plot of student names vs total marks.

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
    print("The Data frame is : ")
    print(df,"\n")

    df['Total'] = df[['Math','Science','English']].sum(axis=1)

    sns.barplot(x='Name',y='Total',data=df)
    plt.title("Barplot")
    plt.show()

if __name__ == "__main__":
    main()