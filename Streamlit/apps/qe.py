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
        st.title('Query Expansion')
        predict_endpoint = 'api/v1/query_expansion/predict'

        st.write('''NLP Service to increase the query answer set by generating variations of the query.''')  # description and instructions

        uploaded_file = st.file_uploader("Choose the input file", type="xls")

        # Display the predict button
        if st.button("Predict"):
            if uploaded_file is not None:
                files = {"file": uploaded_file}
                prediction_response = requests.post(self.url+predict_endpoint, files=files)
                file_path = prediction_response.json()
                with urlopen(file_path.get("url")) as conn:
                    df = pd.read_csv(conn)
                    st.table(df)
                    href = f'<a href="{file_path.get("url")}">Download</a>'
                    st.markdown(href, unsafe_allow_html=True)

