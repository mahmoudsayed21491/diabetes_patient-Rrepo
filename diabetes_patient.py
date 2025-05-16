import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
st.set_page_config(layout= 'wide', page_title= 'diabetes_patient')
st.markdown("<h1 style='text-align: center; color: white;'>diabetes dataset with Analysis</h1>", unsafe_allow_html=True)
st.image('https://img.freepik.com/free-vector/diabetes-flat-composition-medical-with-patient-symptoms-complications-blood-sugar-meter-treatments-medication_1284-28998.jpg')
df = pd.read_csv('E:/data science & python/mid project mahmoud sayed/cleand_data.csv',index_col=0)
page = st.sidebar.radio('Pages', ['Introduction', 'Analysis Questions', 'Reporting'])
if page == 'Introduction':

    st.dataframe(df.head())

    st.header('diabetes_patient Description')

    st.write('''The dataset contains 464003 entries and 13 columns. Here's a summary of the columns:

    Visit_Date: The date on which the patient visited the medical facility (past 6 years).
    Patient_ID:  A unique identifier assigned to each patient.
    Age: Age of the patient at the time of the visit (0–100 years).
    Gender: The gender of the patient ('Male', 'Female', or possibly other identifiers).
    Diagnosis: Diabetes-related diagnosis (Type 1, Type 2, Prediabetes, Gestational, or missing).
    Has_Insurance: Indicates whether the patient has health insurance coverage (e.g., Yes/No or 1/0).
    Total_Cost: The total cost incurred for the patient's visit, including all services.
    Area: Geographical area or region where the patient resides or where the facility is located
      within the emirate (e.g., Al Ain, Palm Jumeirah).
    Registration duration: Time spent during registration (in minutes).
    Nursing duration: Time spent with nursing staff (in minutes).
    Laboratory duration: Time spent in the laboratory (in minutes).
    Consultation duration: Time spent in consultation (in minutes).
    Pharmacy duration: Time spent at the pharmacy (in minutes)
    Year :Year in which the patient visit took place (extracted from Visit_Date ).''')

elif page == 'Analysis Questions':

    st.header(' Q1 What is the percentage of Diagnosis ?')
    st.plotly_chart(px.pie(data_frame= df , names= 'Diagnosis'))
    st.write(''' Insight Q1:

Diagnosis Percentage AnalysisWhat This Metric Tells Us
The percentage of each Diagnosis shows how common each medical condition is among
all patient visits.It helps identify:
The most frequent health issues,
Potential areas for preventive care,
Resource allocation priorities.''')
    st.header('Q2 What is the percentage of Gender ?')
    st.plotly_chart(px.pie(data_frame= df , names= 'Gender'))
    st.write('''insight Q2:

 after comparing the a count   It was found that the number of male visitors was greater than the number of females and others.''')
    st.header('Q3 Does age affect the total medical cost?')
    st.plotly_chart(px.scatter(data_frame= df , x= 'Age' , y='Total_Cost'))
    st.write(''' Insight Q3:

    There is virtually no correlation between age and total medical cost in this dataset. 
             Age does not significantly impact the total cost. ''')
    st.header(' Q4 What Is The Average Total Cost Per Gender ?')
    average_total_cost_per_gender = df.groupby('Gender')['Total_Cost'].mean().sort_values(ascending= False).reset_index()
    st.plotly_chart(px.bar(average_total_cost_per_gender , x= 'Gender', y= 'Total_Cost' , labels= {'Total_Cost': 'avg total cost per gender'}, 
       title= 'average_total_cost_per_gender' , text_auto=True))
    st.write('''Insight Q4:

The average cost is nearly identical across all genders,
 indicating that gender does not influence total cost in this dataset.
     ''')
    st.header('Q5 What Is The Total Cost Per Year ?')
    total_cost_per_year = df.groupby('Year')['Total_Cost'].sum().sort_values(ascending= False).reset_index().round(2)
    st.plotly_chart(px.bar(total_cost_per_year, x= 'Year', y= 'Total_Cost' , labels= {'Total_Cost': 'total cost per year'}, 
       title= 'total cost per year' , text_auto=True))
    st.write('''Insight Q5:

Total medical costs are consistent year-over-year, hovering around 34 million AED.
     ''')
    st.header('Q6 What Is The Average Consultation Duration Per Diagnosis?')
    avg_Consultation_Duration_per_diagnosis = df.groupby('Diagnosis')['Consultation_Duration'].mean().sort_values(ascending= False).reset_index().rename(columns={'Consultation_Duration': 'Avg_Consultation_Duration'})
    st.plotly_chart(px.bar(avg_Consultation_Duration_per_diagnosis, x='Diagnosis',y='Avg_Consultation_Duration' ,
       labels= {'Consultation_Duration' : 'Average Consultation Duration'}, title= 'Average Consultation Duration per Diagnosis',
       text_auto= True) )
    st.write('''Insight Q6:

Type 3 Diabetes patients tend to have the longest consultations on average.
     ''')
    st.header('Q7 What Is The Average Total Cost Per Gender Per Diagnosis ?')
    avg_total_cost_per_area = df.groupby(['Gender', 'Diagnosis'])['Total_Cost'].mean().reset_index()
    st.plotly_chart(px.bar(avg_total_cost_per_area ,x='Diagnosis' , y='Total_Cost',
         labels= {'Total_Cost' : 'Average of Total_Cost'}, title= 'Average Total_Cost per Diagnosis per Gender',
       text_auto= True, color= 'Gender', barmode= 'group'))

    st.write('''Insight Q7:

Costs vary slightly by area and diagnosis, 
with Downtown Dubai showing consistently higher costs compared to others.
     ''')
elif page == 'Reporting':
    Gender = st.sidebar.selectbox('Gender' ,df['Gender'].unique())
    Year = st.sidebar.selectbox('Year', df['Year'].unique())
    Area = st.sidebar.selectbox('Area',df['Area'].unique())
    Diagnosis = st.sidebar.selectbox('Diagnosis', df['Diagnosis'].unique())
    df2 = df[(df['Gender']== Gender) & (df['Year'] == Year) &(df['Area']== Area) & (df['Diagnosis']==Diagnosis) ]
    st.dataframe(df2.head(50))    
