# Hotel_review


ML End-to-End project


It is an end-to-end project, where 

1.Data Exploration + Data Wrangling
2.Picking a model
3.Deploying the whole progess onto a presentaion mode(Flask)


Prerequisites

Pandas,numpy,matplotlib,seaborn
Python and Flask installed


Project Structure


1.model.py 

This code contains the step-by-step procedure of predicting the mmt_review(make my trip review)
using the makemytrip.csv

2.app.py

This contains Flask APIs that receives hotel details through GUI or API calls, 
computes the precited value based on our model and returns it.

3.request.py
 
This uses requests module to call APIs already defined in app.py and dispalys the returned value.

4.templates

This folder contains the HTML template to allow user to 
enter hotel details and display the predicted make my trip review.

