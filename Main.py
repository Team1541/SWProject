import configparser
config = configparser.ConfigParser()
config.read('Config.ini')
dir = config['DEFAULT']['TEMP_DIR']

def isTEMPexist(dir):
    import os
    if os.path.isdir(dir + '/TEMP') == False:
        os.mkdir(dir + '/TEMP')

import GUI
gui = GUI.GUI()
isTEMPexist(dir)
gui.setdir(dir)
gui.init_window()




