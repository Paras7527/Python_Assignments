#Q1: Normalize the 'Math' scores using Min-Max scaling.
import pandas as pd

def main():
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
    
    df = pd.DataFrame(data)

    Max = df['Math'].max()
    print("Max Value : ",Max)

    Min = df['Math'].min()
    print("Min Value : ",Min)

if __name__ == "__main__":
    main()