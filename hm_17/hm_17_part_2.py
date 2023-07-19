import json
import xml.etree.ElementTree as ET


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        return json.dumps(self.__dict__)

    def convert_to_xml(self):
        root = ET.Element("human")

        name = ET.SubElement(root, "name")
        name.text = self.name
        age = ET.SubElement(root, "age")
        age.text = self.age
        gender = ET.SubElement(root, "gender")
        gender.text = self.gender
        birth_year = ET.SubElement(root, "birth_year")
        birth_year.text = self.birth_year

        return ET.tostring(root)


human = Human("Leo", "Messi", "male", "1987")
