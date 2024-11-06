import os
import shutil
from tkinter import Tk, Button, filedialog, messagebox
def organize_files(directory):
    max_files_per_folder = 240
    file_dict = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_ext = os.path.splitext(filename)[1][1:]
            if file_ext not in file_dict:
                file_dict[file_ext] = []
            file_dict[file_ext].append(filename)
    for file_type, files in file_dict.items():
        folder_path = os.path.join(directory, file_type)
        os.makedirs(folder_path, exist_ok = True)
        subfolder_count = 0
        file_count = 0
        subfolder_path = os.path.join(folder_path, f'subfolder_{subfolder_count}')
        os.makedirs(subfolder_path, exist_ok = True)
        for file in files:
            if file_count == max_files_per_folder:
                subfolder_count += 1
                subfolder_path = os.path.join(folder_path, f'subfolder_{subfolder_count}')
                os.makedirs(subfolder_path, exist_ok = True)
                file_count = 0
            shutil.move(os.path.join(directory, file), os.path.join(subfolder_path, file))
            file_count += 1
def select_directory():
    global selected_dir
    selected_dir = filedialog.askdirectory()
    if selected_dir:
        print(f"Selected Directory: {selected_dir}")
def organize_button():
    if selected_dir:
        organize_files(selected_dir)
        messagebox.showinfo("Success", "Operation Successfully Completed")
    else:
        messagebox.showwarning("Error", "Please Select a Directory First")
root = Tk()
root.title("File Sorter")
root.geometry("600x400")
selected_dir = None
select_button = Button(root, text = "Select Directory", command = select_directory)
select_button.pack(pady = 20)
organize_button = Button(root, text = "Organize", command = organize_button)
organize_button.pack(pady = 20)
root.mainloop()