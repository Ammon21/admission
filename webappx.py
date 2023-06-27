import streamlit as st
import numpy as np
import pandas as pd
import pickle
import math

st.header('Admission Office AI Test System')

name = st.text_input("Whats your name?")

age = st.slider('How old are you?', 10, 20, 1)

option = st.selectbox('Gender',
    ('Male', 'Female'))

sex = 0

if option == 'Female':
     sex = 0
else:
     sex = 1

sex     

pob = st.selectbox('Place of Birth',
    ('Ethiopia', 'Foriegn soil'))

place = 0

if pob == 'Ethiopia':
     place = 0
else:
     place = 1

place

tutor = st.selectbox('Do you take any makeup class or tutoring',
    ('yes', 'no'))


makeup = 0

if tutor == 'yes':
     makeup = 1
else:
     makeup = 0

makeup

grade = st.slider('what grade are you in?' , 5, 12, 1)

mothertongue = st.selectbox('what is your first language (mother tongue)',
    ('ethiopian language', 'foriegn language'))

mother = 0

if mothertongue == 'ethiopian language':
     mother = 0
else:
     mother = 1

mother

admission = st.selectbox('Admission type inquiry',
    ('paid', 'scholarship'))

adm = 0

if admission == 'paid':
     adm = 0
else:
     adm = 1

adm   

math = st.number_input('What is your maths grade of the previous semester?')

english = st.number_input('What is your english grade of the previous semester?')

birth = st.radio(
    "What\'s your birth order",
    ('First child', 'middle child', 'last child'))

fx = 0
fm = 0
fl = 0


if birth == 'First child':
    fx = 1
elif birth == 'middle child':
    fm=1
else:
    fl=1    

st.write(fx,fm,fl)      

parenting = st.radio(
    "How do you describe your relationship with your parents (Parrenting Style)",
    ('Authoritative', 'Authoritarian', 'Permissive', 'Uninvolved'))

avx = 0
atx = 0
per = 0

if   parenting == 'Authoritative':
     avx = 1
elif parenting == 'Authoritarian':
     atx = 1
elif parenting == 'Permissive':
     per = 1  

st.write(avx,atx,per)       

transport = st.selectbox('What is your transport type',
    ('Private Car', 'Public Tranportation', 'Service', 'on Foot'))

private = 0
public = 0
service = 0

if   transport == 'Private Car':
     private = 1
elif transport == 'Public Tranportation':
     public = 1
elif transport == 'Service':
     service = 1  

st.write(private,public,service)  




guardian = st.radio(
    "Do you live with both parents",
    ('yes', 'no'))

both = 0
single = 0

if   guardian == 'yes':
     both = 1
elif guardian == 'no':
     single = 1

st.write(both,single)


conductx = st.radio(
    "Conduct at previous school",
    ('A', 'B', 'C'))

conduct = 0

if conductx == 'A':
     conduct = 3
elif conductx == 'B':
     conduct = 2
else:
     conduct = 1

st.write(conduct)  


model = pickle.load(open('new.pkl', 'rb'))


x = model.predict([[conduct, age, sex, place, makeup, grade, adm,mother,math,english, fx,fl,fm,atx,avx,per,private,public,service,both,single]])

message = name + "\'s potential GPA in this academy will be approximately " + str(int(x[0]))

st.header(message)



