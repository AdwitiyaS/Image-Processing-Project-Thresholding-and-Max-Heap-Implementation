# -*- coding: utf-8 -*-
"""
Created on Fri May  3 18:45:25 2024

@author: Dell
"""

import os
from PIL import Image
import heapq


image_directory = "D:\images"

def capture_and_store_images(num_images=30):
    images = []
    for i in range(1, num_images + 1):
        # For demonstration, we'll use a placeholder filename
        filename = f"bird_sample{i}.jpg"
        images.append(filename)
    return images


def build_max_heap(images):
    max_heap = []
    for image in images:
        heapq.heappush(max_heap, image)
    return max_heap


def search_image(image_name, heap):
    found = False
    for filename in heap:
        if filename.lower() == image_name.lower():
            print(f"Image '{image_name}' found!")
            found = True
            break
    if not found:
        print(f"Image '{image_name}' not found.")

def display_image(image_name):
    img_path = os.path.join(image_directory, image_name)
    if os.path.exists(img_path):
        img = Image.open(img_path)
        img.show()
    else:
        print(f"Image '{image_name}' not found.")

def main():
    
    images = capture_and_store_images()

    
    max_heap = build_max_heap(images)
    image_to_search = "bird_sample20.jpg"
    
    
    search_image(image_to_search, max_heap)

   
    display_image(image_to_search)

if __name__ == "__main__":
    main()