import requests
import streamlit as st


API_URL = "http://127.0.0.1:5000/predict_model"


st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)


st.title("Titanic Survival Predictor")

st.write(
    "Enter passenger information and the model will predict "
    "whether the passenger would survive."
)

st.divider()


with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:
        pclass = st.selectbox(
            "Passenger Class",
            [1, 2, 3]
        )

        sex = st.selectbox(
            "Sex",
            ["male", "female"]
        )

        age = st.number_input(
            "Age",
            min_value=0.0,
            max_value=100.0,
            value=25.0
        )

    with col2:
        fare = st.number_input(
            "Ticket Fare",
            min_value=0.0,
            value=50.0
        )

        embarked = st.selectbox(
            "Port of Embarkation",
            ["S", "C", "Q"]
        )

        family_size = st.number_input(
            "Family Size",
            min_value=0,
            value=1
        )

    is_alone = st.checkbox("Passenger is travelling alone")

    submitted = st.form_submit_button(
        "Predict Survival",
        use_container_width=True
    )


if submitted:

    data = {
        "Age": age,
        "Fare": fare,
        "Embarked": embarked,
        "Sex": sex,
        "Pclass": pclass,
        "FamilySize": family_size,
        "IsAlone": is_alone
    }

    try:
        response = requests.post(
            API_URL,
            json=data,
            timeout=10
        )

        if response.status_code == 200:

            result = response.json()

            st.divider()

            prediction = result["Prediction"]

            if prediction == "Survived":
                st.success("Prediction: Survived")
            else:
                st.error("Prediction: Not survived")

            st.metric(
                "API predictions made",
                result["request_count"]
            )

        else:
            st.error("API returned an error")
            st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error(
            "Cannot connect to FastAPI. "
            "Make sure the API is running on port 5000."
        )
