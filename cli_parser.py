from argparse import ArgumentParser

from hm_17.hm_17_part_2 import Human

parser = ArgumentParser(description="Convertor to JSON and XML")

parser.add_argument("--convertor", default="json")
convertor = parser.parse_args().convertor

human = Human("Leo", "Messi", "male", "1987")

if convertor.lower() == "json":
    print(Human.convert_to_json(human))
elif convertor.lower() == "xml":
    print(Human.convert_to_xml(human))
else:
    print(Human.convert_to_json(human))
