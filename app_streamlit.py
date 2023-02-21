# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 02:05:12 2023

@author: megha
"""



#from flask import Flask, request, jsonify, render_template
import pickle
import streamlit as st
#import numpy as np



model_pkl = pickle.load(open('final.pkl', 'rb'))


def welcome():
    return " Welcome All"


def predict(count_in_your_room,hotel_star_rating):
    '''
   To get values from HTML user as input
    '''
    #int_ft = [int(x) for x in request.form.values()]
    #print(int_ft)
    #final_ft = [np.array(int_ft)]
    #print(final_ft)
    final_prediction = model_pkl.predict([[count_in_your_room,hotel_star_rating]])
    print(final_prediction)
  
   
    return final_prediction

    
   
    
def main():
    st.title("Make my trip review")
    html_temp = """
    <div style="background-color:tomato;padding:10px"
    <h2 style="color:white;text-align:center;">Streamlit Make my trip Review Application </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    count_in_your_room = st.text_input("Facilities","Type Here")
    hotel_star_rating = st.text_input("Hotel Rating","Type Here")
    result=""
    if st.button("Predict"):
        result=predict(count_in_your_room,hotel_star_rating)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Build with Streamlit")
        
        
if __name__ == "__main__":
    main()