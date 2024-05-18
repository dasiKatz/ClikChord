import os

train_folder = r'C:\Users\User\Desktop\Project\DataSet\Training'
test_folder = r'C:\Users\User\Desktop\Project\DataSet\Test'
#
# test_chord_folders = test_folder
# for chord_folder in test_chord_folders:
#     print(test_folder)
#     print(chord_folder)
#     for clip_file in os.listdir(os.path.join(test_chord_folders, chord_folder)):
#         print("1")
#         print(clip_file)



def get_directory_names(directory_path):
    return [name for name in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, name))]

test_home = r'C:\Users\User\Desktop\Project\DataSet\Test'
directory_list = get_directory_names(test_home)
print(directory_list)

for directory in directory_list:
    print(directory)
    full_directory_path = os.path.join(test_home, directory)
    print(full_directory_path)
    for filename in os.listdir(full_directory_path):
        print(filename)

