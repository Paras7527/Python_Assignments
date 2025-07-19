#Q8: Plot a line chart of marks for 'Amit' across all subjects.

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

    amit_data = df[df['Name']=='Amit'][['Math','Science','English']].iloc[0]

    sns.lineplot(x=amit_data.index, y=amit_data.values, marker='o')
    plt.title("Barplot")
    plt.show()

if __name__ == "__main__":
    main()