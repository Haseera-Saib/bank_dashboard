import streamlit as st
import pandas as pd 
st.header('Job Details')
data=pd.read_csv('/workspaces/bank_dashboard/mentornow/bank.csv')
a=data['job'].unique()
option=st.selectbox('Select the Job',(a))

df=data[data['job']==option]
st.write(df)

av=df['age'].mean()
r=round(av,2)
#st.write(round(av,2))
st.metric(label='Age',value=r, delta=10)