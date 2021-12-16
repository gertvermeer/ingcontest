try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

import re
from fuzzywuzzy import fuzz

class DocumentProcessor:

    def retrieveContractNumber(self, filename):
        ocrText = pytesseract \
            .image_to_string(Image.open(filename)) \
            .split('\n')
        _lineWithContractNumber = self.__findLineContractNumber(ocrText)
        _contractNumber = self.__filterContractNumberFromLine(_lineWithContractNumber)
        return _contractNumber

    def __findLineContractNumber(self, stringList):
        print("fineLine")
        regex_statements = "[a-zA-Z]+n*.r*.[0-9]{5,}"
        for line in stringList:
            if re.search(regex_statements, line):
                return line
        return "not found"

    def __filterContractNumberFromLine(self, line):
        regex_statements = "[A-Z]{0,1}[0-9]{5,}"
        match = re.search(regex_statements, line)
        line = match.group()

        line = re.sub("([A-Z][0-9]){1, 1}*.Z*.", "2", line)
        line = re.sub("([A-Z][0-9]){1, 1}*.T*.", "1", line)
        line = re.sub("([A-Z][0-9]){1, 1}*.O*.", "0", line)
        line = line.strip()



        return line
