import pandas as pd
file_path = (r"C:\Users\Sreenath_Narayana_re\OneDrive - Dell Technologies\Pictures\sree "
             r"DS\datasets-20241023T054639Z-001\apple_stocks.csv")
apple_stocks = pd.read_csv(file_path)
print(apple_stocks.head())
print()


