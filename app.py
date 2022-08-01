import streamlit as st
import sqlite3



conn = sqlite3.connect('data.db', check_same_thread = False)
cur = conn.cursor()

def form():
    st.subheader("윤아의 독서장 :heart:")
    with st.form(key="Info Form", clear_on_submit=True):
        bookname = st.text_input("Enter the book name : ")
        summary = st.text_area("Summarize the content of the book : ")
        date = st.date_input("Enter the date : ")
        submit = st.form_submit_button(label="Submit")


        if bookname != "" and summary != "" and submit == True:
            addData(bookname, summary, date)
            st.success ("Success!!")
        
        elif (bookname == "" or summary == "") and submit == True:
            st.write("내용을 입력하세요!!")

def addData(a, b, c):
    # cur.execute("""CREATE TABLE IF NOT EXISTS MY_BOOK(id integer primary key autoincrement, BOOKNAME TEXT(50), SUMMARY TEXT(500), DATE TEXT(20));""")
    cur.execute("""CREATE TABLE IF NOT EXISTS MY_BOOK(BOOKNAME TEXT(50), SUMMARY TEXT(500), DATE TEXT(20));""")

    cur.execute("INSERT INTO MY_BOOK VALUES (?, ?, ?)", (a, b, c))
    conn.commit()

def get_book_list():
    book_list = []
    cur.execute("SELECT BOOKNAME FROM MY_BOOK")
    rows = cur.fetchall()
    for i in rows:
        book_list.append(i[0])
    print(book_list)
    return book_list    



if __name__ == "__main__":
    form()

    lst = get_book_list()
    st.write(lst)


