import os
from PIL import Image

# Directories
images_dir = r"data\dataset_figaro1k\training\images"
masks_dir = r"data\dataset_figaro1k\training\masks"

# Get list of files
image_files = sorted(os.listdir(images_dir))
mask_files = sorted(os.listdir(masks_dir))

# Check if the number of images and masks is the same
if len(image_files) != len(mask_files):
    print("Mismatch in the number of images and masks. Check your dataset.")
else:
    # Rename and convert mask files to match image file names and format
    for image_file, mask_file in zip(image_files, mask_files):
        image_name, image_ext = os.path.splitext(image_file)
        mask_path = os.path.join(masks_dir, mask_file)

        # Map JPG extension to JPEG format
        image_format = image_ext[1:].upper()
        if image_format == "JPG":
            image_format = "JPEG"

        # Load mask and convert it to the image format
        mask = Image.open(mask_path)
        new_mask_name = f"{image_name}{image_ext}"
        new_mask_path = os.path.join(masks_dir, new_mask_name)

        # Save mask in the same format as the image
        mask.convert("RGB").save(new_mask_path, format=image_format)  # Format derived from extension
        print(f"Converted and renamed: {mask_file} -> {new_mask_name}")

        # Optionally, remove the original mask file after conversion
        os.remove(mask_path)

    print("All mask files renamed and converted successfully!")
