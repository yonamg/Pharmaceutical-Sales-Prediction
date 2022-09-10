import streamlit as st
import os
from PIL import Image
import sys


def image_grid():
    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
    print(PROJECT_PATH)
    image_dir = os.path.join(PROJECT_PATH,'grid_image')
    print(image_dir)

    fName_list = os.listdir(image_dir)

    print(len(os.listdir(image_dir)))
    img_file_num = len(os.listdir(image_dir))


    idx = 0
    

    for _ in range(len(fName_list)-1):
        cols = st.columns(4)
        if idx < len(fName_list):
            cols[0].image(f'./grid_image/{fName_list[idx]}',width=150, caption=fName_list[idx])
            print(os.path.join(image_dir, fName_list[idx]))
            idx += 1
        if idx < len(fName_list):
            cols[1].image(f'./grid_image/{fName_list[idx]}',width=150, caption=fName_list[idx])
            idx += 1
        if idx < len(fName_list):
            cols[2].image(f'./grid_image/{fName_list[idx]}',width=150, caption=fName_list[idx])
            idx += 1
        if idx < len(fName_list):
            cols[3].image(f'./grid_image/{fName_list[idx]}',width=150, caption=fName_list[idx])
            idx += 1
        else:
            break



