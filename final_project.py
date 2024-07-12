import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_json("https://data.cityofnewyork.us/resource/43nn-pn8j.json")

violation_col = input("Enter the column name for violation description (ex: 'violation_description'): ")
if violation_col not in df.columns:
    print(f"Column '{violation_col}' not found, using default 'violation_description'.")
    violation_col = 'violation_description'

if 'inspection_date' in df.columns:
    df['inspection_date'] = pd.to_datetime(df['inspection_date'])

common_violations = df['violation_description'].value_counts().head(10)
if 'inspection_date' in df.columns:
    df['year'] = df['inspection_date'].dt.year
    trends_over_time = df['year'].value_counts().sort_index()

if 'boro' in df.columns:
    violations_by_borough = df['boro'].value_counts()

print("Most Common Types of Violations:")
print(common_violations)

print("\nNumber of Violations Over Time:")
print(trends_over_time)

print("\nNumber of Violations by Borough:")
print(violations_by_borough)

while True:
    x_column = input("Enter the column name for x-axis(e.g., 'inspection_date', 'year'): ")
    y_column = input("Enter the column name for y-axis(e.g., 'violation_code', 'boro'): ")

    if x_column not in df.columns or y_column not in df.columns:
        print("Invalid columns. Please enter valid column names from the DataFrame.")
        print(f"Available columns: {', '.join(df.columns)}")
    else:
        break


plt.show()
plt.figure(figsize=(10, 6))
plt.scatter(df[x_column], df[y_column], alpha=0.5)
plt.title(f'Scatter Plot of {y_column} vs {x_column}')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.grid(True)

if 'boro' in df.columns:
    plt.figure(figsize=(8, 8))
    plt.pie(violations_by_borough, labels=violations_by_borough.index, autopct='%1.1f%%', startangle=140)
    plt.title('Violations by Borough')
    plt.axis('equal')
    plt.show()

