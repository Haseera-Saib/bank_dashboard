import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.header('Job Details')
data=pd.read_csv('/workspaces/bank_dashboard/mentornow/bank.csv')
a=data['job'].unique()
option=st.selectbox('Select the Job',(a))

ct=st.container(border=True)

col1,col2,col3=ct.columns(3)

ctn=st.container(border=True)

c1,c2=ctn.columns(2)

ctnr=st.container(border=True)
df=data[data['job']==option]
ctnr.write(df)

with col1:

    av=df['age'].mean()
    r=round(av,2)
#st.write(round(av,2))
    st.metric(label='Age',value=r,)

with col2:

    b=df['marital'].value_counts()['married']
    st.metric(label='Married Count', value=b)

with col3:

    ave=df['balance'].mean()
    rr=round(ave,2)
#st.write(round(av,2))
    st.metric(label='Acoount Balance',value=rr,)




c1.header('First Chart')
fig = px.density_heatmap(df, x="marital", y="age", template="seaborn")
c1.plotly_chart(fig)

c2.header('Second Chart')
fig2=px.histogram(df, x="age")
c2.plotly_chart(fig2)