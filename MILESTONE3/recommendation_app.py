import streamlit as st
import pandas as pd
import numpy as np

# Recommendation function
def recommend_categories(df):
    # Add placeholder values if columns are missing
    if 'Time Spent' not in df.columns:
        df['Time Spent'] = np.random.uniform(1, 5, len(df))
    if 'Ratings' not in df.columns:
        df['Ratings'] = np.random.uniform(1, 5, len(df))

    recommendations = {}

    # Calculate recommendations for each feature
    for feature in ['Dining Preference', 'Room Preference', 'Wellness', 'Pricing Pattern']:
        if feature in df.columns:
            grouped = df.groupby(feature).agg({'Time Spent': 'mean', 'Ratings': 'mean'}).reset_index()
            grouped['Score'] = grouped['Time Spent'] * grouped['Ratings']  # Combine metrics to rank categories
            top_category = grouped.sort_values(by='Score', ascending=False).iloc[0]
            recommendations[feature] = {
                'Category': top_category[feature],
                'Average Time Spent': round(top_category['Time Spent'], 2),
                'Average Rating': round(top_category['Ratings'], 2)
            }

    return recommendations

# Streamlit app
def main():
    st.title("Category-Based Recommendation System")

    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)

            # Add placeholder values if necessary
            if 'Time Spent' not in df.columns:
                df['Time Spent'] = np.random.uniform(1, 5, len(df))
            if 'Ratings' not in df.columns:
                df['Ratings'] = np.random.uniform(1, 5, len(df))

            st.sidebar.success("File successfully uploaded!")

            st.sidebar.header("Dataset Preview")
            if st.sidebar.checkbox("Show Dataset"):
                st.write(df.head())

            st.sidebar.header("Show Time Spent and Ratings")
            if st.sidebar.checkbox("Show Calculated Columns"):
                st.write(df[['Time Spent', 'Ratings']])

            if st.sidebar.button("Generate Recommendations"):
                st.subheader("Top Recommended Categories")
                recommendations = recommend_categories(df)
                if isinstance(recommendations, str):  # If it's an error message
                    st.write(recommendations)
                else:
                    for feature, details in recommendations.items():
                        st.markdown(f"<h3 style='color: #4CAF50;'>{feature}:</h3>", unsafe_allow_html=True)
                        st.markdown(
                            f"<div style='background-color: #f9f9f9; padding: 10px; border-radius: 5px; margin-bottom: 10px;'>"
                            f"<b>Category:</b> {details['Category']}<br>"
                            f"<b>Average Time Spent:</b> {details['Average Time Spent']} hours<br>"
                            f"<b>Average Rating:</b> {details['Average Rating']} ⭐</div>",
                            unsafe_allow_html=True
                        )

                st.balloons()  # Add balloons animation for better UX
        except Exception as e:
            st.error(f"Error reading file: {e}")
    else:
        st.info("Please upload a CSV file to proceed.")

if __name__ == "__main__":
    main()
