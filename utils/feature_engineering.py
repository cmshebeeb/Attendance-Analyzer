import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np

def preprocess_data(input_path, output_path):
    # Load cleaned dataset
    df = pd.read_csv(input_path)
    df['attendance_percentage'] = pd.to_numeric(df['attendance_percentage'], errors='coerce')
    
    # Create new features
    df['present_ratio'] = df['present_days'] / df['total_classes']
    df['absent_ratio'] = df['absent_days'] / df['total_classes']
    bins = [0, 0.5, 0.75, 1.00]
    labels = ['low', 'medium', 'high']
    df['attendance_category'] = pd.cut(df['present_ratio'], bins=bins, labels=labels)
    print(df['attendance_category'].value_counts())
    
    # Scale numerical features
    min_max_scaler = MinMaxScaler()
    standard_scaler = StandardScaler()
    df[['total_classes', 'present_days', 'absent_days']] = min_max_scaler.fit_transform(df[['total_classes', 'present_days', 'absent_days']])
    df[['attendance_percentage']] = standard_scaler.fit_transform(df[['attendance_percentage']])
    
    # Encode categorical variables
    df = pd.get_dummies(df, columns=['attendance_category'])
    
    # Handle missing values
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
    
    # Save feature-engineered dataset
    df.to_csv(output_path, index=False)
    print("Feature-engineered data saved successfully at:", output_path)

if __name__ == "__main__":
    input_path = 'data/AI_cleaned.csv'
    output_path = 'data/feature_engineered_AI.csv'
    preprocess_data(input_path, output_path)
