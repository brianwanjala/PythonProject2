import os

# Set the target folder
target_folder = r"C:\Users\k\OneDrive\Pictures\Camera Roll"

# Change to the target directory
os.chdir(target_folder)
print(f"Current working directory: {os.getcwd()}")

# Prefix to add to each file
prefix = "new_video_"

# Counter for optional numbering (if needed)
count = 1

for filename in os.listdir():
    # Skip directories
    if os.path.isdir(filename):
        continue

    # Get file extension
    name, ext = os.path.splitext(filename)

    # Create the new name
    new_name = f"{prefix}{count}{ext}"

    # Rename the file
    os.rename(filename, new_name)
    print(f"Renamed: {filename} → {new_name}")

    count += 1

print("✅ All files have been renamed successfully!")
