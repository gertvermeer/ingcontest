# ingcontest
ING Contest: who writes the best document reading tool

In this contest you are gonna play with opensource OCR tooling. The contest is based
on real project. Due to migration of old archives to a new archive, documents where stored
under wrong contractnumbers. Before putting the documents in the target archive the correct
documentsnumbers must be extracted from the contract using OCR tooling.

Unfortunately all documents were not scanned very accurate, so you need to do some tricks to
retrieve the right contractnumbers. Can you write a DocumentProcessor class that recognises all
the right contractnumbers?

You can test your DocumentProcessor using the testSuite.

Please feel free not to use Tesseract but use your own tools.

Good luck!




To run this programm you need to first:
Windows:
- install the Tesseract software (https://youtu.be/QJkKDsjj1oA) - windows
- create a virtual environment `python3 -m venv env`
- activate the virtual environment `env\Scripts\activate.bat`
- install dependencies `pip install -r Requirements.txt`
- make sure in the DocumentProcessor the path to the Tesseract executable is correct

Mac:
- Make sure python3 is installed (this is the esiest using `brew install python`)
- install the Tesseract software using homebrew: `brew install tesseract` - mac users
- Create a virtual environment `python3 -m venv env`
- Activate the virtual environment `source env/bin/activate`
- install dependencies `pip install -r Requirements.txt`
- If you don't have brew installed in the default prefix, add the following environment variable: `export TESSDATA_PREFIX=$(brew --prefix)/share/tessdata`


Linux
Uitgegaan van Raspbian/VSCode (Debian) 
- sudo apt install tesseract-ocr y
- sudo apt install tesseract-ocr-dut
… make a programming directory
… go there
- git clone https://github.com/gertvermeer/ingcontest.git
… in VSCode
- install Pylance etc.
