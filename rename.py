import os

# rename filename "calibration document" to "input document"

for filename in os.listdir("."):
    if filename.startswith("calibration"):
        os.rename(filename, filename.replace("calibration", "input"))