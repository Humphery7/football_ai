import os
import pickle
import random
import pathlib
import pandas as pd
import streamlit as st

code_dir = pathlib.Path(__file__).parent.resolve()
files_location = code_dir / ".."/"football_predictions"
files_location = files_location.resolve()

model = pickle.load(open(str(files_location/'model.pkl'), 'rb'))
database = pd.read_csv(str(files_location/ 'database.csv'))


st.set_page_config(page_title="Football Match Predictor", page_icon="⚽", layout="wide")

# Custom CSS to style the app
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to bottom right, #4CAF50, #2196F3);
    }
    .main-card {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 10px;
    }
    .team-selection {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .vs {
        font-size: 2rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Main app layout
st.markdown('<h1 style="text-align: center; color: white;">Football Match Predictor</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    # Team selection
    col1, col2, col3 = st.columns([2, 1, 2])

    teams_dict = {'Arsenal': 0, 'Aston Villa': 1, 'Brentford': 2,
                  'Brighton and Hove Albion': 3, 'Burnley': 4 ,
                  'Chelsea': 5, 'Crystal Palace': 6, 'Everton': 7,
                  'Fulham': 8, 'Leeds United': 9, 'Leicester City': 10,
                  'Liverpool': 11, 'Manchester City': 12,
                  'Manchester United': 13, 'Newcastle United': 14 ,
                  'Norwich City': 15, 'Sheffield United': 16, 'Southampton': 17,
                  'Tottenham Hotspur': 18, 'Watford': 19, 'West Bromwich Albion': 20,
                  'West Ham United': 21, 'Wolverhampton Wanderers': 22 }

    teams = teams_dict.keys()

    with col1:
        st.markdown('<h3 style="text-align: center;">Home Team</h3>', unsafe_allow_html=True)
        home_team = st.selectbox('Select home team', teams, key='home')

    with col2:
        st.markdown('<p class="vs" style="text-align: center;">VS</p>', unsafe_allow_html=True)

    with col3:
        st.markdown('<h3 style="text-align: center;">Away Team</h3>', unsafe_allow_html=True)
        away_team = st.selectbox('Select away team', teams, key='away')

    # Prediction button
    if st.button('Predict Outcome', disabled=(not home_team or not away_team)):
        # This is where you'd call your ML model
        # For now, we'll just set a random prediction
        home_team_code = teams_dict[home_team]
        away_team_code = teams_dict[away_team]

        try:
            prediction = model.predict(database.loc[(database['team'] == home_team_code) & (database['opponent'] == away_team_code), :])
            outcomes = {2: 'Home Win', 1: 'Away Win', 0: 'Draw'}
            st.markdown(f'<h2 style="text-align: center;">Prediction</h2>', unsafe_allow_html=True)
            st.markdown(f'<p style="text-align: center; font-size: 1.5rem;">{outcomes[prediction[0]]}</p>',
                        unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<h2 style="text-align: center;">Prediction</h2>', unsafe_allow_html=True)
            st.markdown(f'<p style="text-align: center; font-size: 1.5rem;">"Match Not Coming up anytime soon"</p>', unsafe_allow_html=True)



    st.markdown('</div>', unsafe_allow_html=True)


# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
