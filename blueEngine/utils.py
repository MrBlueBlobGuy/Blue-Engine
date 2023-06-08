def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

"""
def get_model_data(path:str):
    try:
        with open(path) as file:
            model_data = file.readlines()
            print(model_data)
            return model_data
    except Exception as err:
        print(err)
        return None
    
def parse_model_data(model_data:list[str])->tuple[list]:
    model_vertex_data = []
    model_normal_data = []
    model_texture_data = []
    model_index_data = []

    for i in model_data:
        line_contents = i.split()
        if i.startswith("v "):
            line_contents.pop(line_contents.index('v'))
            vertice_set = tuple(float(vertice) for vertice in line_contents)
            model_vertex_data.append(vertice_set)
        elif i.startswith("vn "):
            line_contents.pop(line_contents.index('vn '))
            normal_set = tuple(float(normal) for normal in line_contents)
            model_normal_data.append(normal_set)
        elif i.startswith("vt "):
            line_contents.pop(line_contents.index('vt '))
            texture_coord_set = tuple(float(tex_coord) for tex_coord in line_contents)
            model_texture_data.append(texture_coord_set)
        else:
            continue

    return (model_vertex_data, model_index_data, model_texture_data, model_normal_data)
"""
