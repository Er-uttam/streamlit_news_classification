import streamlit as st
import pandas as pd
import pickle as pk
# title 
st.title('NEWS classification')



# open the file in a binary mode
with open('LogisticRegression.pickle','rb') as file:
# call the load file to 
    model =  pk.load(file)

#form
news = st.text_area("Enter News ")

if st.button("Submit"):
    df = pd.DataFrame({
    'news':[news]
})
    result = model.predict(df['news'])
    st.write("The category is :",result)