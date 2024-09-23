import tkinter as tk
import os
import file_organizer as fo


def handle_organize():
    directory = entry.get()
    if os.path.exists(directory):
        fo.organize_files(directory)
        print(f"Organized files in {directory}")
    else:
        print(f"Directory '{directory}' does not exist!")

# Create the main window
root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")  # Set window size

# Label and input for directory
label = tk.Label(root, text="Enter Directory Path:")
label.pack(pady=20)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Button to trigger file organization
button = tk.Button(root, text="Organize Files", command=handle_organize)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
