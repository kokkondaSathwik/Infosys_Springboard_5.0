import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from textblob import TextBlob
from dotenv import load_dotenv
from streamlit_lottie import st_lottie
import requests
import os

# Load environment variables
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("PASSWORD")
SLACK_TOKEN = os.getenv("SLACK-TOKEN")
SLACK_CHANNEL = os.getenv("SLACK-CHANNEL")

# Initialize Session State
if "preferences" not in st.session_state:
    st.session_state["preferences"] = []
if "recommendation_details" not in st.session_state:
    st.session_state["recommendation_details"] = ""
if "feedback_type" not in st.session_state:
    st.session_state["feedback_type"] = ""
if "recommendations" not in st.session_state:
    st.session_state["recommendations"] = []
if "feedback" not in st.session_state:
    st.session_state["feedback"] = ""
if "customer_name" not in st.session_state:
    st.session_state["customer_name"] = ""
if "customer_email" not in st.session_state:
    st.session_state["customer_email"] = ""

# Load Lottie Animation JSON
def load_lottie_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Lottie Animation URLs
feedback_animation = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_ktwnwv5m.json")
recommendations_animation = load_lottie_url("https://assets7.lottiefiles.com/packages/lf20_y2q5phvx.json")
notifications_animation = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_rdkfh2cz.json")

# Sample Data for Recommendations
data = {
    "Preference": ["Dining", "Room", "Wellness", "Pricing"],
    "Top Recommendation": [
        "Experience our premium buffet dining that offers a wide range of gourmet dishes, including options for vegetarians, vegans, and gluten-free diets. Our chefs use the freshest ingredients to create a culinary delight that caters to all taste buds. Don't miss our weekend specials featuring international cuisines.",
        "Upgrade to our deluxe rooms, which are equipped with luxurious bedding, state-of-the-art amenities, and a breathtaking view. Enjoy complimentary room service and access to our exclusive lounge for a truly relaxing stay.",
        "Discover our comprehensive wellness programs that include yoga and meditation sessions, personalized fitness training, and spa therapies designed to rejuvenate your body and mind. Join our wellness workshops for tips on maintaining a healthy lifestyle.",
        "Take advantage of our special pricing options, including discounts for long-term stays, early bird bookings, and loyalty rewards. Explore our flexible packages that provide excellent value for money without compromising on quality."
    ]
}
recommendations_df = pd.DataFrame(data)

# Function to Send Email
def send_email(recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {e}"

# Function to Send Slack Notification
def send_slack_notification(message):
    try:
        client = WebClient(token=SLACK_TOKEN)
        response = client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
        if response['ok']:
            return "Slack notification sent successfully!"
    except SlackApiError as e:
        return f"Failed to send Slack notification: {e.response['error']}"

# Function to Classify Feedback
def classify_feedback(feedback_text):
    sentiment = TextBlob(feedback_text).sentiment.polarity
    return "Positive" if sentiment > 0 else "Negative"

# Generate Recommendations Based on Preferences
def generate_recommendations(selected_preferences):
    filtered_recommendations = recommendations_df[
        recommendations_df["Preference"].isin(selected_preferences)
    ]
    return filtered_recommendations["Top Recommendation"].tolist()

# Custom Styling
st.markdown(
    """
    <style>
        body {
            background-color: #FAF3DD; /* Light gold */
            color: black;
        }
        .stButton button {
            background-color: #4CAF50 !important;
            color: white !important;
            border-radius: 8px !important;
            font-size: 16px !important;
            padding: 8px 20px !important;
        }
        .stTextInput input, .stTextArea textarea, .stSelectbox select, .stMultiSelect select {
            background-color: #ADD8E6 !important; /* Light blue */
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Streamlit App Title
st.title("🌟 Customer Feedback Management System")

# Feedback Animation
st_lottie(feedback_animation, height=300, key="feedback_anim")

# Collect Customer Details and Feedback
st.subheader("Step 1: Customer Details and Feedback")
st.session_state["customer_name"] = st.text_input("Customer Name", st.session_state["customer_name"])
st.session_state["customer_email"] = st.text_input("Email Address", st.session_state["customer_email"])
st.session_state["feedback"] = st.text_area("Provide your Feedback", st.session_state["feedback"])

# Select Preferences
st.subheader("Step 2: Select Preferences for Recommendations")
selected_preferences = st.multiselect(
    "Select Areas for Recommendations",
    options=recommendations_df["Preference"].tolist(),
    default=st.session_state["preferences"]
)

if selected_preferences != st.session_state["preferences"]:
    st.session_state["preferences"] = selected_preferences

# Button for Classification and Recommendations
if st.button("Classify Feedback and Get Recommendations"):
    if not (st.session_state["customer_name"] and st.session_state["customer_email"] and st.session_state["feedback"]):
        st.error("Please fill all required fields before proceeding.")
    else:
        # Classify Feedback
        st.session_state["feedback_type"] = classify_feedback(st.session_state["feedback"])
        st.success(f"Feedback classified as: {st.session_state['feedback_type']}")

        # Generate Recommendations
        if not st.session_state["preferences"]:
            st.error("Please select at least one preference.")
        else:
            st.session_state["recommendations"] = generate_recommendations(st.session_state["preferences"])
            st.success("Recommendations generated successfully!")
            for rec in st.session_state["recommendations"]:
                st.write(f"- {rec}")

            # Prepare Email Content
            email_subject = "Thank You for Your Feedback!"
            email_body = f"""
            Hi {st.session_state['customer_name']},

            Thank you for sharing your feedback with us. Here's a summary of what we received:
            - **Feedback:** {st.session_state['feedback']}
            - **Feedback Type:** {st.session_state['feedback_type']}
            - **Preferences:** {', '.join(st.session_state['preferences'])}
            - **Recommendations:** {', '.join(st.session_state['recommendations'])}

            We appreciate your input and will use it to improve our services.

            Best regards,
            Feedback Team
            """
            email_status = send_email(st.session_state["customer_email"], email_subject, email_body)
            st.info(email_status)

            # Prepare Slack Notification
            slack_message = f"""
            *New Feedback Received:*
            - *Name:* {st.session_state['customer_name']}
            - *Email:* {st.session_state['customer_email']}
            - *Feedback:* {st.session_state['feedback']}
            - *Feedback Type:* {st.session_state['feedback_type']}
            - *Preferences:* {', '.join(st.session_state['preferences'])}
            - *Recommendations:* {', '.join(st.session_state['recommendations'])}
            """
            slack_status = send_slack_notification(slack_message)
            st.info(slack_status)
