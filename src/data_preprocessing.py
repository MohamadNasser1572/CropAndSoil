import pandas as pd

def load_data(CropAndSoilFile_path):
    return pd.read_csv(CropAndSoilFile_path)

def clean_data(df):
    return df.dropna()

if __name__ == "__main__":
    df = load_data(r'C:\Users\pc\Documents\Datasets\Crop and Soil\data_core.csv')
    df_clean = clean_data(df)
    df_clean.to_csv(r'C:\Users\pc\Documents\CropAndSoil\notebooks\CropAndSoil.ipynb', index=False)
    print("Data preprocessing completed successfully!")
