import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Recommendation function
def recommend_services(df, customer_name):
    if 'Customer Name' not in df.columns:
        return "The uploaded file does not contain a 'Customer Name' column."
    
    # Check if customer exists in the dataset
    if customer_name not in df['Customer Name'].values:
        return "Customer not found. Please try a different name."
    
    # Subset data for recommendation
    required_columns = ['Feedback', 'Dining Preference', 'Room Preference', 'Wellness', 'Pricing Pattern']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        return f"The following required columns are missing: {', '.join(missing_columns)}"
    
    df_subset = df[required_columns]
    
    # Combine relevant features for similarity
    df_subset['combined_features'] = df_subset['Feedback'] + " " + \
                                     df_subset['Dining Preference'] + " " + \
                                     df_subset['Room Preference'] + " " + \
                                     df_subset['Wellness'] + " " + \
                                     df_subset['Pricing Pattern']
    
    # Vectorize combined features
    vectorizer = CountVectorizer().fit_transform(df_subset['combined_features'])
    similarity_matrix = cosine_similarity(vectorizer)
    
    # Find index of the input customer
    customer_index = df[df['Customer Name'] == customer_name].index[0]
    
    # Get similarity scores for the customer
    similarity_scores = list(enumerate(similarity_matrix[customer_index]))
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    # Get top 5 recommendations
    top_indices = [i[0] for i in sorted_scores[1:6]]
    recommendations = df.iloc[top_indices][['Customer Name', 'dept', 'Dining Preference', 'Room Preference', 'Wellness']]
    
    return recommendations

# Streamlit app
def main():
    st.title("Feedback-Based Recommendation System")
    
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.sidebar.success("File successfully uploaded!")
            st.sidebar.header("Dataset Preview")
            if st.sidebar.checkbox("Show Dataset"):
                st.write(df.head())
            
            # Recommendation functionality
            st.sidebar.title("Options")
            customer_name = st.sidebar.text_input("Enter Customer Name for Recommendations")
            
            if st.sidebar.button("Get Recommendations"):
                if customer_name:
                    st.subheader(f"Recommendations for {customer_name}")
                    recommendations = recommend_services(df, customer_name)
                    if isinstance(recommendations, str):  # If it's an error message
                        st.write(recommendations)
                    else:
                        st.dataframe(recommendations)
                else:
                    st.warning("Please enter a valid customer name.")
        except Exception as e:
            st.error(f"Error reading file: {e}")
    else:
        st.info("Please upload a CSV file to proceed.")

if __name__ == "__main__":
    main()
