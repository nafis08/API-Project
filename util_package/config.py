import configparser

def getConfig():
    # Read configuration from properties.ini
    config = configparser.ConfigParser()
    config.read('util_package/properties.ini')
    return config