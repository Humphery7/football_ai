# football_ai

# Football Match Predictor ⚽

This project is a machine learning-based web application for predicting the outcome of football matches. It uses data from [FBref](https://fbref.com/en/) and is built with **Streamlit** to create an interactive and user-friendly interface. The model is trained using **GradientBoostingClassifier**, and the app allows users to select home and away teams to predict match outcomes.

## Features

- **Football Match Predictions**: Predicts whether the home team will win, the away team will win, or if the match will end in a draw.
- **Interactive UI**: Built using Streamlit, with a responsive design and smooth team selection.
- **Custom Styling**: The UI features a custom CSS for an enhanced user experience, including gradient backgrounds and a clean layout.

## Data Source

The match data used for training the model was sourced from [FBref](https://fbref.com/en/), which contains a rich set of football statistics for teams and players.

## Installation

### Prerequisites

Before running the app, ensure you have **Python 3.11.7** installed.

### Virtual Environment Setup

Create a virtual environment using Conda:

```bash
conda create -p venv python==3.11.7
```

Activate the environment:

```bash
conda activate ./venv
```

### Installing Dependencies

Install the necessary packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

Alternatively, the main libraries used are:

- **Streamlit**: For creating the web app interface
- **Pandas**: For data manipulation
- **NumPy**: For numerical operations
- **Scikit-learn**: For machine learning models

You can install them individually if needed:

```bash
pip install streamlit pandas numpy scikit-learn
```

## How to Run

To start the app, run the following command:

```bash
streamlit run app.py
```

This will launch the web app in your browser, where you can select home and away teams and predict the match outcome.

## Model Information

The model used for prediction is a **GradientBoostingClassifier**. It has been trained on football data to predict whether the home team wins, the away team wins, or the match ends in a draw. The training data includes historical match statistics and results from various teams in the Premier League.

## Usage

1. **Select Teams**: Choose the home and away teams from the dropdown menus.
2. **Predict Outcome**: Click the **Predict Outcome** button, and the model will predict the match result based on the selected teams.
3. **Results**: The predicted outcome will be displayed below the selection in a user-friendly format (e.g., Home Win, Away Win, or Draw).

## Customization

- **Team List**: The teams available for selection are defined in the `teams_dict` dictionary. You can easily update or modify these teams as needed.
- **Styling**: Custom CSS is used to style the app. If you'd like to change the appearance, modify the CSS code in the Streamlit `st.markdown` block.

## Project Structure

```
football-predictor/
│
├── main.py               # The main Streamlit app file
├── model.pkl            # The pre-trained machine learning model
├── database.csv         # The dataset containing match statistics
├── venv/                # Conda virtual environment
└── requirements.txt     # List of dependencies for the project
```

## Acknowledgments

- Football match data sourced from [FBref](https://fbref.com/en/).
- Built using [Streamlit](https://streamlit.io/), [Pandas](https://pandas.pydata.org/), and [Scikit-learn](https://scikit-learn.org/).

## Future Improvements

- Add more leagues and teams to the predictor.
- Improve the model by incorporating additional features such as player form and injuries.
- Enable real-time match updates and predictions.

---
