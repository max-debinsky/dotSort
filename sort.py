import os

path = input("Specify the directory(leave blank for current): ")
if path == "":
    path = "./"

dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")

filesToSort = [".pdf", ".docx", ".jfif", ".png", ".doc", ".zip", ".jpg", "jpeg", ".pptx", ".xlsx"]
createMisc = True

for fileType in filesToSort:
    folderPath = f"{path}/" + fileType.replace(".", "")
    if not os.path.exists(folderPath):
        print(f"Creating folder: {fileType}")
        os.makedirs(folderPath)

    for file in dir_list:
        if file.endswith(fileType):
            os.replace(f"{path}/{file}", f"{folderPath}/{file}")
            print(f"Moving {file}")