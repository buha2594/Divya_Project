
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
# Function to create a database connection
def get_connection():
    return pymysql.connect(
        host='127.0.0.1',       
        user='root',            
        password='Bugha2594@',  
        database='test'         
    )

# SQL Query for eBooks vs Physical Books availability
def get_ebooks_vs_physical():
    query = """
    SELECT  isEbook, COUNT(*) AS Total_Books
    FROM books GROUP BY isEbook;
    """
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# SQL Query to find the Publisher with the Most Books Published
def get_publisher_most_books():
    query = """
    SELECT Publisher FROM
        (
         SELECT Publisher,COUNT(*) AS TOTAL FROM books WHERE Publisher IS NOT NULL GROUP BY Publisher ORDER BY TOTAL DESC
        ) AS PUB LIMIT 1;
    """
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# SQL Query to Identify the Publisher with the Highest Average Rating
def publisher_high_avg_rating():
    query="""
    SELECT Publisher, AVG(averageRating) AS AvgRating
    FROM books
    WHERE Publisher IS NOT NULL AND averageRating IS NOT NULL
    GROUP BY Publisher
    ORDER BY AvgRating DESC
    LIMIT 1;
"""
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

#SQL Query to Get the Top 5 Most Expensive Books by Retail Price
def top_expensiv_books():
    query="""
    SELECT DISTINCT book_title,amount_retailPrice
    FROM books
    ORDER BY amount_retailPrice DESC limit 5;
    """
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

#SQL Query to Find Books Published After 2010 with at Least 500 Pages
def publish_2010():
    query="""
    SELECT book_title From BOOKS WHERE year1>'2010' AND pageCount>=500;
    """
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df
#SQL Query to List Books with Discounts Greater than 20%
def books_discount():
    query="""
    SELECT book_title FROM books
    WHERE ((amount_listPrice - amount_retailPrice) / amount_listPrice) * 100 > 20;
    """
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df
#SQL Query to Find the Average Page Count for eBooks vs Physical Books
def avg_pagecount():
    query="""
    SELECT isEbook,AVG(pageCount) FROM books group by isEbook;
    """
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df

#SQL Query to List Publishers with More than 10 Books
def Publishers_Books():
    query="""
    SELECT Publisher, COUNT(*) AS total_books FROM books
    WHERE Publisher IS NOT NULL GROUP BY Publisher HAVING COUNT(*) > 10
    ORDER BY total_books DESC;
"""
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

#SQL Query to Find the Average Page Count for Each Category
def avg_pagecount():
    query="""
    SELECT categories, AVG(pageCount) from books group by categories;
    """
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df

#SQL Query to Retrieve Books with More than 3 Authors
def three_authors():
    query="""
    select book_title,book_authors from books
    WHERE LENGTH(book_authors) - LENGTH(REPLACE(book_authors, ',', '')) + 1 > 3;
    """
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df
#SQL Query Books with Ratings Count Greater Than the Average
def avg_ratings():
    query="""
    select distinct book_title from books where ratingsCount >averageRating;
    """
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df
#SQL Query to Books with the Same Author Published in the Same Year
def same_Authors():
    query="""
    SELECT b1.book_title
    FROM books b1
    JOIN books b2
    ON b1.book_authors = b2.book_authors
    AND b1.year1 = b2.year1
    AND b1.book_id <> b2.book_id
    ORDER BY b1.book_authors, b1.year1;
"""
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df

#SQL Query to Year with the Highest Average Book Price
def highest_avg():
    query="""
    SELECT year1, AVG(amount_retailPrice) AS avg_price
    FROM books
    GROUP BY year1
    ORDER BY avg_price DESC
    LIMIT 1;
"""
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df

#SQL Query to Count Authors Who Published 3 Consecutive Years
def consecutive_years():
    query="""
    SELECT DISTINCT t1.book_authors
    FROM books t1
    JOIN books t2 ON t1.book_authors = t2.book_authors AND t1.year1 = t2.year1 + 1
    JOIN books t3 ON t1.book_authors = t3.book_authors AND t1.year1 = t3.year1 + 2
    WHERE t1.book_authors IS NOT NULL;
    """
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df
#Create a query to find the average amount_retailPrice of eBooks and physical books. Return a single result set with columns for avg_ebook_price and avg_physical_price. Ensure to handle cases where either category may have no entries.
def isbooks_avg():
    query="""SELECT  isEbook, avg(amount_retailPrice) AS avg_ebook_price
    FROM books GROUP BY isEbook;"""
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df

#Create a SQL query that determines which publisher has the highest average rating among its books, but only for publishers that have published more than 10 books. Return the publisher, average_rating, and the number of books published.
def avg_publisher_ratings():
    query="""
    WITH PublisherStats AS (
    SELECT 
        publisher,
        COUNT(*) AS book_count,
        AVG(averageRating) AS avg_rating
    FROM books
    WHERE averageRating IS NOT NULL AND publisher IS NOT NULL
    GROUP BY publisher
    HAVING COUNT(*) > 10
)
    SELECT 
        publisher,
        avg_rating,
        book_count
    FROM PublisherStats
    ORDER BY avg_rating DESC
    LIMIT 1;
"""
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df

#Sql query to Find the Top 3 Authors with the Most Book
def top3_authors():
    query="""SELECT book_authors, COUNT(*) AS total_books FROM books
    WHERE book_authors IS NOT NULL AND book_authors <> ''
    GROUP BY book_authors
    ORDER BY total_books DESC
    LIMIT 3;"""
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df

#sql query to Write a SQL query to find authors who have published books in the same year 
# but under different publishers. Return the authors, year, and the COUNT of books they published in that year.
def publish_Sameyear():
    query="""
    SELECT 
    ba.book_authors AS author, 
    ba.year1 AS year, 
    COUNT(*) AS book_count
    FROM  books ba
    JOIN   books bb
    ON  ba.book_authors = bb.book_authors 
    AND ba.year1 = bb.year1 
    AND ba.Publisher <> bb.Publisher
    WHERE   ba.book_authors IS NOT NULL 
    AND ba.year1 IS NOT NULL
    GROUP BY  ba.book_authors, ba.year1
    ORDER BY  book_count DESC;"""
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df

#Write a SQL query to identify books that have an averageRating that is more than two standard deviations away from the average rating of all books. Return the title, averageRating, and ratingsCount for these outliers.
def avgrating_stddev():
    query="""WITH BookStats AS (
    SELECT
    book_title,
    averageRating,
    ratingsCount,
    AVG(averageRating) OVER () AS avg_rating,
    STDDEV(averageRating) OVER () AS stddev_rating
    FROM  books
    )
    SELECT
    book_title,
    averageRating,
    ratingsCount
    FROM BookStats
    WHERE ABS(averageRating - avg_rating) > 2 * stddev_rating;
"""
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df
# Streamlit app interface
def main():
    st.title("SQL Query Results")

    query_option = st.selectbox("Select Query", 
                                ["eBooks vs Physical Books Availability", 
                                 "Publisher with Most Books Published",
                                 "Identify the Publisher with the Highest Average Rating",
                                 "Get the Top 5 Most Expensive Books by Retail Price",
                                 "Find Books Published After 2010 with at Least 500 Pages",
                                 "List Books with Discounts Greater than 20%",
                                 "Find the Average Page Count for eBooks vs Physical Books",
                                 "List Publishers with More than 10 Books",
                                 "Find the Average Page Count for Each Category",
                                 "To Retrieve Books with More than 3 Authors",
                                 "Books with Ratings Count Greater Than the Average",
                                 "Books with the Same Author Published in the Same Year",
                                 "Year with the Highest Average Book Price",
                                 "Count Authors Who Published 3 Consecutive Years",
                                 "Create a query to find the average amount_retailPrice of eBooks and physical books. Return a single result set with columns for avg_ebook_price and avg_physical_price. Ensure to handle cases where either category may have no entries.",
                                 "Create a SQL query that determines which publisher has the highest average rating among its books, but only for publishers that have published more than 10 books. Return the publisher, average_rating, and the number of books published.",
                                 "Find the Top 3 Authors with the Most Books",
                                 "Write a SQL query to find authors who have published books in the same year but under different publishers. Return the authors, year, and the COUNT of books they published in that year.",
                                 "Write a SQL query to identify books that have an averageRating that is more than two standard deviations away from the average rating of all books. Return the title, averageRating, and ratingsCount for these outliers."])
                                 

    if query_option == "eBooks vs Physical Books Availability":
        result = get_ebooks_vs_physical()
        st.write(result)

    elif query_option == "Publisher with Most Books Published":
        result = get_publisher_most_books()
        st.write(result)
    elif query_option == "Identify the Publisher with the Highest Average Rating":
        result = publisher_high_avg_rating()
        st.write(result)
    elif query_option == "Get the Top 5 Most Expensive Books by Retail Price":
        result = top_expensiv_books()
        st.write(result)
    elif query_option == "Find Books Published After 2010 with at Least 500 Pages":
        result = publish_2010()
        st.write(result)
    elif query_option == "List Books with Discounts Greater than 20%":
        result = books_discount()
        st.write(result)
    elif query_option == "Find the Average Page Count for eBooks vs Physical Books":
        result = avg_pagecount()
        st.write(result)
    elif query_option == "List Publishers with More than 10 Books":
        result = Publishers_Books()
        st.write(result)
    elif query_option == "Find the Average Page Count for Each Category":
        result = avg_pagecount()
        st.write(result)
    elif query_option == "To Retrieve Books with More than 3 Authors":
        result = three_authors()
        st.write(result)
    elif query_option == "Books with Ratings Count Greater Than the Average":
        result = avg_ratings()
        st.write(result)
    elif query_option == "Books with the Same Author Published in the Same Year":
        result = same_Authors()
        st.write(result)
    elif query_option == "Year with the Highest Average Book Price":
        result = highest_avg()
        st.write(result)
    elif query_option == "Count Authors Who Published 3 Consecutive Years":
        result = consecutive_years()
        st.write(result)
    elif query_option == "Create a query to find the average amount_retailPrice of eBooks and physical books. Return a single result set with columns for avg_ebook_price and avg_physical_price. Ensure to handle cases where either category may have no entries.":
        result = isbooks_avg()
        st.write(result)
    elif query_option =="Create a SQL query that determines which publisher has the highest average rating among its books, but only for publishers that have published more than 10 books. Return the publisher, average_rating, and the number of books published.":
        result = avg_publisher_ratings()
        st.write(result)
    elif query_option =="Find the Top 3 Authors with the Most Books":
        result = top3_authors()
        st.write(result)
    elif query_option =="Write a SQL query to find authors who have published books in the same year but under different publishers. Return the authors, year, and the COUNT of books they published in that year.":
        result = publish_Sameyear()
        st.write(result)
    elif query_option =="Write a SQL query to identify books that have an averageRating that is more than two standard deviations away from the average rating of all books. Return the title, averageRating, and ratingsCount for these outliers.":
        result = avgrating_stddev()
        st.write(result)
set_bg_hack_url()
if __name__ == '__main__':
    main()
