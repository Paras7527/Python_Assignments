#Q8: Plot a histogram of math marks.

import pandas as pd
import numpy as np
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
    
    plt.hist(df['Math'],color='skyblue',)
    plt.title("Histogram for Maths Marks")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()
    

    

if __name__ == "__main__":
    main()