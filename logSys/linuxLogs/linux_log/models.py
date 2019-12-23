from django.db import models

# Create your models here.
class File:
    name: str
    path: str
    text: str
    tp = "file_type"

    def __init__(self, name, path, text):
        self.name = name
        self.path = path
        self.text = text
    
        

class Folder:
    name: str
    path: str
    tp = "folder_type"
 
    def __init__(self, name, path):
        self.name = name
        self.path = path