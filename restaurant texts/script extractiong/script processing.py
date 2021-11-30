from os import listdir
from os.path import isfile, join

from mapscript.preprocessing.extract_texts_info import extract_texts_info
from mapscript.script import Script
from mapscript.visualization.visualizator import Visualizator

texts_dir_path = '/home/yessense/PycharmProjects/map-script-researching/restaurant texts/texts'
texts = [filename for filename in listdir(texts_dir_path) if isfile(join(texts_dir_path, filename))]



# for text_info in
text_info = extract_texts_info(texts)[0]
script = Script(text_info)

vis = Visualizator(script, save_to_file=False, show_buttons=False)

vis.show()
print("Done")
