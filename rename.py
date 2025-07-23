import os
from PIL import Image
import re

# === SETTINGS ===
base_dir = "good_data"  # Folder containing class subfolders
output_size = (1024, 1024)

def is_renamed(filename, prefix):
    pattern = re.compile(rf"^{prefix}_\d{{3}}\.(jpg|JPG)$")
    return pattern.match(filename)

def process_images():
    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        if not os.path.isdir(folder_path):
            continue

        # Get list of image files that haven't already been renamed
        image_files = [f for f in os.listdir(folder_path)
                       if f.lower().endswith(('.jpg', '.jpeg', '.png'))
                       and not is_renamed(f, folder_name)]

        image_files.sort()  # Optional: natural sorting for consistency

        # Start from the next available index
        existing = [f for f in os.listdir(folder_path)
                    if is_renamed(f, folder_name)]
        existing_indices = [int(re.search(r"(\d{3})", f).group(1))
                            for f in existing]
        next_idx = max(existing_indices, default=0) + 1

        for img_name in image_files:
            img_path = os.path.join(folder_path, img_name)
            try:
                img = Image.open(img_path)
                img = img.resize(output_size, Image.LANCZOS)

                new_name = f"{folder_name}_{next_idx:03d}.jpg"
                new_path = os.path.join(folder_path, new_name)

                img.save(new_path, "JPEG")
                os.remove(img_path)

                print(f"Processed: {img_name} -> {new_name}")
                next_idx += 1

            except Exception as e:
                print(f"Failed to process {img_path}: {e}")

if __name__ == "__main__":
        for img_name in image_files:
            img_path = os.path.join(folder_path, img_name)
            try:
                img = Image.open(img_path)
                img = img.resize(output_size, Image.LANCZOS)

                new_name = f"{folder_name}_{next_idx:03d}.jpg"
                new_path = os.path.join(folder_path, new_name)

                img.save(new_path, "JPEG")
                os.remove(img_path)

                print(f"Processed: {img_name} -> {new_name}")
                next_idx += 1

            except Exception as e:
                print(f"Failed to process {img_path}: {e}")
