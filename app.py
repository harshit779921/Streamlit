import streamlit as st
import pandas as pd 
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np 

data = pd.read_csv("data//population.csv")
x = np.array(data['Year']).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(data['population']))


st.title("Population Predictor")
st.image("data//worldpop.jpg",width = 800)
nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])
if nav == "Home":
    
    if st.checkbox("Show Table"):
        st.table(data)
    
    graph = st.selectbox("What kind of Graph ? ",["Non-Interactive","Interactive"])

    val = st.slider("Filter data using years",1970,2010)
    if graph == "Non-Interactive":
        plt.figure(figsize = (10,8))
        plt.scatter(data["Year"],data["population"])
        plt.ylim(0)
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.tight_layout()
        st.pyplot()
    if graph == "Interactive":
        layout =go.Layout(
            xaxis = dict(range=[1970,2010]),
            yaxis = dict(range =[3500000000,7000000000])
        )
        fig = go.Figure(data=go.Scatter(x=data["Year"], y=data["population"], mode='markers'),layout = layout)
        st.plotly_chart(fig)
    
if nav == "Prediction":
    st.header("Know the Population")
    val = st.number_input("Enter the year",2011,2040,step =1)
    val = np.array(val).reshape(1,-1)
    pred =lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your predicted population is {round(pred)}(in Billion)")
        st.balloons()

if nav == "Contribute":
    st.header("Contribute to our dataset")
    ex = st.number_input("Enter the population",1970,2010)
    sal = st.number_input("Enter the population",3500000000,1000000000,step = 1)
    if st.button("submit"):
        to_add = {"population":[ex],"population":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("data//population.csv",mode='a',header = False,index= False)
        st.success("Submitted")
        
