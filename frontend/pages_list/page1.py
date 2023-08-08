import streamlit as st

def page1():
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
                # Welcome to FPL Predictor!

                ## Your Ultimate Tool for Winning Your Fantasy League

                Are you ready to dominate your fantasy league? Look no further! Our FPL Predictor uses advanced machine learning algorithms to forecast player performance in the upcoming gameweeks of Premier League. Our model analyzes player statistics, historical data, match fixtures, and more to give you accurate predictions for player points.


                ## Why FPL Predictor?

                - 📊 **Data-Driven**: Our predictions are based on a wealth of data, ensuring accuracy and reliability.
                - 🧠 **Machine Learning Magic**: Our advanced algorithms adapt and learn from past performances to deliver the best predictions.
                - ⏰ **Real-Time Updates**: Get real-time updates on predicted points, injuries, and more to stay ahead of the game.
                - 🏆 **Dominate Your League**: Make strategic decisions and lead your fantasy league with confidence.

                ## Get Started Today!

                Join the ranks of successful fantasy managers who trust FPL Predictor. Whether you're a seasoned manager or a newcomer, our predictions will give you the edge you need to conquer your fantasy league.
            """)
        
    with col2:
        st.image("https://e0.365dm.com/22/08/1600x900/skysports-fantasy-premier-league_5864666.jpg?20220814171817")