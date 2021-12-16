import os

try:
    from PIL import Image
except ImportError:
    import Image

from DocumentProcessor import DocumentProcessor


documentProcessor = DocumentProcessor()
INPUT_DIRECTORY = 'inputfiles'

filesToBeScanned = os.listdir(INPUT_DIRECTORY)

for file in filesToBeScanned:
    print("Found in file: ",file, " Contractnummer: "
          , documentProcessor.retrieveContractNumber(INPUT_DIRECTORY + "/"  + file))





