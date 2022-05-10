from argparse import ArgumentParser
from main import analysFileProperties
from main import PROJECT_PATH
import sys
import os

MAPS_LIST = "mappings"
analyser = ArgumentParser(add_help=False)
analyser.add_argument('--path', action="store")

arguments = analyser.parse_args(sys.argv[1:])

print(arguments)
paths = str(arguments.__getattribute__("paths")).split(",")

build_properties = analysFileProperties(PROJECT_PATH)
if MAPS_LIST not in build_properties.keys():
    pass

mapp_list = build_properties[MAPS_LIST].split(",")
mapp_list = [mappings for mappings in mapp_list if not mappings.strip() == ""]

for path in paths: 
    paths = path.strip()
    for mappings in mapp_list:
        mappings = mappings.strip()
        os.system("java -jar ../BON-2.4.x.jar " +
                  "--inputJar \"" + path + "\" "
                  "--outputJar \"" + path.replace(".jar", "") + "-deobf-" + mappings + ".jar\" " +
                  "--mappingsVer " + mappings
                  )