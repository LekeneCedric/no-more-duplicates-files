import sys
from os import path, system

sys.path.append('models/')
sys.path.append('enums/')
sys.path.append('actions/')

from file_item import file_item
from files_type import file_type
from files_operations import list_dir, load_file, read_root
from extract_duplicates import extract_duplicates
from utils import println, extract_file_name_from_path

ROOT_PATH = '/home/code237/Documents/GitHub/PERSONAL_PROJECTS/no-more-duplicates-files/test_dir'
if __name__ == '__main__':

  files = list_dir(ROOT_PATH)

  root = file_item('root', file_type.DIR, ROOT_PATH,[])

  for file in files:

      file = path.join(ROOT_PATH, file)
      is_dir = path.isdir(file)
      type = file_type.DIR if is_dir else file_type.FILE

      root.add_child(load_file(file))
  read_root(root)
  duplicates = []
  duplicates = extract_duplicates(root)


  for duplicate in duplicates:
    println('----------------------------------------')
    for file in duplicates[duplicate]:
      println(f'[+] {extract_file_name_from_path(file)}')








