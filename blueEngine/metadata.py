"""
files to associate common filetypes with their respective extensions 
"""

import pathlib
import hashlib

ass = {
    # Commonly used filetypes
    "lua":  "lua source file",
    "dll": "dynamically linkable library files",
    "shader": "shader file",
    "png" : "portable network graphics",
    "jpg": "Joint Photographic Experts Group",
    "jpeg": "Joint Photographic Experts Group",
    "txt": "text file",
    "svg": "scaleable network graphics",
    "obj": "wireframe object file",
    "mtl": "wireframe material file",
    "zip": "zip archive file",
    
    # Engine specific filetypes
    "prefab": "prefabricated asset",
    "scene": "scene asset",
    "asg": "blue engine assets group asset",
    "compute": "compute shader file",
}                   # 100% short for associations ;)

"""
Metadata Format : JSON
"""
def write_metadata(filepath):
    meta_data = {
        "name":filepath,
    }
    
    try:
        with open(filepath, "r+") as file:
            if filepath.split('.')[-1] in ass:
                write_metadata["file_hash"] = str(hashlib.md5(bin(file.read())).hexdigest)
    except Exception as err:
        print(err)