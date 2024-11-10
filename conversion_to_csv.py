import pandas as pd

# Load the dataset
data = pd.read_csv('E:\MyData\Desktop\Resume Projects\HR-Analytics')  # Adjust path as needed

# Display basic info and statistics
print(data.info())  # Check data types and null values
print(data.describe())  # Summary statistics for numerical columns
print(data.head())  # View first few rows

# Encode Attrition column to binary (1 = Yes, 0 = No)
data['Attrition'] = data['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)

# If you have other categorical columns, use one-hot encoding
data = pd.get_dummies(data, columns=['Gender', 'JobRole', 'MaritalStatus', 'OverTime'], drop_first=True)

# Attrition by Department
attrition_by_department = data.groupby('Department')['Attrition'].mean()
print(attrition_by_department)

# Attrition by Age Group
data['AgeGroup'] = pd.cut(data['Age'], bins=[20, 30, 40, 50, 60], labels=['20-30', '30-40', '40-50', '50-60'])
attrition_by_age = data.groupby('AgeGroup')['Attrition'].mean()
print(attrition_by_age)

# Save cleaned and processed data
data.to_csv('Cleaned_EmployeeAttrition.csv', index=False)
