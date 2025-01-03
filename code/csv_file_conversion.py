from csv import reader
from os import walk
import os
import pygame

def import_csv_layout(path):
    layout_map = []
    with open(path) as file:
        layout = reader(file, delimiter= ",")
        for row in layout:
            layout_map.append(list(row))
        return layout_map


def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for img in img_files:
            img_path = path + "/" + img
            img_surf = pygame.image.load(img_path).convert_alpha()
            surface_list.append(img_surf)

    return surface_list
