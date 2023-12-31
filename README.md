# Auction_Web_App

## Standalone Installation

### This is a Web Application used to auction items online

### Prerequisites

1. Linux/Windows OS.
2. Python / Python3 installed.
3. Latest version of `pip` installed.

### Steps

1. Open your bash terminal.
2. Create a virtual environment and activate it
```
python3 -m venv django && django\Scripts\activate
```

4. Clone this repository in any directory of your choice.

```
git clone https://github.com/thelo09/Auction_Web_App.git
```

3. Run the following command to move into the cloned repository.

```
cd Auction_Web_App
```

4. Run the following command to install the requirements

```
pip install -r requirements.txt
```

5. Run the following command to start the Django server

```
python manage.py runserver
```

## Docker Installation

### Prerequisite
1. Docker

### Steps
1. Run the following command

```
docker run rajashekharreddytella/auction_web_app:v1
```

Open localhost:8000 in browser.
