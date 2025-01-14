import streamlit as st
import pandas as pd

# Load Dataset
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Analyze Feedback Sentiment
def sentiment_analysis(data):
    sentiment_counts = data['sentiment-future'].value_counts()
    return sentiment_counts

# Main App
def main():
    st.title("Feedback Analysis Dashboard")
    
    # File upload
    uploaded_file = st.file_uploader("Upload the feedback dataset CSV", type=["csv"])
    
    if uploaded_file:
        # Load the data
        data = load_data(uploaded_file)
        
        # Display Data
        st.subheader("Dataset Preview")
        st.dataframe(data.head())
        
        # Sentiment Analysis
        st.subheader("Sentiment Analysis")
        sentiment_counts = sentiment_analysis(data)
        st.bar_chart(sentiment_counts)
        
        # Customer Insights
        st.subheader("Customer Insights")
        avg_stay = data['customer-stay duration'].mean()
        total_customers = len(data)
        avg_payment = data['customer-amt to be paid'].mean()
        
        st.metric("Average Stay Duration", f"{avg_stay:.2f} days")
        st.metric("Total Customers", total_customers)
        st.metric("Average Payment Amount", f"${avg_payment:.2f}")
        
        # Department-wise Feedback
        st.subheader("Feedback by Department")
        dept_feedback = data['dept'].value_counts()
        st.bar_chart(dept_feedback)
        
if __name__ == "__main__":
    main()
