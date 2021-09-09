import streamlit as st
import requests
import pandas as pd
from urllib.request import urlopen


class MakeCalls:
    def __init__(self, url: str = "http://localhost:8080/") -> None:
        """
        Constructor for the MakeCalls class. This class is used to perform API calls to the backend service.
        :param url: URL of the server. Default value is set to local host: http://localhost:8080/
        """
        self.url = url
        self.headers = {"Content-Type": "application/json"}

    def app(self):
        st.title('Fallback Reduction')
        predict_endpoint = 'api/v1/fallback_reduction/predict'

        st.write('''NLP Service to reduce the chatbot query fallback.''')  # description and instructions

        uploaded_fall_file = st.file_uploader("Choose the fallback data file", type="xls")
        uploaded_db_file = st.file_uploader("Choose the FAQ database file", type="xlsx")

        # Display the predict button
        if st.button("Predict"):
            if uploaded_fall_file is not None and uploaded_db_file is not None:
                files = {"fall_file": uploaded_fall_file, "db_file": uploaded_db_file}
                print(self.url)
                prediction_response = requests.post(self.url+predict_endpoint, files=files)
                file_path = prediction_response.json()
                with urlopen(file_path.get("url")) as conn:
                    df = pd.read_csv(conn)
                    st.table(df)
                    href = f'<a href="{file_path.get("url")}">Download</a>'
                    st.markdown(href, unsafe_allow_html=True)

