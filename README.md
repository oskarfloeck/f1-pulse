# f1-pulse

A Flask-powered web application that lets Formula 1 fans predict race outcomes with advanced customizable models.

**Live demo /** [somelink.com.au](somelink.com.au)

## Roadmap

1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

## Overview

The F1 Predictor Web App is a dynamic platform designed for Formula 1 enthusiasts to predict qualification grids and race results.

**What it is** / A web app where registered users can make predictions based on various customizable models.

**Why I made it** / To combine my passion for Formula 1 with practical experience in Flask, Python, and web development technologies while showcasing my skills in predictive modeling and user-centric design.

**Who it is for** / F1 fans, data enthusiasts, and anyone interested in exploring the factors affecting race outcomes.
    
## Features

* **User Authentication:** Register and log in to access prediction tools.
    
* **Prediction Models:** Choose between three models for race predictions:
    
* **Driver-centric:** Focuses on recent and historical driver performance.

* **Conditions-focused:** Emphasizes weather, track conditions, and external factors.

* **Car-based:** Prioritizes car performance and technical specifications.

* **Interactive User Interface:** Smooth user experience with dynamic updates using jQuery.

* **Data Storage:** Predictions and user data stored securely using SQLite and SQLAlchemy.

* **Responsive Design:** Accessible across desktop and mobile devices.

## Technologies Used

    Backend: Flask, Python, SQLAlchemy
    Database: SQLite
    Frontend: HTML, CSS, JavaScript, jQuery
    Other Libraries: (List any other relevant libraries or tools)

## Installation

To run the project locally, follow these steps:

#### 1. Clone the repo
Navigate to where you would like the project and run the following.

	git clone https://github.com/yourusername/f1-pulse.git  
	cd f1-pulse 

#### 2. Set up virtual environment

	python -m venv env  
	source env/bin/activate  # On Windows, use `env\Scripts\activate`  

#### 3. Install dependencies

	pip install -r requirements.txt  

#### 4. Set up the database

	flask db upgrade  # If using Flask-Migrate or equivalent  

#### 5. Run the development server

    flask run  

#### 6. Access the app.

Open your browser and navigate to http://127.0.0.1:5000 (or wherever your flask normally serves your site).

## Usage

    Create an account or log in.
    Navigate to the Predictions page:
        Select your preferred model (Driver, Conditions, or Car).
        Input predictions for qualifying and race results.
    View results and insights:
        Compare your predictions with actual results after races.

## Contributing

Contributions are welcome to improve the app’s functionality and performance. To get started:

    Fork the repository.
    Create a new branch for your feature or bugfix.
    Submit a pull request with a detailed explanation of changes.

Refer to the CONTRIBUTING.md file for additional guidelines.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
Contact

Have questions or feedback? Feel free to reach out:

    Email: your.email@example.com
    GitHub: yourusername
    LinkedIn: (Add your LinkedIn URL)