import os

print(os.getcwd())
os.chdir(r"C:\Users\k\OneDrive\Pictures\Camera Roll")
print(os.getcwd())

for i in os.listdir():

    os.rename(i, "new_video" + i)
print("files have been renamed successfully")

