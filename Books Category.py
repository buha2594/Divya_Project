import streamlit as st
import pymysql
import pandas as pd

##background image
def set_bg_hack_url():

    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url('https://img.freepik.com/free-photo/abstract-brown-gradient-well-used-as-background-product-display_1258-55303.jpg?t=st=1737216925~exp=1737220525~hmac=c5c688f17578d5075cacd6a4eb7eec3aca05c05d4d406c2787130133242c683a&w=1060');
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
set_bg_hack_url()

# Function to create a database connection
def get_connection():
    return pymysql.connect(
        host='127.0.0.1',       
        user='root',            
        password='Bugha2594@',  
        database='test'         
    )
def get_books_by_keyword(keyword):
    query = """
    SELECT book_title, book_authors 
    FROM books 
    WHERE book_title LIKE %s;
    """
    conn = get_connection()
    # Use parameterized query to prevent SQL injection
    df = pd.read_sql(query, conn, params=(f"%{keyword}%",))
    conn.close()
    return df

# Main Streamlit app
def main():
    st.title("Books with a Specific Keyword in the Title")
    
    # User input
    user_input = st.text_input("Enter the keyword:")
    
    # Submit button
    if st.button("Submit"):
        if user_input:
            # Fetch the data from the database
            result_df = get_books_by_keyword(user_input)
            
            if not result_df.empty:
                # Display the results in a table
                st.write("Search Results:")
                st.dataframe(result_df)
            else:
                st.write("No books found with the given keyword.")
        else:
            st.write("Please enter a keyword before submitting.")

if __name__ == "__main__":
    main()