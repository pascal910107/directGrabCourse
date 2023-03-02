# directGrabCourse


## Create virtual environment
python -m venv venv


## Enter virtual environment
### Windows
.\venv\scripts\activate
### Unix or MacOS
source ./venv/bin/activate


## Download plugin
pip install -r requirements.txt


## Download pytesseract
### Windows
go to https://github.com/UB-Mannheim/tesseract/wiki download and execute  
put the path of the file into the path of the environment variable, like C:\Program Files\Tesseract-OCR


## Copy .env file and set the value
cp .env.example .env
