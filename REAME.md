# Django REST Framework Quickstart

This is a basic Django REST Framework application with a single public endpoint that responds with "Hello, world!".

## Overview
This application is a simple demonstration of Django REST Framework. It includes a single public endpoint (/) that responds with a JSON message: `{"message": "Hello, world!"}`.

## Prerequisites

- Python 3.8 or higher
- `mkvenv` for creating a virtual environment

## Installation

1. Clone the repository:  
`git clone ` 

2. Navigate to the project directory:  
`cd tutorial`

3. Create a virtual environment using [mkvenv](https://pypi.org/project/mkvenv/)  
`mkvenv`  
check documentation, install and figure out to activate the virtual environment to not clutter your local python environment

5. Install the required dependencies:  
`pip install -r requirements.txt`

## Running the Application: 

Ensure you are in the project directory and your virtual environment is activated.

Run the Django server:  
`python manage.py runserver`  

Visit  
[http://127.0.1:8000/](http://127.0.1:8000/)  
in your web browser. You should see a message saying "Hello, world!".


## Contributing
Contributions are welcome. Fork the repo, push to your origin, open a pull request with your changes from the fork into the main repo.

## License
This project is licensed under the terms of the MIT license.