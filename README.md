# Calculator Appium Automation Suite (Python)

This project is an automation suite created in Python for the Calculator Application. It includes automated tests using the Pytest framework and Appium Python Client to ensure the functionality of the Calculator Application.

## Installation

1. Ensure you have Python installed on your system (version 3.12 or higher).
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Install [Poetry](https://python-poetry.org/docs/#installation) if you haven't already:
5. Install project dependencies using Poetry:

```
poetry install
```

## To run the automated tests and generate an allure report, execute:

```
poetry run pytest
```

Allure report will be generated automatically inside allure-results folder.

## To serve the allure report, execute:

```
allure serve allure-results
```

For this, allure must be installed locally on your system. Refer [this](https://allurereport.org/docs/install/) for installing allure on your system.
