import streamlit as st

name = st.text_input("Enter your Name: ")
fname = st.text_input("Enter your Father Name: ")
lname = st.text_input("Enter your Last Name: ")
add = st.text_area("Enter your Address: ")

classData = st.selectbox("Enter your Class: ", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

button = st.button("Done!")
if button:
    st.markdown(f"""
    Full Name : {name} {fname} {lname}\n
    address : {add}\n            
    Class : {classData}
                """)