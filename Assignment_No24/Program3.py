#Q3: Group students by gender and calculate average marks.
import pandas as pd

def main():
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
    df = pd.DataFrame(data)

    df['Gender'] = ['Male','Male','Female']
    df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
    print("Dataframe is :\n",df)

    grouped_data = df.groupby('Gender')[['Math','Science','English']].mean()
    print(grouped_data)

if __name__ == "__main__":
    main()