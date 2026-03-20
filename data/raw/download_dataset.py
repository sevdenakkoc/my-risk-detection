from pathlib import Path
import shutil
import kagglehub

# Step 1 — Download dataset to Kaggle cache
dataset_path = Path(kagglehub.dataset_download("anshankul/ibm-amlsim-example-dataset"))

print(f"Downloaded dataset to cache: {dataset_path}")

# Step 2 — Define where we want the data INSIDE our project
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

print(f"Copying files into project folder: {RAW_DATA_PATH}")

# Step 3 — Copy only CSV files into data/raw
for file in dataset_path.glob("*.csv"):
    destination = RAW_DATA_PATH / file.name
    shutil.copy(file, destination)
    print(f"Copied {file.name}")

print("✅ Dataset is now available inside your project.")