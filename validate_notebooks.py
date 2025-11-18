import nbformat
import os

root_folder = "S:/Employee_Performance_Analysis_Swayam"

for dirpath, _, filenames in os.walk(root_folder):
    for file in filenames:
        if file.endswith(".ipynb"):
            path = os.path.join(dirpath, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    nb = nbformat.read(f, as_version=4)
                nbformat.validate(nb)
                print(f"{path} ✅ Valid")
            except Exception as e:
                print(f"{path} ❌ Invalid: {e}")