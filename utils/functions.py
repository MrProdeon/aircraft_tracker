from src.APIAdapter import Plane

def get_object_list(planes_information : dict):
    """
    Функция для преобразования сырых данных о самолетах в объекты самолетов Planes.
    :param planes_information: Словарь, который мы получаем из метода get_aeroplanes в классе APIAdapter.
    В нем содержится информацию о каждом самолете в воздушном пространстве страны.
    :return: список с объектами самолетов, экземпляры класса Plane
    """
    object_list = []
    for plane in planes_information["states"]:
        object_ = Plane(plane[2], plane[1], plane[9], plane[13])
        object_list.append(object_)

    return object_list