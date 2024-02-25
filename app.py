import numpy as np
import pickle
import streamlit as st

st.set_page_config(page_title='Score Predictor', layout="centered")

filename = 'final_model.pkl'
model = pickle.load(open(filename, 'rb'))

st.markdown("<h1 style='text-align: center; color: white;'> Score Predictor</h1>",
            unsafe_allow_html=True)

st.markdown("<h6 style='text-align: center; color: white;'>ML Model to predict Scores between teams in an ongoing match. Choose teams and provide current overs, runs, wickets to predict the score. </h6>",
            unsafe_allow_html=True)


st.markdown(
    f"""
         <style>
         .stApp {{
             background-image: url("https://t4.ftcdn.net/jpg/05/71/83/47/360_F_571834789_ujYbUnH190iUokdDhZq7GXeTBRgqYVwa.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox(":red[Select the Batting Team]", ('Chennai Super Kings', 'Delhi Capitals', 'Punjab Kings', 'Kolkata Knight Riders',
                                'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad', 'Gujrat Titans', 'Lucknow Super Giants'))
with col2:
    bowling_team = st.selectbox(':red[Select the Bowling Team]', ('Chennai Super Kings', 'Delhi Capitals', 'Punjab Kings', 'Kolkata Knight Riders',
                                'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad', 'Gujrat Titans', 'Lucknow Super Giants'))

if bowling_team == batting_team:
    st.error('Bowling and Batting teams should be different')

overs = st.slider(':red[Current Over]', 0, 20)
overs = int(overs)

col1, col2 = st.columns(2)
with col1:
    totalRunsText = f":red[Enter the Total Runs Scored till {overs} overs] "
    TotalRuns = st.number_input(totalRunsText, min_value=0, max_value=300)
with col2:
    totalWicketsText = f":red[Enter the Total Wickets taken till {overs} overs] "
    TotalWickets = st.number_input(totalWicketsText, min_value=0, max_value=9)

with col1:
    runs_in_prev_5 = st.number_input(
        ':red[Enter the Runs Scored in the last 5 overs]', min_value=0, max_value=TotalRuns)
with col2:
    wickets_in_prev_5 = st.number_input(
        ':red[Enter the Wickets taken in the last 5 overs]', min_value=0, max_value=TotalWickets)


prediction_array = [TotalRuns, TotalWickets,
                    overs, runs_in_prev_5, wickets_in_prev_5]

if batting_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1, 0, 0, 0, 0, 0, 0, 0]
elif batting_team == 'Delhi Capitals':
    prediction_array = prediction_array + [0, 1, 0, 0, 0, 0, 0, 0]
elif batting_team == 'Punjab Kings':
    prediction_array = prediction_array + [0, 0, 1, 0, 0, 0, 0, 0]
elif batting_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0, 0, 0, 1, 0, 0, 0, 0]
elif batting_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0, 0, 0, 0, 1, 0, 0, 0]
elif batting_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0, 0, 0, 0, 0, 1, 0, 0]
elif batting_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 1, 0]
elif batting_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 0, 1]
elif batting_team == 'Gujrat Titans':
    prediction_array = prediction_array + [1, 0, 0, 0, 0, 0, 0, 0]
elif batting_team == 'Lucknow Super Giants':
    prediction_array = prediction_array + [0, 0, 1, 0, 0, 0, 0, 0]
# Bowling Team
if bowling_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1, 0, 0, 0, 0, 0, 0, 0]
elif bowling_team == 'Delhi Capitals':
    prediction_array = prediction_array + [0, 1, 0, 0, 0, 0, 0, 0]
elif bowling_team == 'Punjab Kings':
    prediction_array = prediction_array + [0, 0, 1, 0, 0, 0, 0, 0]
elif bowling_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0, 0, 0, 1, 0, 0, 0, 0]
elif bowling_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0, 0, 0, 0, 1, 0, 0, 0]
elif bowling_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0, 0, 0, 0, 0, 1, 0, 0]
elif bowling_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 1, 0]
elif bowling_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 0, 1]
elif bowling_team == 'Gujrat Titans':
    prediction_array = prediction_array + [1, 0, 0, 0, 0, 0, 0, 0]
elif bowling_team == 'Lucknow Super Giants':
    prediction_array = prediction_array + [0, 0, 1, 0, 0, 0, 0, 0]


prediction_array = np.array([prediction_array])
predict = model.predict(prediction_array)

if st.button('Predict Score', use_container_width=True):
    my_prediction = int(round(predict[0]))
    st.markdown(f"<h6 style='text-align: center; color: white;'>Predicted Match Score is {my_prediction-5} - {my_prediction+5}</h6>",
                unsafe_allow_html=True)
