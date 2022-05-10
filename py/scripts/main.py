import os
import pathlib

SETTINGS_PATH = "../settings.json"
PROJECT_PATH = "../../build.properties"

RELEASE = "releaseKey"
BUILD = "buildVerison"

#WHERE IS CLASS?!

def updateVersion():
    storage = analysFileProperties(SETTINGS_PATH)
    project = analysFileProperties(PROJECT_PATH)

    checkingChanges(storage, project[RELEASE])
    saveProperties(SETTINGS_PATH, storage)


def checkingChanges(storage, new_version):
    if RELEASE not in storage.keys(): 
        storage[RELEASE] = "unknown"
    if BUILD not in storage.keys():
        storage[BUILD] = "0"

    if storage[RELEASE] != new_version: 
        storage[RELEASE] = new_version
        storage[BUILD] = str(1)

def saveProperties(path, properties):
    with open(path, "w") as file:
        for p in properties.items():
            file.write(p[0] + "=" + p[1] + "\n") or file.write(p[0] + ":" + p[1] + "\n")
    pass


def analysFileProperties(path):
    with open(path) as file:
        properties = dict
        lines = file.read().splitlines()

        for line in lines:
            if ":" in line:
                key_value = line.split(":")
                properties[key_value[0]] = key_value[1]

            if "=" in line:
                key_value = line.split("=")
                properties[key_value[0]] = key_value[1]
    return properties
