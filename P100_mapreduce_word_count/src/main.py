import glob
import os.path
import shutil
import string
import time

ACTIVITY_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FOLDER = os.path.join(ACTIVITY_FOLDER, "data")
INPUT_FOLDER = os.path.join(ACTIVITY_FOLDER, "temp", "input")
OUTPUT_FOLDER = os.path.join(ACTIVITY_FOLDER, "temp", "output")
SUBMISSION_FOLDER = os.path.join(ACTIVITY_FOLDER, "submission")



# La carpeta input/ debe existir y estar vacia.
# -----------------------------------------------------------------------------

if os.path.exists(INPUT_FOLDER):
    for file in glob.glob(f"{INPUT_FOLDER}/*"):
        os.remove(file)
else:
    os.makedirs(INPUT_FOLDER)


n = 1000

for file in glob.glob(f"{DATA_FOLDER}/*"):

    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    for i in range(1, n + 1):

        raw_filename_with_extension = os.path.basename(file)

        raw_filename_without_extension = os.path.splitext(raw_filename_with_extension)[
            0
        ]

        new_filename = f"{raw_filename_without_extension}_{i:05d}.txt"

        with open(f"{INPUT_FOLDER}/{new_filename}", "w", encoding="utf-8") as f2:
            f2.write(text)

            # Lectura de los archivos
# -----------------------------------------------------------------------------

start_time = time.time()

sequence = []
files = glob.glob(f"{INPUT_FOLDER}/*")
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            sequence.append((file, line))
                
# Mapper
# -----------------------------------------------------------------------------

pairs_sequence = []
for _, line in sequence:
    line = line.lower()
    line = line.translate(str.maketrans("", "", string.punctuation))
    line = line.replace("\n", "")
    words = line.split()
    pairs_sequence.extend([(word, 1) for word in words])            
            
            