import os
import shutil
import random

source_base = "archive/dataset_test/dataset_test" 
target_dir = "data/Real"
images_per_class = 50


os.makedirs(target_dir, exist_ok=True)

# Loop through each subfolder (i.e., class: asian, scandinavian, etc.)
for class_name in os.listdir(source_base):
    class_path = os.path.join(source_base, class_name)
    
    if not os.path.isdir(class_path):
        continue  # skip non-folder files

    # Get image file names (filter for common image types)
    image_files = [f for f in os.listdir(class_path)
                   if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))]

    # Shuffle and select N images
    selected_images = random.sample(image_files, min(images_per_class, len(image_files)))

    # Copy each selected image
    for i, img_file in enumerate(selected_images):
        src = os.path.join(class_path, img_file)
        dst_filename = f"{class_name}_{i+1}.jpg"  # rename to avoid collisions
        dst = os.path.join(target_dir, dst_filename)
        shutil.copy(src, dst)

    print(f"Copied {len(selected_images)} images from '{class_name}'")

print("Done! All selected images copied to:", target_dir)
