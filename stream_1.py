import pandas as pd
import streamlit as st
import pickle as pkl
import os
os.chdir(r"C:\Users\249835\Desktop\Project Final\Project")
#########################################################
image = '''
<style>
[data-testid='stAppViewContainer']{
background-image: url('https://sm.mashable.com/t/mashable_in/photo/default/shutterstock-735045577_y218.1248.jpg');
background-size: cover;
}
'''
st.markdown(image, unsafe_allow_html=True)






##########################################################################
df=pd.read_csv("telcom_new1.csv")

# Title of the page
st.title("Telecom Customer Churn Prediction")

# Write method is used to write a line below the heading
st.write("This app is based on 19 inputs that predict whether a customer will Churn or not? Using this app, a Telecom Company can identify specific customer segments; that will Churn.")
st.write("Please use the following form to get started!")
#st.markdown('<p class="big-font">(NOTE: For convinience, usual values are pre-selected in the form.)</p>', unsafe_allow_html=True)


#Select customer gender
st.subheader("Select Customer's Gender")
selected_Gender = st.radio("Enter your Gender", ['Female', 'Male'],index =0)
st.write("Selected Gender:", selected_Gender)

def encode_Gender(selected_item):
    dict_gender = {'Female':0, 'Male':1}
    return dict_gender.get(selected_item, 'No info available')

selected_Gender = encode_Gender(selected_Gender) 

#Select Customer is SeniorCitizen

st.subheader("Select Customer is SeniorCitizen")
selected_SeniorCitizen = st.radio("Select SeniorCitizen", ['Yes', 'No'],index =0)
st.write("Selected SeniorCitizen:", selected_SeniorCitizen)

def encode_SeniorCitizen(selected_item):
    dict_SeniorCitizen = {'Yes':1, 'No':0}
    return dict_SeniorCitizen.get(selected_item, 'No info available')

selected_SeniorCitizen = encode_SeniorCitizen(selected_SeniorCitizen) 
#################################

st.subheader("Select Customer having Partner")
selected_Partner = st.radio("Select Partner", ['Yes', 'No'],index =0)
st.write("Selected Partner:", selected_Partner)

def encode_Partner(selected_item):
    dict_Partner = {'Yes':1, 'No':0}
    return dict_Partner.get(selected_item, 'No info available')

selected_Partner = encode_Partner(selected_Partner)


##########################
st.subheader("Select Customer are Dependent")
selected_Dependents = st.radio("Select Dependents", ['Yes', 'No'],index =0)
st.write("Selected Dependents:", selected_Dependents)

def encode_Dependents(selected_item):
    dict_Dependents = {'Yes':1, 'No':0}
    return dict_Dependents.get(selected_item, 'No info available')

selected_Dependents = encode_Partner(selected_Dependents)
#################################################
st.title("Select Customer Tenure")
st.write("Enter a value within the range of 0 to 72")

tenure = st.slider("Select a value", 0, 72)

st.write("You selected:", tenure)

##########################################
st.subheader("Select Customer having PhoneService")
selected_PhoneService = st.radio("Select PhoneService", ['Yes', 'No'],index =0)
st.write("Selected PhoneService:", selected_PhoneService)

def encode_PhoneService(selected_item):
    dict_PhoneService = {'Yes':1, 'No':0}
    return dict_PhoneService.get(selected_item, 'No info available')

selected_PhoneService = encode_PhoneService(selected_PhoneService)
#######################################################################
st.subheader("Select Customer having MultipleLines")
selected_MultipleLines = st.radio("Select MultipleLines", ['No phone service', 'No', 'Yes'],index =0)
st.write("Selected MultipleLines:", selected_MultipleLines)

def encode_MultipleLines(selected_item):
    dict_MultipleLines = {'No phone service':2, 'No':0, 'Yes':1}
    return dict_MultipleLines.get(selected_item, 'No info available')

selected_MultipleLines = encode_MultipleLines(selected_MultipleLines)
#######################################################
st.subheader("Select Customer having InternetService")
selected_InternetService = st.radio("Select InternetService", ['DSL', 'Fiber optic', 'No'],index =0)
st.write("Selected InternetService:", selected_InternetService)

def encode_InternetService(selected_item):
    dict_InternetService = {'DSL':0, 'Fiber optic':1, 'No':2}
    return dict_InternetService.get(selected_item, 'No info available')

selected_InternetService = encode_InternetService(selected_InternetService)
####################################################
st.subheader("Select Customer having OnlineSecurity")
selected_OnlineSecurity = st.radio("Select OnlineSecurity", ['No', 'Yes', 'No internet service'],index =0)
st.write("Selected OnlineSecurity:", selected_OnlineSecurity)

def encode_OnlineSecurity(selected_item):
    dict_OnlineSecurity = {'No':0, 'Yes':1, 'No internet service':2}
    return dict_OnlineSecurity.get(selected_item, 'No info available')

selected_OnlineSecurity = encode_OnlineSecurity(selected_OnlineSecurity)
#################################################
st.subheader("Select Customer having OnlineBackup")
selected_OnlineBackup = st.radio("Select OnlineBackup", ['Yes', 'No', 'No internet service' ],index =0)
st.write("Selected OnlineBackup:", selected_OnlineBackup)

def encode_OnlineBackup(selected_item):
    dict_OnlineBackup = {'Yes':1, 'No':0, 'No internet service':2 }
    return dict_OnlineBackup.get(selected_item, 'No info available')

selected_OnlineBackup = encode_OnlineBackup(selected_OnlineBackup)
##########################################################
st.subheader("Select Customer having DeviceProtection")
selected_DeviceProtection = st.radio("Select DeviceProtection", ['No', 'Yes', 'No internet service'  ],index =0)
st.write("Selected DeviceProtection:", selected_DeviceProtection)

def encode_DeviceProtection(selected_item):
    dict_DeviceProtection = {'No':0, 'Yes':1, 'No internet service':2  }
    return dict_DeviceProtection.get(selected_item, 'No info available')

selected_DeviceProtection = encode_DeviceProtection(selected_DeviceProtection)
##########################################################
st.subheader("Select Customer having TechSupport")
selected_TechSupport = st.radio("Select TechSupport", ['No', 'Yes', 'No internet service'  ],index =0)
st.write("Selected TechSupport:", selected_DeviceProtection)

def encode_TechSupport(selected_item):
    dict_TechSupport = {'No':0, 'Yes':1, 'No internet service':2  }
    return dict_TechSupport.get(selected_item, 'No info available')

selected_TechSupport = encode_TechSupport(selected_TechSupport)
###################################################
st.subheader("Select Customer having StreamingTV")
selected_StreamingTV = st.radio("Select StreamingTV", ['No', 'Yes', 'No internet service'  ],index =0)
st.write("Selected StreamingTV:", selected_StreamingTV)

def encode_StreamingTV(selected_item):
    dict_StreamingTV = {'No':0, 'Yes':1, 'No internet service':2  }
    return dict_StreamingTV.get(selected_item, 'No info available')

selected_StreamingTV = encode_StreamingTV(selected_StreamingTV)
#########################################
st.subheader("Select Customer having StreamingMovies")
selected_StreamingMovies = st.radio("Select StreamingMovies", ['No', 'Yes', 'No internet service'  ],index =0)
st.write("Selected StreamingMovies:", selected_StreamingMovies)

def encode_StreamingMovies(selected_item):
    dict_StreamingMovies = {'No':0, 'Yes':1, 'No internet service':2  }
    return dict_StreamingMovies.get(selected_item, 'No info available')

selected_StreamingMovies = encode_StreamingMovies(selected_StreamingMovies)
###########################################
st.subheader("Select Customer having Contract")
selected_Contract = st.radio("Select Contract", ['Month-to-month', 'One year', 'Two year'],index =0)
st.write("Selected Contract:", selected_Contract)

def encode_Contract(selected_item):
    dict_Contract = {'Month-to-month':0, 'One year':1, 'Two year':2}
    return dict_Contract.get(selected_item, 'No info available')

selected_Contract = encode_Contract(selected_Contract)
#######################################################
st.subheader("Select Customer having PaperlessBilling")
selected_PaperlessBilling = st.radio("Select PaperlessBilling", ['Yes', 'No'  ],index =0)
st.write("Selected PaperlessBilling:", selected_PaperlessBilling)

def encode_PaperlessBilling(selected_item):
    dict_PaperlessBilling = {'Yes':1, 'No':0  }
    return dict_PaperlessBilling.get(selected_item, 'No info available')

selected_PaperlessBilling = encode_PaperlessBilling(selected_PaperlessBilling)

########################################
st.subheader("Select Customer having PaymentMethod")
selected_PaymentMethod = st.radio("Select PaymentMethod", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)' ],index =0)
st.write("Selected PaymentMethod:", selected_PaymentMethod)

def encode_PaymentMethod(selected_item):
    dict_PaymentMethod = {'Electronic check':0, 'Mailed check':1, 'Bank transfer (automatic)':2, 'Credit card (automatic)':3 }
    return dict_PaymentMethod.get(selected_item, 'No info available')

selected_PaymentMethod = encode_PaymentMethod(selected_PaymentMethod)
#####################################################

# Selecting MonthlyCharges
st.subheader("Select Customer's MonthlyCharges")
selected_MonthlyCharges = st.number_input("Enter your MonthlyCharges: ", step= 0.1)
st.write("Selected MonthlyCharges:", selected_MonthlyCharges)

#####################################
# Selecting TotalCharges
st.subheader("Select Customer's TotalCharges")
selected_TotalCharges = st.number_input("Enter your TotalCharges: ", step= 0.1)
st.write("Selected TotalCharges:", selected_TotalCharges)

###################################

st.subheader("Now, we will predict whether customer will Churn or not.")

clsr=pkl.load(open('Mavi','rb'))


predictionUsingRF= clsr.predict([[selected_Gender,selected_SeniorCitizen,selected_Partner,selected_Dependents,tenure,selected_PhoneService,
                                     selected_MultipleLines,selected_InternetService,selected_OnlineSecurity,
                                     selected_OnlineBackup,selected_DeviceProtection,selected_TechSupport,
                                     selected_StreamingTV,selected_StreamingMovies,selected_Contract,
                                       selected_PaperlessBilling,selected_PaymentMethod,
                                       selected_MonthlyCharges,selected_TotalCharges
                                  ]])
proba=round((clsr.predict_proba([[selected_Gender,selected_SeniorCitizen,selected_Partner,selected_Dependents,tenure,selected_PhoneService,
                                     selected_MultipleLines,selected_InternetService,selected_OnlineSecurity,
                                     selected_OnlineBackup,selected_DeviceProtection,selected_TechSupport,
                                     selected_StreamingTV,selected_StreamingMovies,selected_Contract,
                                       selected_PaperlessBilling,selected_PaymentMethod,
                                       selected_MonthlyCharges,selected_TotalCharges
                                  ]])[0][1])*100,2)

predict_button = st.button('Predict using Voting Classifier')

if predict_button:
    if(predictionUsingRF > 0.5):
        st.success('This customer will  Churn with probability percentage {}% '.format(proba))
    else:
        st.success('This customer will NOT Churn with probability percentage {}%'.format(proba))

