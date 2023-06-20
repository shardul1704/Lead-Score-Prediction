from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np


def predict_conversion(model, df):
    
    predictions_data = predict_model(estimator = model, data = df, raw_score=True)
    return predictions_data
    
model = load_model('Lead_score_lightgbm_model')


st.title('Lead Score Prediction Web App')
st.write('Our web app is an intelligent tool designed to calculate lead scores\
        for potential customers based on their activity attributes and intentions.\
        By utilizing advanced machine learning techniques,\
        we have developed a model that aims to maximize profits.\
        The lead scoring process involves analyzing various customer activities,\
        such as website visits, email interactions, social media engagement, and more.\
        By considering these activities alongside their expressed intentions,\
        our model assigns a score that indicates the likelihood of a customer converting\
        into a paying customer or making a significant purchase.\
        This powerful tool empowers businesses to prioritize and focus their efforts on high-scoring leads,\
        ultimately optimizing their sales and marketing strategies to increase revenue and drive profitability.')


lead_origin = ('API','Landing Page Submission','Lead Add Form','Lead Import','Quick Add Form')
Origin = st.selectbox('Lead Origin', lead_origin)

lead_source = ('Olark Chat', 'Organic Search', 'Direct Traffic', 'Google','Referral Sites', 'Welingak Website', 'Reference', 'google','Facebook', 'blog', 'Pay per Click Ads', 'bing','Social Media', 'WeLearn', 'Click2call', 'Live Chat','welearnblog_Home', 'youtubechannel', 'testone', 'Press_Release','NC_EDM')
Source = st.selectbox('Lead Source', lead_source)

yesno = ('Yes','No')
Not_Email = st.selectbox('Do Not Email', yesno)                         

Not_Call = st.selectbox('Do Not Call', yesno)

TotalVisits = st.slider(label = 'TotalVisits', min_value = 0,
                          max_value = 300 ,
                          value = 1,
                          step = 1)
   
Total_Time_Spent = st.slider(label = 'Total Time Spent on Website(sec)', min_value = 0,
                          max_value = 2000,
                          value = 1,
                          step = 1)

Page_Views = st.slider(label = 'Page Views Per Visit', min_value = 0.00,
                          max_value = 200.00 ,
                          value = 1.00,
                          step = 0.01)

activities = ('Page Visited on Website', 'Email Opened', 'Unreachable','Converted to Lead', 'Olark Chat Conversation', 'Email Bounced','Email Link Clicked', 'Form Submitted on Website', 'Unsubscribed','Had a Phone Conversation', 'View in browser link Clicked', 'Approached upfront', 'SMS Sent', 'Visited Booth in Tradeshow','Resubscribed to emails', 'Email Received', 'Email Marked Spam')
Last_Activity = st.selectbox('Last Activity', activities)

countries = ('India', 'Russia', 'Kuwait', 'Oman', 'United Arab Emirates','United States', 'Australia', 'United Kingdom', 'Bahrain', 'Ghana','Singapore', 'Qatar', 'Saudi Arabia', 'Belgium', 'France','Sri Lanka', 'China', 'Canada', 'Netherlands', 'Sweden', 'Nigeria','Hong Kong', 'Germany', 'Asia/Pacific Region', 'Uganda', 'Kenya','Italy', 'South Africa', 'Tanzania', 'unknown', 'Malaysia','Liberia', 'Switzerland', 'Denmark', 'Philippines', 'Bangladesh','Vietnam', 'Indonesia')
Country = st.selectbox('Country', countries)

specials = ('Select', 'Business Administration', 'Media and Advertising', 'Supply Chain Management', 'IT Projects Management','Finance Management', 'Travel and Tourism','Human Resource Management', 'Marketing Management','Banking, Investment And Insurance', 'International Business','E-COMMERCE', 'Operations Management', 'Retail Management','Services Excellence', 'Hospitality Management','Rural and Agribusiness', 'Healthcare Management', 'E-Business') 
Specialization = st.selectbox('Specialization', specials)

hearhow = ('Select', 'Word Of Mouth', 'Other', 'Online Search','Multiple Sources', 'Advertisements', 'Student of SomeSchool','Email', 'Social Media', 'SMS')
Hear_About = st.selectbox('How did you hear about X Education', hearhow)

occup = ('Unemployed', 'Student', 'Working Professional','Businessman', 'Other', 'Housewife')
Current_Occupation = st.selectbox('What is your current occupation', occup)

matters = ('Better Career Prospects', 'Flexibility & Convenience','Other')
Matters_Most = st.selectbox('What matters most to you in choosing a course', matters)

Search = st.selectbox('Did you search for us?', yesno)

Magazine = st.selectbox('Did you find us in a magazine?', yesno)
                          
Newspaper_Article = st.selectbox('Did you find us in a Newspaper article?', yesno)

X_Education_Forums = st.selectbox('Did you find us in X Education forums?', yesno)

Digital_Advertisement = st.selectbox('Did you find us through digital ads?', yesno)
                          
Through_Recommendations = st.selectbox('Did you find us through recommendations?', yesno)

Receive_More_Updates = st.selectbox('Would you like to receive more updates about our courses?', yesno)

tgs = ('Interested in other courses', 'Ringing',
       'Will revert after reading the email', 'Lost to EINS',
       'In confusion whether part time or DLP', 'Busy', 'switched off',
       'in touch with EINS', 'Already a student',
       'Diploma holder (Not Eligible)', 'Graduation in progress',
       'Closed by Horizzon', 'number not provided', 'opp hangup',
       'Not doing further education', 'invalid number',
       'wrong number given', 'Interested  in full time MBA',
       'Still Thinking', 'Lost to Others',
       'Shall take in the next coming month', 'Lateral student',
       'Interested in Next batch', 'Recognition issue (DEC approval)',
       'Want to take admission but has financial problems',
       'University not recognized')
Tags = st.selectbox('Tags', tgs)

leadquality = ('Low in Relevance', 'Might be', 'Not Sure', 'Worst','High in Relevance')
Lead_Quality = st.selectbox('Lead Quality', leadquality)

Update_Supply_Chain = st.selectbox('Update me on Supply Chain Content?', yesno)

Get_updates_DM = st.selectbox('Get updates on DM Content?', yesno)

leadprofile = ('Select', 'Potential Lead', 'Other Leads', 'Lateral Student','Dual Specialization Student', 'Student of SomeSchool')
Lead_Profile = st.selectbox('Lead Profile', leadprofile)

citites = ('Select', 'Mumbai', 'Thane & Outskirts', 'Other Metro Cities','Other Cities', 'Other Cities of Maharashtra', 'Tier II Cities')
City = st.selectbox('City', citites)

activityindex = ('01.High', '02.Medium', '03.Low')
Activity_Index = st.selectbox('Asymmetrique Activity Index', activityindex)

profileindex = ('01.High', '02.Medium', '03.Low')
Profile_Index = st.selectbox('Asymmetrique Profile Index', profileindex)

Activity_Score = st.slider(label = 'Asymmetrique Activity Score', min_value = 0,
                          max_value = 20 ,
                          value = 1,
                          step = 1)

Profile_Score = st.slider(label = 'Asymmetrique Profile Score', min_value = 0,
                          max_value = 20 ,
                          value = 1,
                          step = 1)
                          
cheque = st.selectbox('Agree to pay the amount through cheque?', yesno)

Mastering_Interview = st.selectbox('A free copy of Mastering The Interview?', yesno)

notableactivity = ('Modified', 'Email Opened', 'Page Visited on Website','Email Bounced', 'Email Link Clicked', 'Unreachable','Unsubscribed', 'Had a Phone Conversation','Olark Chat Conversation', 'SMS Sent', 'Approached upfront','Resubscribed to emails', 'View in browser link Clicked','Form Submitted on Website', 'Email Received', 'Email Marked Spam')
Notable_Activity = st.selectbox('Last Notable Activity', notableactivity)

features = {'Lead Origin': lead_origin, 'Lead Source': lead_source,
            'Do Not Email': Not_Email, 'Do Not Call': Not_Call,
            'TotalVisits': TotalVisits, 'Total Time Spent on Website': Total_Time_Spent,
            'Page Views Per Visit': Page_Views, 'Last Activity': Last_Activity,
            'Country': Country, 'Specialization': Specialization, 'How did you hear about X Education': Hear_About,
            'What is your current occupation': Current_Occupation, 'What matters most to you in choosing a course': Matters_Most,
            'Search': Search, 'Magazine': Magazine,
            'Newspaper Article': Newspaper_Article, 'X Education Forums': X_Education_Forums,
            'Newspaper': Newspaper_Article, 'Digital Advertisement': Digital_Advertisement,
            'Through Recommendations': Through_Recommendations, 'Receive More Updates About Our Courses': Receive_More_Updates, 'Tags': Tags,
            'Lead Quality': Lead_Quality, 'Update me on Supply Chain Content': Update_Supply_Chain,
            'Get updates on DM Content': Get_updates_DM, 'Lead Profile': Lead_Profile,
            'City': City, 'Asymmetrique Activity Index': Activity_Index,
            'Asymmetrique Profile Index': Profile_Index, 'Asymmetrique Activity Score': Activity_Score,
            'Asymmetrique Profile Score': Profile_Score, 'I agree to pay the amount through cheque': cheque,
            'A free copy of Mastering The Interview': Mastering_Interview, 'Last Notable Activity': Notable_Activity,
            }

features_df  = pd.DataFrame([features])

#st.table(features_df)

if st.button('Predict'):
    prediction = predict_conversion(model, features_df)
    score0 = prediction['prediction_score_0'][0]
    score1 = prediction['prediction_score_1'][0]
    conversion = prediction['prediction_label'][0]
    if int(conversion)==1:
        st.header('Based on feature values, **the lead will lead to conversion!**  :grin: ')
    elif int(conversion)==0:
        st.header('Based on feature values, **the lead will NOT lead to conversion!**  :sweat: ')
    st.write('There is a **'+str(score1*100)+'%** chance that the lead will lead to conversion!')
    st.write('There is a **'+str(score0*100)+'%** chance that the lead will NOT lead to conversion!')




