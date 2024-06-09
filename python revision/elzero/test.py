# import os
# from PIL import Image
# import csv
# import my_numpy as np
# a = {1, 2, 3}
# b = {4, 5, 6}
#
# a.update(b)
# c = a.union(b)
# print(a)
# print(c)
#
#
#
# # Example file path
# file_path = '/path/to/your/file.jpg'
#
# # Get the extension of the file
# file_extension = os.path.splitext(file_path)
#
# print("Extension of the file:", file_extension)
#
#
# f = ["jpeg", "jpg"]
# g = ["jpeg", "png", "jpeg", "jpg"]
#
# for ext in g:
#   if ext not in f:
#     pass
#   print(ext)
#
# # nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# #
# # for num in nums:
# #   # tane4 (ignore) ely maktoob fy el condtion delwa2ty
# #   if num == 17:
# #     continue
# #   print(num)
#
#
# img_path = r"Z:\UNI\study\python for AI\test\fork1.jpeg"
# img = Image.open(img_path)
# # print(list(img.getdata()))
# # print(os.path.splitext(os.path.basename(img_path))[0])
# input_dir = r"Z:\UNI\study\python for AI\test"
# dirs = os.listdir(input_dir)
# files_paths = map(lambda file: os.path.abspath(file), dirs)
# files_paths2 = map(lambda file: os.path.join(input_dir, file), dirs)
# print(list(files_paths))
# print(list(files_paths2))
#
# print('-'*40)
# output_dir = r'Z:\UNI\study\python for AI\test_folder2'
# already_copied_imgs = map(lambda file_name: os.path.splitext(file_name)[0], list(os.listdir(output_dir)))
# print(list(already_copied_imgs))
#
# print('-'*40)
#
#
# current_path = os.getcwd()
# if 'labels.csv' not in list(os.listdir(current_path)):
#   with open('labels.csv', 'a') as labels_file:
#     fields = ["name", "label"]
#     csv_writer = csv.DictWriter(labels_file, fields, delimiter=";")
#     csv_writer.writeheader()
#
# existing_labels = []
# with open('labels.csv', 'r') as read_labels:
#   csv_reader = csv.reader(read_labels)
#   for label in csv_reader:
#     existing_labels.append(label)
#
# # print(existing_labels)
#
# with open('labels.csv', 'a') as append_labels:
#   csv_writer = csv.writer(append_labels, delimiter=';')
#   existing_labels2 = []
#   for row in existing_labels:
#     if len(row) > 0:
#       existing_labels2.append(row)
#   print(existing_labels2)
#   # csv_writer.writerow(["00001;cat"])
#   # csv_writer.writerow(["00002;cat"])
#   # csv_writer.writerow(["00003;cat"])


# with open('labels.csv', 'a+') as labels_file:
#   csv_writer = csv.writer(labels_file, delimiter=";")
#   csv_reader = csv.DictReader(labels_file)
#   csv_writer.writerow(['000000', 'cat'])
#   print(list(csv_reader))








# img_array = np.array(np.zeros((1, 100, 100)))
#
# print(img_array.shape)


def testerror(ss):

  for i in range(ss):
    if i == 5:
      return "1st condition"

  return -1

my_list = [1,2,3,4,5]

my_list.remove(3)

# for i in range(self._size):
#     if val == current_node.elem:
#         current_node.elem = None
#         is_node_deleted = True
#         if i == 0:
#             current_node.next_node.prev_node = None
#             self._head = current_node.next_node
#             self._size = self._size - 1
#             current_node = current_node.next_node
#         elif i == self._size - 1:
#             current_node.prev_node.next_node = None
#             self._tail = current_node.prev_node
#             self._size = self._size - 1
#             current_node = current_node.next_node
#         else:
#             current_node.next_node.prev_node = current_node.prev_node
#             current_node.prev_node.next_node = current_node.next_node
#             self._size = self._size - 1
#             current_node = current_node.next_node
#     else:
#         current_node = current_node.next_node


# for i in range(self._size):
#     if val == current_node.elem:
#         # reduce the size of the list by 1 because an element will be removed
#         self._size = self._size - 1
#         # Make the current el = None
#         current_node.elem = None
#         if i == self._size: # it is not (self._size - 1) the size is already reduced by one above
#             current_node.prev_node.next_node = None
#             self._tail = current_node.prev_node
#         elif i == 0:
#             current_node.next_node.prev_node = None
#             self._head = current_node.next_node
#         else:
#             # Break the link between the cur node and the next and prev nodes.
#             current_node.prev_node.next_node = current_node.next_node
#             current_node.next_node.prev_node = current_node.prev_node
#         return True
#     else:
#         current_node = current_node.next_node


