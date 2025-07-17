 
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

def to_float(val):
    try:
        return float(val)
    except:
        return np.nan

#Loading the saved models


diabetes_model = pickle.load(open('../Saved models/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('../Saved models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('../Saved models/parkinsons_model.sav','rb'))

#Sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons = ['activity','heart','person'],
                           default_index = 0)
    
    
#Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):
    
    #Page title
    st.title('Diabetes Prediction using ML')
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    #Code for prediction
    diab_diagnosis = ''
    
    #Creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        fields = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        if any(f.strip() == "" for f in fields):
            st.warning("Please enter all values for Diabetes Prediction.")
        else:
            diab_prediction = diabetes_model.predict([[to_float(Pregnancies), to_float(Glucose), to_float(BloodPressure), to_float(SkinThickness), to_float(Insulin), to_float(BMI), to_float(DiabetesPedigreeFunction), to_float(Age)]])
            if (diab_prediction[0]==1):
                diab_diagnosis = 'The person is Diabetic'
            else:
                diab_diagnosis = 'The person is Not Diabetic'
            st.success(diab_diagnosis)
    
    
    
            
#Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):
    
    #Page title
    st.title('Heart Disease Prediction using ML')
    
    age = st.number_input('Age of the Person')
    sex = st.number_input('Sex of the Person')
    cp = st.number_input('Chest pain types')
    trestbps = st.number_input('Resting Blood Pressure')
    chol = st.number_input('Serum Cholestoral in mg/dl')
    fbs = st.number_input('Fasting blood sugar > 120 mg/dl')
    restecg = st.number_input('Resting Electrocardiographic results')
    thalach = st.number_input('Maximum Heart Rate achieved')
    exang = st.number_input('Exercise Induced Angina')
    oldpeak = st.number_input('ST depression induced by exercise')
    slope = st.number_input('Slope of the peak exercise ST segment')
    ca = st.number_input('Mjor vessels colored by flourosopy')
    thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    
    #Code for prediction
    heart_diagnosis = ''
    
    #Creating a button for prediction
    
    if st.button('Heart Test Result'):
        fields = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        # If all fields are at default (0 or empty), prompt user to enter values
        if all((str(f).strip() == "" or f == 0) for f in fields):
            st.warning("Please enter all values for Heart Disease Prediction.")
        else:
            heart_prediction = heart_disease_model.predict([[to_float(age), to_float(sex), to_float(cp), to_float(trestbps), to_float(chol), to_float(fbs), to_float(restecg), to_float(thalach), to_float(exang), to_float(oldpeak), to_float(slope), to_float(ca), to_float(thal)]])
            if (heart_prediction[0]==1):
                heart_diagnosis = 'The person is suffering from Heart disease'
            else:
                heart_diagnosis = 'The person is Not suffering from Heart disease'
            st.success(heart_diagnosis)
    
    
    
#Parkinsons Prediction Page
if(selected == 'Parkinsons Prediction'):
    
    #Page title
    st.title('Parkinsons Prediction using ML')
    

    fo = st.text_input('MDVP:Fo(Hz)')
    fhi = st.text_input('MDVP:Fhi(Hz)')
    flo = st.text_input('MDVP:Flo(Hz)')
    Jitter_percent = st.text_input('MDVP:Jitter(%)')
    Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    RAP = st.text_input('MDVP:RAP')
    PPQ = st.text_input('MDVP:PPQ')
    DDP = st.text_input('Jitter:DDP')
    Shimmer = st.text_input('MDVP:Shimmer')
    Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    APQ3 = st.text_input('Shimmer:APQ3')
    APQ5 = st.text_input('Shimmer:APQ5')
    APQ = st.text_input('MDVP:APQ')
    DDA = st.text_input('Shimmer:DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')
            
            
    #Code for prediction
    parkinsons_diagnosis = ''
            
    #Creating a button for prediction
            
    if st.button('Parkinsons Test Result'):
        fields = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        if any(f.strip() == "" for f in fields):
            st.warning("Please enter all values for Parkinsons Prediction.")
        else:
            parkinsons_prediction = parkinsons_model.predict([[to_float(fo), to_float(fhi), to_float(flo), to_float(Jitter_percent), to_float(Jitter_Abs), to_float(RAP), to_float(PPQ), to_float(DDP), to_float(Shimmer), to_float(Shimmer_dB), to_float(APQ3), to_float(APQ5), to_float(APQ), to_float(DDA), to_float(NHR), to_float(HNR), to_float(RPDE), to_float(DFA), to_float(spread1), to_float(spread2), to_float(D2), to_float(PPE)]])
            if (parkinsons_prediction[0]==1):
                parkinsons_diagnosis = 'The person is suffering from Parkinsons disease'
            else:
                parkinsons_diagnosis = 'The person is Not suffering from Parkinsons disease'
            st.success(parkinsons_diagnosis)
    

st.markdown(
    """
    <hr style="margin-top: 40px; margin-bottom: 10px;">
    <div style="text-align: center; color: #444; font-size: 18px; font-weight: 600; background:rgba(255,255,255,0.7); padding: 8px 0; border-radius: 8px;">
        © NIMAL DINESH M 2025
    </div>
    """,
    unsafe_allow_html=True
) 
   
