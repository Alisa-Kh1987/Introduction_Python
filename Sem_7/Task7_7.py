# ЗАДАЧА С СЕМИНАРА (в рамках ДЗ)

# ✔Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. 
# ✔Каждая группа включает файлы с несколькими расширениями. 
# ✔В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import shutil


def sort_files(files_folder, video, images, text_docums, music_docs):
    video = ['.mov', '.mp4', '.avi']
    images = ['.jpg', '.jpeg', '.bmp', '.png']
    text_docums = ['.txt', '.doc', '.docx']
    music_docs = ['.mp3', '.wav', '.ogg']
       
    for file in os.listdir(files_folder):
        _, fileextension = os.path.splitext(file)
    
# закончить не успела. Буду дописывать после 11 семинара.    
    





    

    

