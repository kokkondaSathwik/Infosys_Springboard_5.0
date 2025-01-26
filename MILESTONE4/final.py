# import streamlit as st
# import pandas as pd
# import numpy as np
# from textblob import TextBlob
# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Slack configuration
# SLACK_TOKEN = "xoxe.xoxp-1-Mi0yLTgxODAyNjUyNTM1MjMtODE4Mjg4MjQzMDUxNi04MzU4ODUxMjE3OTM3LTgzMzE2MjUyODY4NzEtMzZhMTgyNTQ0NzUxOTk4MzY0MTUxZTEwYzhkYTQzYWM5NDUwYWExYzBjZWMwNzJkZWMwZmMzZDU0ZmMwMjg0Yg"
# SLACK_CHANNEL = "#test-slackbot"

# # Email configuration
# EMAIL_ADDRESS = "sathwikkokkonda6787@gmail.com"
# EMAIL_PASSWORD = "Sathwik123@"

# # Function to analyze sentiment
# def analyze_sentiment(feedback):
#     analysis = TextBlob(feedback)
#     sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative"
#     areas_of_concern = []
#     if "price" in feedback.lower():
#         areas_of_concern.append("Pricing")
#     if "service" in feedback.lower():
#         areas_of_concern.append("Service")
#     if "quality" in feedback.lower():
#         areas_of_concern.append("Product Quality")
#     return sentiment, areas_of_concern

# # Function to send email
# def send_email(recipient_email, subject, body):
#     try:
#         msg = MIMEMultipart()
#         msg['From'] = EMAIL_ADDRESS
#         msg['To'] = recipient_email
#         msg['Subject'] = subject
#         msg.attach(MIMEText(body, 'plain'))

#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#         server.send_message(msg)
#         server.quit()
#         return "Email sent successfully!"
#     except Exception as e:
#         return f"Failed to send email: {e}"

# # Function to send Slack notification
# def send_slack_notification(message):
#     try:
#         client = WebClient(token=SLACK_TOKEN)
#         response = client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
#         if response['ok']:
#             return "Slack notification sent successfully!"
#     except SlackApiError as e:
#         return f"Failed to send Slack notification: {e.response['error']}"

# # Streamlit app
# def main():
#     st.title("Customer Feedback Management System")

#     # Input form for feedback
#     with st.form("feedback_form"):
#         customer_name = st.text_input("Customer Name")
#         customer_email = st.text_input("Email Address")
#         feedback = st.text_area("Provide your Feedback")
#         submitted = st.form_submit_button("Submit Feedback")

#     if submitted:
#         if customer_name and customer_email and feedback:
#             # Analyze sentiment and identify areas of concern
#             sentiment, areas_of_concern = analyze_sentiment(feedback)
#             st.success(f"Feedback Sentiment: {sentiment}")
#             st.info(f"Areas of Concern: {', '.join(areas_of_concern) if areas_of_concern else 'None'}")

#             # Allow user to add preferences/recommendations
#             st.subheader("Add Preferences/Recommendations")
#             preferences = st.multiselect("Select Areas for Recommendations", ["Dining", "Room", "Wellness", "Pricing"])
#             recommendation_details = st.text_area("Recommendation Details (Optional)")

#             # Send email and Slack notifications
#             email_subject = f"Feedback Received: {sentiment} Sentiment"
#             email_body = f"""
#             Hello {customer_name},

#             Thank you for your feedback! Here's what we analyzed:
#             Sentiment: {sentiment}
#             Areas of Concern: {', '.join(areas_of_concern) if areas_of_concern else 'None'}
#             Your Preferences: {', '.join(preferences) if preferences else 'None'}
            
#             Best Regards,
#             Feedback Team
#             """
#             email_status = send_email(customer_email, email_subject, email_body)
#             st.info(email_status)

#             slack_message = f"""
#             New Feedback Received:
#             - Name: {customer_name}
#             - Sentiment: {sentiment}
#             - Areas of Concern: {', '.join(areas_of_concern) if areas_of_concern else 'None'}
#             """
#             slack_status = send_slack_notification(slack_message)
#             st.info(slack_status)

#             st.success("Feedback processed successfully!")
#         else:
#             st.error("Please fill in all fields.")

# if __name__ == "__main__":
#     main()

# import streamlit as st
# import pandas as pd
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError

# # Initialize Session State
# if "preferences" not in st.session_state:
#     st.session_state["preferences"] = []
# if "recommendation_details" not in st.session_state:
#     st.session_state["recommendation_details"] = ""

# # Sample Data for Recommendations (replace this with your dataset if needed)
# data = {
#     "Preference": ["Dining", "Room", "Wellness", "Pricing"],
#     "Top Recommendation": [
#         "Try our premium buffet dining experience.",
#         "Upgrade to a deluxe room for better comfort.",
#         "Check out our yoga and meditation classes.",
#         "Avail special discounts on long-term bookings."
#     ]
# }
# recommendations_df = pd.DataFrame(data)

# # Email Configuration
# EMAIL_ADDRESS = "sathwikkokki2@gmail.com"
# EMAIL_PASSWORD = "nuvb oyjj ivwg tvlw"

# # Slack Configuration
# SLACK_TOKEN = "xoxb-8369506059808-8343911087205-8mI5YVmecj0Mix0raoVUYyis"
# SLACK_CHANNEL = "#testing"

# # Function to Send Email
# def send_email(recipient_email, subject, body):
#     try:
#         msg = MIMEMultipart()
#         msg['From'] = EMAIL_ADDRESS
#         msg['To'] = recipient_email
#         msg['Subject'] = subject
#         msg.attach(MIMEText(body, 'plain'))

#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#         server.send_message(msg)
#         server.quit()
#         return "Email sent successfully!"
#     except Exception as e:
#         return f"Failed to send email: {e}"

# # Function to Send Slack Notification
# def send_slack_notification(message):
#     try:
#         client = WebClient(token=SLACK_TOKEN)
#         response = client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
#         if response['ok']:
#             return "Slack notification sent successfully!"
#     except SlackApiError as e:
#         return f"Failed to send Slack notification: {e.response['error']}"

# # Streamlit App Title
# st.title("Customer Feedback Management System")

# # Feedback Form
# with st.form("feedback_form"):
#     customer_name = st.text_input("Customer Name")
#     customer_email = st.text_input("Email Address")
#     feedback = st.text_area("Provide your Feedback")
#     submitted = st.form_submit_button("Submit Feedback")

# # Add Preferences Section
# st.subheader("Add Preferences/Recommendations")

# # Multiselect for Preferences
# selected_preferences = st.multiselect(
#     "Select Areas for Recommendations",
#     options=recommendations_df["Preference"].tolist(),
#     default=st.session_state["preferences"]
# )

# # Persist preferences in session state
# if selected_preferences != st.session_state["preferences"]:
#     st.session_state["preferences"] = selected_preferences

# # Additional Recommendation Details
# recommendation_details = st.text_area(
#     "Recommendation Details (Optional)", value=st.session_state["recommendation_details"]
# )
# if recommendation_details != st.session_state["recommendation_details"]:
#     st.session_state["recommendation_details"] = recommendation_details

# # Show Recommendations Based on Preferences
# if st.session_state["preferences"]:
#     st.subheader("Recommendations Based on Preferences")
#     filtered_recommendations = recommendations_df[
#         recommendations_df["Preference"].isin(st.session_state["preferences"])
#     ]
#     for _, row in filtered_recommendations.iterrows():
#         st.markdown(f"**{row['Preference']}**: {row['Top Recommendation']}")

# # Feedback Submission Logic
# if submitted:
#     st.success("Feedback submitted successfully!")
#     st.write("Customer Name:", customer_name)
#     st.write("Email Address:", customer_email)
#     st.write("Feedback:", feedback)
#     st.write("Selected Preferences:", st.session_state["preferences"])
#     st.write("Additional Recommendation Details:", st.session_state["recommendation_details"])

#     # Prepare Email Content
#     email_subject = "Thank You for Your Feedback!"
#     email_body = f"""
#     Hi {customer_name},

#     Thank you for sharing your feedback with us. Here's a summary of what we received:
#     - Feedback: {feedback}
#     - Preferences: {', '.join(st.session_state['preferences'])}
#     - Recommendations: {st.session_state['recommendation_details']}

#     We appreciate your input and will use it to improve our services.

#     Best regards,
#     Feedback Team
#     """
#     email_status = send_email(customer_email, email_subject, email_body)
#     st.info(email_status)

#     # Prepare Slack Notification
#     slack_message = f"""
#     New Feedback Received:
#     - Name: {customer_name}
#     - Email: {customer_email}
#     - Feedback: {feedback}
#     - Preferences: {', '.join(st.session_state['preferences'])}
#     """
#     slack_status = send_slack_notification(slack_message)
#     st.info(slack_status)

# import streamlit as st
# import pandas as pd
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError
# from textblob import TextBlob

# # Initialize Session State
# if "preferences" not in st.session_state:
#     st.session_state["preferences"] = []
# if "recommendation_details" not in st.session_state:
#     st.session_state["recommendation_details"] = ""

# # Sample Data for Recommendations (replace this with your dataset if needed)
# data = {
#     "Preference": ["Dining", "Room", "Wellness", "Pricing"],
#     "Top Recommendation": [
#         "Try our premium buffet dining experience.",
#         "Upgrade to a deluxe room for better comfort.",
#         "Check out our yoga and meditation classes.",
#         "Avail special discounts on long-term bookings."
#     ]
# }
# recommendations_df = pd.DataFrame(data)

# # Email Configuration
# EMAIL_ADDRESS = "sathwikkokki2@gmail.com"
# EMAIL_PASSWORD = "nuvb oyjj ivwg tvlw"

# # Slack Configuration
# SLACK_TOKEN = "xoxb-8369506059808-8343911087205-8mI5YVmecj0Mix0raoVUYyis"
# SLACK_CHANNEL = "#testing"

# # Function to Send Email
# def send_email(recipient_email, subject, body):
#     try:
#         msg = MIMEMultipart()
#         msg['From'] = EMAIL_ADDRESS
#         msg['To'] = recipient_email
#         msg['Subject'] = subject
#         msg.attach(MIMEText(body, 'plain'))

#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#         server.send_message(msg)
#         server.quit()
#         return "Email sent successfully!"
#     except Exception as e:
#         return f"Failed to send email: {e}"

# # Function to Send Slack Notification
# def send_slack_notification(message):
#     try:
#         client = WebClient(token=SLACK_TOKEN)
#         response = client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
#         if response['ok']:
#             return "Slack notification sent successfully!"
#     except SlackApiError as e:
#         return f"Failed to send Slack notification: {e.response['error']}"

# # Function to Classify Feedback
# def classify_feedback(feedback_text):
#     sentiment = TextBlob(feedback_text).sentiment.polarity
#     return "Positive" if sentiment > 0 else "Negative"

# # Streamlit App Title
# st.title("Customer Feedback Management System")

# # Feedback Form
# with st.form("feedback_form"):
#     customer_name = st.text_input("Customer Name")
#     customer_email = st.text_input("Email Address")
#     feedback = st.text_area("Provide your Feedback")
#     submitted = st.form_submit_button("Submit Feedback")

# # Add Preferences Section
# st.subheader("Add Preferences/Recommendations")

# # Multiselect for Preferences
# selected_preferences = st.multiselect(
#     "Select Areas for Recommendations",
#     options=recommendations_df["Preference"].tolist(),
#     default=st.session_state["preferences"]
# )

# # Persist preferences in session state
# if selected_preferences != st.session_state["preferences"]:
#     st.session_state["preferences"] = selected_preferences

# # Additional Recommendation Details
# recommendation_details = st.text_area(
#     "Recommendation Details (Optional)", value=st.session_state["recommendation_details"]
# )
# if recommendation_details != st.session_state["recommendation_details"]:
#     st.session_state["recommendation_details"] = recommendation_details

# # Show Recommendations Based on Preferences
# if st.session_state["preferences"]:
#     st.subheader("Recommendations Based on Preferences")
#     filtered_recommendations = recommendations_df[
#         recommendations_df["Preference"].isin(st.session_state["preferences"])
#     ]
#     for _, row in filtered_recommendations.iterrows():
#         st.markdown(f"**{row['Preference']}**: {row['Top Recommendation']}")

# # Feedback Submission Logic
# if submitted:
#     feedback_type = classify_feedback(feedback)
#     st.success("Feedback submitted successfully!")
#     st.write("**Customer Name:**", customer_name)
#     st.write("**Email Address:**", customer_email)
#     st.write("**Feedback:**", feedback)
#     st.write("**Feedback Type:**", feedback_type)
#     st.write("**Selected Preferences:**", ", ".join(st.session_state["preferences"]))
#     st.write("**Additional Recommendation Details:**", st.session_state["recommendation_details"])

#     # Prepare Email Content
#     email_subject = "Thank You for Your Feedback!"
#     email_body = f"""
#     Hi {customer_name},

#     Thank you for sharing your feedback with us. Here's a summary of what we received:
#     - **Feedback:** {feedback}
#     - **Feedback Type:** {feedback_type}
#     - **Preferences:** {', '.join(st.session_state['preferences'])}
#     - **Recommendations:** {st.session_state['recommendation_details']}

#     We appreciate your input and will use it to improve our services.

#     Best regards,
#     Feedback Team
#     """
#     email_status = send_email(customer_email, email_subject, email_body)
#     st.info(email_status)

#     # Prepare Slack Notification
#     slack_message = f"""
#     *New Feedback Received:*
#     - *Name:* {customer_name}
#     - *Email:* {customer_email}
#     - *Feedback:* {feedback}
#     - *Feedback Type:* {feedback_type}
#     - *Preferences:* {', '.join(st.session_state['preferences'])}
#     """
#     slack_status = send_slack_notification(slack_message)
#     st.info(slack_status)

# import streamlit as st
# import pandas as pd
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError
# from textblob import TextBlob

# # Initialize Session State
# if "preferences" not in st.session_state:
#     st.session_state["preferences"] = []
# if "recommendation_details" not in st.session_state:
#     st.session_state["recommendation_details"] = ""

# # Sample Data for Recommendations (replace this with your dataset if needed)
# data = {
#     "Preference": ["Dining", "Room", "Wellness", "Pricing"],
#     "Top Recommendation": [
#         "Try our premium buffet dining experience.",
#         "Upgrade to a deluxe room for better comfort.",
#         "Check out our yoga and meditation classes.",
#         "Avail special discounts on long-term bookings."
#     ]
# }
# recommendations_df = pd.DataFrame(data)

# # Email Configuration
# EMAIL_ADDRESS = "sathwikkokki2@gmail.com"
# EMAIL_PASSWORD = "nuvb oyjj ivwg tvlw"

# # Slack Configuration
# SLACK_TOKEN = "xoxb-8369506059808-8343911087205-8mI5YVmecj0Mix0raoVUYyis"
# SLACK_CHANNEL = "#testing"

# # Function to Send Email
# def send_email(recipient_email, subject, body):
#     try:
#         msg = MIMEMultipart()
#         msg['From'] = EMAIL_ADDRESS
#         msg['To'] = recipient_email
#         msg['Subject'] = subject
#         msg.attach(MIMEText(body, 'plain'))

#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#         server.send_message(msg)
#         server.quit()
#         return "Email sent successfully!"
#     except Exception as e:
#         return f"Failed to send email: {e}"

# # Function to Send Slack Notification
# def send_slack_notification(message):
#     try:
#         client = WebClient(token=SLACK_TOKEN)
#         response = client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
#         if response['ok']:
#             return "Slack notification sent successfully!"
#     except SlackApiError as e:
#         return f"Failed to send Slack notification: {e.response['error']}"

# # Function to Classify Feedback
# def classify_feedback(feedback_text):
#     sentiment = TextBlob(feedback_text).sentiment.polarity
#     return "Positive" if sentiment > 0 else "Negative"

# # Generate Additional Recommendations Based on Feedback
# def generate_feedback_recommendations(feedback_text):
#     if "food" in feedback_text.lower() or "dining" in feedback_text.lower():
#         return ["Explore our new gourmet menu.", "Enjoy exclusive dining discounts this weekend."]
#     elif "room" in feedback_text.lower():
#         return ["Upgrade to our executive suite for extra comfort.", "Try our late checkout options for a relaxed stay."]
#     elif "wellness" in feedback_text.lower() or "health" in feedback_text.lower():
#         return ["Join our spa membership for year-round relaxation.", "Check out our new wellness workshops."]
#     else:
#         return ["Contact our support team for personalized recommendations."]

# # Streamlit App Title
# st.title("Customer Feedback Management System")

# # Feedback Form
# with st.form("feedback_form"):
#     customer_name = st.text_input("Customer Name")
#     customer_email = st.text_input("Email Address")
#     feedback = st.text_area("Provide your Feedback")
#     submitted = st.form_submit_button("Submit Feedback")

# # Add Preferences Section
# st.subheader("Add Preferences/Recommendations")

# # Multiselect for Preferences
# selected_preferences = st.multiselect(
#     "Select Areas for Recommendations",
#     options=recommendations_df["Preference"].tolist(),
#     default=st.session_state["preferences"]
# )

# # Persist preferences in session state
# if selected_preferences != st.session_state["preferences"]:
#     st.session_state["preferences"] = selected_preferences

# # Additional Recommendation Details
# recommendation_details = st.text_area(
#     "Recommendation Details (Optional)", value=st.session_state["recommendation_details"]
# )
# if recommendation_details != st.session_state["recommendation_details"]:
#     st.session_state["recommendation_details"] = recommendation_details

# # Show Recommendations Based on Preferences
# if st.session_state["preferences"]:
#     st.subheader("Recommendations Based on Preferences")
#     filtered_recommendations = recommendations_df[
#         recommendations_df["Preference"].isin(st.session_state["preferences"])
#     ]
#     for _, row in filtered_recommendations.iterrows():
#         st.markdown(f"**{row['Preference']}**: {row['Top Recommendation']}")

# # Feedback Submission Logic
# if submitted:
#     feedback_type = classify_feedback(feedback)
#     additional_recommendations = generate_feedback_recommendations(feedback)

#     st.success("Feedback submitted successfully!")
#     st.write("**Customer Name:**", customer_name)
#     st.write("**Email Address:**", customer_email)
#     st.write("**Feedback:**", feedback)
#     st.write("**Feedback Type:**", feedback_type)
#     st.write("**Selected Preferences:**", ", ".join(st.session_state["preferences"]))
#     st.write("**Additional Recommendation Details:**", st.session_state["recommendation_details"])
#     st.write("**Recommendations Based on Feedback:**")
#     for rec in additional_recommendations:
#         st.write(f"- {rec}")

#     # Prepare Email Content
#     email_subject = "Thank You for Your Feedback!"
#     email_body = f"""
#     Hi {customer_name},

#     Thank you for sharing your feedback with us. Here's a summary of what we received:
#     - **Feedback:** {feedback}
#     - **Feedback Type:** {feedback_type}
#     - **Preferences:** {', '.join(st.session_state['preferences'])}
#     - **Recommendations:** {st.session_state['recommendation_details']}
#     - **Additional Recommendations Based on Feedback:** {', '.join(additional_recommendations)}

#     We appreciate your input and will use it to improve our services.

#     Best regards,
#     Feedback Team
#     """
#     email_status = send_email(customer_email, email_subject, email_body)
#     st.info(email_status)

#     # Prepare Slack Notification
#     slack_message = f"""
#     *New Feedback Received:*
#     - *Name:* {customer_name}
#     - *Email:* {customer_email}
#     - *Feedback:* {feedback}
#     - *Feedback Type:* {feedback_type}
#     - *Preferences:* {', '.join(st.session_state['preferences'])}
#     - *Recommendations Based on Feedback:* {', '.join(additional_recommendations)}
#     """
#     slack_status = send_slack_notification(slack_message)
#     st.info(slack_status)


#final code -1 
# import streamlit as st
# import pandas as pd
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError
# from textblob import TextBlob

# # Initialize Session State
# if "preferences" not in st.session_state:
#     st.session_state["preferences"] = []
# if "recommendation_details" not in st.session_state:
#     st.session_state["recommendation_details"] = ""
# if "feedback_type" not in st.session_state:
#     st.session_state["feedback_type"] = ""
# if "recommendations" not in st.session_state:
#     st.session_state["recommendations"] = []

# # Sample Data for Recommendations (replace this with your dataset if needed)
# data = {
#     "Preference": ["Dining", "Room", "Wellness", "Pricing"],
#     "Top Recommendation": [
#         "Try our premium buffet dining experience.",
#         "Upgrade to a deluxe room for better comfort.",
#         "Check out our yoga and meditation classes.",
#         "Avail special discounts on long-term bookings."
#     ]
# }
# recommendations_df = pd.DataFrame(data)

# # Email Configuration
# EMAIL_ADDRESS = "sathwikkokki2@gmail.com"
# EMAIL_PASSWORD = "nuvb oyjj ivwg tvlw"

# # Slack Configuration
# SLACK_TOKEN = "xoxb-8369506059808-8343911087205-8mI5YVmecj0Mix0raoVUYyis"
# SLACK_CHANNEL = "#testing"

# # Function to Send Email
# def send_email(recipient_email, subject, body):
#     try:
#         msg = MIMEMultipart()
#         msg['From'] = EMAIL_ADDRESS
#         msg['To'] = recipient_email
#         msg['Subject'] = subject
#         msg.attach(MIMEText(body, 'plain'))

#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#         server.send_message(msg)
#         server.quit()
#         return "Email sent successfully!"
#     except Exception as e:
#         return f"Failed to send email: {e}"

# # Function to Send Slack Notification
# def send_slack_notification(message):
#     try:
#         client = WebClient(token=SLACK_TOKEN)
#         response = client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
#         if response['ok']:
#             return "Slack notification sent successfully!"
#     except SlackApiError as e:
#         return f"Failed to send Slack notification: {e.response['error']}"

# # Function to Classify Feedback
# def classify_feedback(feedback_text):
#     sentiment = TextBlob(feedback_text).sentiment.polarity
#     return "Positive" if sentiment > 0 else "Negative"

# # Generate Recommendations Based on Preferences
# def generate_recommendations(selected_preferences):
#     filtered_recommendations = recommendations_df[
#         recommendations_df["Preference"].isin(selected_preferences)
#     ]
#     return filtered_recommendations["Top Recommendation"].tolist()

# # Streamlit App Title
# st.title("Customer Feedback Management System")

# # Step 1: Collect Customer Details and Feedback
# customer_name = st.text_input("Customer Name")
# customer_email = st.text_input("Email Address")
# feedback = st.text_area("Provide your Feedback")

# if st.button("Classify Feedback"):
#     st.session_state["feedback_type"] = classify_feedback(feedback)
#     st.success(f"Feedback classified as: {st.session_state['feedback_type']}")

# # Step 2: Select Preferences
# st.subheader("Select Preferences for Recommendations")
# selected_preferences = st.multiselect(
#     "Select Areas for Recommendations",
#     options=recommendations_df["Preference"].tolist(),
#     default=st.session_state["preferences"]
# )

# if selected_preferences != st.session_state["preferences"]:
#     st.session_state["preferences"] = selected_preferences

# # Step 3: Get Recommendations
# if st.button("Get Recommendations"):
#     st.session_state["recommendations"] = generate_recommendations(st.session_state["preferences"])
#     st.success("Recommendations generated successfully!")
#     for rec in st.session_state["recommendations"]:
#         st.write(f"- {rec}")

# # Step 4: Send Email and Slack Notification
# if st.session_state["recommendations"] and customer_name and customer_email and feedback:
#     # Prepare Email Content
#     email_subject = "Thank You for Your Feedback!"
#     email_body = f"""
#     Hi {customer_name},

#     Thank you for sharing your feedback with us. Here's a summary of what we received:
#     - **Feedback:** {feedback}
#     - **Feedback Type:** {st.session_state['feedback_type']}
#     - **Preferences:** {', '.join(st.session_state['preferences'])}
#     - **Recommendations:** {', '.join(st.session_state['recommendations'])}

#     We appreciate your input and will use it to improve our services.

#     Best regards,
#     Feedback Team
#     """
#     email_status = send_email(customer_email, email_subject, email_body)
#     st.info(email_status)

#     # Prepare Slack Notification
#     slack_message = f"""
#     *New Feedback Received:*
#     - *Name:* {customer_name}
#     - *Email:* {customer_email}
#     - *Feedback:* {feedback}
#     - *Feedback Type:* {st.session_state['feedback_type']}
#     - *Preferences:* {', '.join(st.session_state['preferences'])}
#     - *Recommendations:* {', '.join(st.session_state['recommendations'])}
#     """
#     slack_status = send_slack_notification(slack_message)
#     st.info(slack_status)

#final code -2


import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from textblob import TextBlob
from dotenv import load_dotenv
import os

# Initialize Session State
if "preferences" not in st.session_state:
    st.session_state["preferences"] = []
if "recommendation_details" not in st.session_state:
    st.session_state["recommendation_details"] = ""
if "feedback_type" not in st.session_state:
    st.session_state["feedback_type"] = ""
if "recommendations" not in st.session_state:
    st.session_state["recommendations"] = []

# Sample Data for Recommendations (replace this with your dataset if needed)
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

# # Email Configuration
# EMAIL_ADDRESS = "EMAIL"
# EMAIL_PASSWORD = "PASSWORD"

# # Slack Configuration
# SLACK_TOKEN = "SLACK-TOKEN"
# SLACK_CHANNEL = "SLACK-CHANNEL"

# from dotenv import load_dotenv
# import os

load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("PASSWORD")
SLACK_TOKEN = os.getenv("SLACK-TOKEN")
SLACK_CHANNEL = os.getenv("SLACK-CHANNEL")


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

# Streamlit App Title
st.title("Customer Feedback Management System")

# Step 1: Collect Customer Details and Feedback
customer_name = st.text_input("Customer Name")
customer_email = st.text_input("Email Address")
feedback = st.text_area("Provide your Feedback")

if st.button("Classify Feedback"):
    st.session_state["feedback_type"] = classify_feedback(feedback)
    st.success(f"Feedback classified as: {st.session_state['feedback_type']}")

# Step 2: Select Preferences
st.subheader("Select Preferences for Recommendations")
selected_preferences = st.multiselect(
    "Select Areas for Recommendations",
    options=recommendations_df["Preference"].tolist(),
    default=st.session_state["preferences"]
)

if selected_preferences != st.session_state["preferences"]:
    st.session_state["preferences"] = selected_preferences

# Step 3: Get Recommendations
if st.button("Get Recommendations"):
    st.session_state["recommendations"] = generate_recommendations(st.session_state["preferences"])
    st.success("Recommendations generated successfully!")
    for rec in st.session_state["recommendations"]:
        st.write(f"- {rec}")

# Step 4: Send Email and Slack Notification
if st.session_state["recommendations"] and customer_name and customer_email and feedback:
    # Prepare Email Content
    email_subject = "Thank You for Your Feedback!"
    email_body = f"""
    Hi {customer_name},

    Thank you for sharing your feedback with us. Here's a summary of what we received:
    - **Feedback:** {feedback}
    - **Feedback Type:** {st.session_state['feedback_type']}
    - **Preferences:** {', '.join(st.session_state['preferences'])}
    - **Recommendations:** {', '.join(st.session_state['recommendations'])}

    We appreciate your input and will use it to improve our services.

    Best regards,
    Feedback Team
    """
    email_status = send_email(customer_email, email_subject, email_body)
    st.info(email_status)

    # Prepare Slack Notification
    slack_message = f"""
    *New Feedback Received:*
    - *Name:* {customer_name}
    - *Email:* {customer_email}
    - *Feedback:* {feedback}
    - *Feedback Type:* {st.session_state['feedback_type']}
    - *Preferences:* {', '.join(st.session_state['preferences'])}
    - *Recommendations:* {', '.join(st.session_state['recommendations'])}
    """
    slack_status = send_slack_notification(slack_message)
    st.info(slack_status)

#testing
# import streamlit as st
# import pandas as pd
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError
# from textblob import TextBlob
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()
# EMAIL_ADDRESS = os.getenv("EMAIL")
# EMAIL_PASSWORD = os.getenv("PASSWORD")
# SLACK_TOKEN = os.getenv("SLACK-TOKEN")
# SLACK_CHANNEL = os.getenv("SLACK-CHANNEL")

# # Initialize Session State
# if "preferences" not in st.session_state:
#     st.session_state["preferences"] = []
# if "recommendation_details" not in st.session_state:
#     st.session_state["recommendation_details"] = ""
# if "feedback_type" not in st.session_state:
#     st.session_state["feedback_type"] = ""
# if "recommendations" not in st.session_state:
#     st.session_state["recommendations"] = []

# # Sample Data for Recommendations (replace this with your dataset if needed)
# data = {
#     "Preference": ["Dining", "Room", "Wellness", "Pricing"],
#     "Top Recommendation": [
#         "Experience our premium buffet dining that offers a wide range of gourmet dishes, including options for vegetarians, vegans, and gluten-free diets. Our chefs use the freshest ingredients to create a culinary delight that caters to all taste buds. Don't miss our weekend specials featuring international cuisines.",
#         "Upgrade to our deluxe rooms, which are equipped with luxurious bedding, state-of-the-art amenities, and a breathtaking view. Enjoy complimentary room service and access to our exclusive lounge for a truly relaxing stay.",
#         "Discover our comprehensive wellness programs that include yoga and meditation sessions, personalized fitness training, and spa therapies designed to rejuvenate your body and mind. Join our wellness workshops for tips on maintaining a healthy lifestyle.",
#         "Take advantage of our special pricing options, including discounts for long-term stays, early bird bookings, and loyalty rewards. Explore our flexible packages that provide excellent value for money without compromising on quality."
#     ]
# }
# recommendations_df = pd.DataFrame(data)

# # Function to Send Email
# def send_email(recipient_email, subject, body):
#     try:
#         msg = MIMEMultipart()
#         msg['From'] = EMAIL_ADDRESS
#         msg['To'] = recipient_email
#         msg['Subject'] = subject
#         msg.attach(MIMEText(body, 'plain'))

#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#         server.send_message(msg)
#         server.quit()
#         return "Email sent successfully!"
#     except Exception as e:
#         return f"Failed to send email: {e}"

# # Function to Send Slack Notification
# def send_slack_notification(message):
#     try:
#         client = WebClient(token=SLACK_TOKEN)
#         response = client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
#         if response['ok']:
#             return "Slack notification sent successfully!"
#     except SlackApiError as e:
#         return f"Failed to send Slack notification: {e.response['error']}"

# # Function to Classify Feedback
# def classify_feedback(feedback_text):
#     sentiment = TextBlob(feedback_text).sentiment.polarity
#     return "Positive" if sentiment > 0 else "Negative"

# # Generate Recommendations Based on Preferences
# def generate_recommendations(selected_preferences):
#     filtered_recommendations = recommendations_df[
#         recommendations_df["Preference"].isin(selected_preferences)
#     ]
#     return filtered_recommendations["Top Recommendation"].tolist()

# # Streamlit App Title
# st.title("Customer Feedback Management System")

# # Step 1: Collect Customer Details and Feedback
# customer_name = st.text_input("Customer Name")
# customer_email = st.text_input("Email Address")
# feedback = st.text_area("Provide your Feedback")

# if st.button("Classify Feedback"):
#     st.session_state["feedback_type"] = classify_feedback(feedback)
#     st.success(f"Feedback classified as: {st.session_state['feedback_type']}")

# # Step 2: Select Preferences
# st.subheader("Select Preferences for Recommendations")
# selected_preferences = st.multiselect(
#     "Select Areas for Recommendations",
#     options=recommendations_df["Preference"].tolist(),
#     default=st.session_state["preferences"]
# )

# if selected_preferences != st.session_state["preferences"]:
#     st.session_state["preferences"] = selected_preferences

# # Step 3: Get Recommendations
# if st.button("Get Recommendations"):
#     st.session_state["recommendations"] = generate_recommendations(st.session_state["preferences"])
#     st.success("Recommendations generated successfully!")
#     for rec in st.session_state["recommendations"]:
#         st.write(f"- {rec}")

# # Step 4: Add a Button to Send Notifications
# if st.button("Send Notifications"):
#     if st.session_state["recommendations"] and customer_name and customer_email and feedback:
#         # Prepare Email Content
#         email_subject = "Thank You for Your Feedback!"
#         email_body = f"""
#         Hi {customer_name},

#         Thank you for sharing your feedback with us. Here's a summary of what we received:
#         - **Feedback:** {feedback}
#         - **Feedback Type:** {st.session_state['feedback_type']}
#         - **Preferences:** {', '.join(st.session_state['preferences'])}
#         - **Recommendations:** {', '.join(st.session_state['recommendations'])}

#         We appreciate your input and will use it to improve our services.

#         Best regards,
#         Feedback Team
#         """
#         email_status = send_email(customer_email, email_subject, email_body)
#         st.info(email_status)

#         # Prepare Slack Notification
#         slack_message = f"""
#         *New Feedback Received:*
#         - *Name:* {customer_name}
#         - *Email:* {customer_email}
#         - *Feedback:* {feedback}
#         - *Feedback Type:* {st.session_state['feedback_type']}
#         - *Preferences:* {', '.join(st.session_state['preferences'])}
#         - *Recommendations:* {', '.join(st.session_state['recommendations'])}
#         """
#         slack_status = send_slack_notification(slack_message)
#         st.info(slack_status)
#     else:
#         st.warning("Please complete all steps before sending notifications!")















