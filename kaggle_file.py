import kaggle

# Authenticate using Kaggle API credentials
kaggle.api.authenticate()

print(kaggle.api.dataset_list_files('ahmedaliraja/attendance-sheet-data-set-for-university').files)

# Download the dataset
kaggle.api.dataset_download_files('ahmedaliraja/attendance-sheet-data-set-for-university', path='./data', unzip=True)

kaggle.api.dataset_metadata('ahmedaliraja/attendance-sheet-data-set-for-university',path='.')

datasets= kaggle.api.dataset_list(search='Attendance')
print(datasets)