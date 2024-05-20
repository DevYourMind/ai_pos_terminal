from multiprocessing import Process, Manager
from PIL import Image
import numpy as np
import cv2
from pathlib import Path
import os
import pandas as pd
import numpy as np
from time import time

# def foo(D, filenames, i):
#     for filename in filenames:
#         image = Image.open(filename)
#         gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
#         D[filename] = cv2.Laplacian(gray, cv2.CV_64F).var()


# if __name__ == "__main__":
#     path_photos = Path(r'D:\projects\ai_pos_terminal\ai_pos_terminal\data\blurred_data')
#     filenames_images = []
#     for dirpath, dirnames, filenames in os.walk(path_photos):
#         if len(dirnames)==0 and len(filenames):
#             filenames_images.extend([str(Path(dirpath) / x) for x in filenames])
#     filenames_images = filenames_images[:100]
#     start = time()
#     n_proc = 5
#     n_part = len(filenames_images) // n_proc
#     filenames = []
#     with Manager() as manager:
#         D = manager.dict()
#         processes = []
#         for i in range(n_proc):
#             temp_filenames = filenames_images[i*n_part: (i+1)*n_part]
#             filenames.extend(temp_filenames)
#             p = Process(target=foo, args=(D, temp_filenames, i))
#             p.start()
#             processes.append(p)
#         for p in processes:
#             p.join()
#         data = {'filename': val for val in dict(D).keys()}
#         data['fm'] = [val for val in dict(D).values()]
#         pd.DataFrame(data).to_excel('multiproc_data.xlsx')
#     print(len(filenames))   
#     print(time()- start)


from multiprocessing import Pool, Manager
import functools
from itertools import chain

# items = []
items_result = {}
def foo(*filenames):
    dict_fm = {}
    # nums = []
    for filename in filenames:
        image = Image.open(filename)
        gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
        num = cv2.Laplacian(gray, cv2.CV_64F).var()
        # nums.append(cv2.Laplacian(gray, cv2.CV_64F).var())
        dict_fm[filename] = num
    return dict_fm

if __name__ == '__main__':
    path_photos = Path(r'D:\projects\ai_pos_terminal\ai_pos_terminal\data\blurred_data')
    filenames_images = []
    for dirpath, dirnames, filenames in os.walk(path_photos):
        if len(dirnames)==0 and len(filenames):
            filenames_images.extend([str(Path(dirpath) / x) for x in filenames])
    # filenames_images = filenames_images[:100]
    manager = Manager()
    items = manager.list()
    n_proc = 4
    n_part = len(filenames_images) // n_proc
    lists = []
    # lists = [filenames_images[i*n_part: (i+1)*n_part] for i in range(n_proc)]
    for i in range(n_proc):
        temp_filenames = tuple(filenames_images[i*n_part: (i+1)*n_part])
        lists.append(temp_filenames)
    with Pool(n_proc) as p:
        # items += p.starmap(foo, lists)
        items_result = dict(chain.from_iterable(d.items() for d in p.starmap(foo, lists)))
    data = {'filename': [val for val in items_result.keys()], 
            'fm': [val for val in items_result.values()]}
    df = pd.DataFrame(data)
    # print(df.head())
    df.to_excel('dict_multiproc.xlsx')