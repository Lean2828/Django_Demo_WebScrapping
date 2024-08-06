@echo off
REM -- Install Script for Demo Web Scraping --

REM -- Clone the Repository
echo Cloning the repository...
git clone https://github.com/Lean2828/Demo_WebScraping.git
cd Demo_WebScraping

REM -- Create Virtual Environment
echo Creating virtual environment...
python -m venv selenium-venv

REM -- Activate Virtual Environment
echo Activating virtual environment...
call selenium-venv\Scripts\activate

REM -- Install Dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM -- Inform the User
echo Installation complete. You can now run the scripts.
echo To activate the virtual environment, use:
echo call selenium-venv\Scripts\activate
