import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Recommendation function
def recommend_services(df, new_feedback):
    # Check for required columns
    required_columns = ['Feedback', 'Dining Preference', 'Room Preference', 'Wellness', 'Pricing Pattern']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        return f"The following required columns are missing: {', '.join(missing_columns)}"

    df_subset = df[required_columns]

    # Combine relevant features for similarity and handle missing values
    df_subset['combined_features'] = (
        df_subset['Feedback'].fillna('') + " " +
        df_subset['Dining Preference'].fillna('') + " " +
        df_subset['Room Preference'].fillna('') + " " +
        df_subset['Wellness'].fillna('') + " " +
        df_subset['Pricing Pattern'].fillna('')
    )

    # Add new feedback as a temporary entry
    temp_df = pd.DataFrame([{'combined_features': new_feedback}])
    df_subset = pd.concat([df_subset, temp_df], ignore_index=True)

    # Vectorize combined features
    vectorizer = CountVectorizer().fit_transform(df_subset['combined_features'])
    similarity_matrix = cosine_similarity(vectorizer)

    # Find similarity scores for the new feedback
    new_feedback_index = len(df_subset) - 1
    similarity_scores = list(enumerate(similarity_matrix[new_feedback_index]))
    sorted_scores = sorted(similarity_scores[:-1], key=lambda x: x[1], reverse=True)

    # Get top 5 recommendations
    top_indices = [i[0] for i in sorted_scores[:5]]
    recommendations = df.iloc[top_indices][['Dining Preference', 'Room Preference', 'Wellness', 'Pricing Pattern']]

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

            # Feedback input
            st.sidebar.header("Manual Feedback")
            new_feedback = st.sidebar.text_area("Provide Feedback:")

            if st.sidebar.button("Get Recommendations"):
                if new_feedback:
                    st.subheader("Recommendations Based on Your Feedback")
                    recommendations = recommend_services(df, new_feedback)
                    if isinstance(recommendations, str):  # If it's an error message
                        st.write(recommendations)
                    else:
                        st.dataframe(recommendations)
                else:
                    st.warning("Please provide feedback to get recommendations.")
        except Exception as e:
            st.error(f"Error reading file: {e}")
    else:
        st.info("Please upload a CSV file to proceed.")

if __name__ == "__main__":
    main()
