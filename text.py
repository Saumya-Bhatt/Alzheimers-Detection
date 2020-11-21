import streamlit as st
from PIL import Image

def newline(n):
    for _ in range(n):
        st.markdown('\n')

class Info():

    def intro(self):
        newline(3)
        st.header("Alzheimer's Disease")
        st.markdown('''
        Alzheimer's disease is a progressive disorder that causes brain cells to waste away (degenerate) and die. Alzheimer's disease is the most common cause of dementia — a continuous decline in thinking, behavioral and social skills that disrupts a person's ability to function independently.
        ''')
        newline(1)
        ALZ_stages = Image.open('Images/stages-of-alzheimers.jpg')
        st.image(ALZ_stages,caption='Different stages of Alzheimers', use_column_width=True)
        return None

    def symptoms(self):
        newline(2)
        st.markdown('## Symptoms')
        st.markdown('''
        Memory loss is the key symptom of Alzheimer's disease. An early sign of the disease is usually difficulty remembering recent events or conversations. As the disease progresses, memory impairments worsen and other symptoms develop. Given below are some of the symptoms:
        \n
        1. Forgetting basic tasks, events or even name and faces of family members.
        2. Difficult multitasking which may even progress to inability to recognize and deal with basic maths.
        3. Poor judgement and planning.
        \n
        Above mentioned reasons can lead the person to depression, social withdrawal, mood swings, irritibily and may cause drastic changes in sleep and eating patterns.
        ''')
        newline(2)
        return None

    def preserved(self):
        st.markdown('## Preserved Skills')
        st.markdown('''
        Many important skills are preserved for longer periods even while symptoms worsen. Preserved skills may include reading or listening to books, telling stories and reminiscing, singing, listening to music, dancing, drawing, or doing crafts.
        \n
        These skills may be preserved longer because they are controlled by parts of the brain affected later in the course of the disease.
        ''')
        newline(2)
        return None

    def causes(self):
        st.markdown('## Probable Causes')
        st.markdown('''
        Scientists believe that for most people, Alzheimer's disease is caused by a combination of genetic, lifestyle and environmental factors that affect the brain over time.
        \n
        The exact causes of Alzheimer's disease aren't fully understood, but at its core are problems with brain proteins that fail to function normally, disrupt the work of brain cells (neurons) and unleash a series of toxic events. Neurons are damaged, lose connections to each other and eventually die.
        ''')
        newline(1)
        st.markdown('__Risk Factors__')
        st.markdown('''
        1. **Age** : Alzheimer's is not a part of normal aging, but as you grow older the likelihood of developing Alzheimer's disease increases.
        2. **Family History** : Scientists have identified rare changes (mutations) in three genes that virtually guarantee a person who inherits one of them will develop Alzheimer's. But these mutations account for less than 1 percent of people with Alzheimer's disease.
        3. **Gender** : There appears to be little difference in risk between men and women, but, overall, there are more women with the disease because they generally live longer than men.
        4. **Mild Cognitive Impairment** : MCI is a decline in memory or other thinking skills that is greater than what would be expected for a person's age, but the decline doesn't prevent a person from functioning in social or work environments.
        5. **Sleep Patterns** : Research has shown that poor sleep patterns, such as difficulty falling asleep or staying asleep, are associated with an increased risk of Alzheimer's disease.
        6. **Past Head Trauma** : People who've had a severe head trauma have a greater risk of Alzheimer's disease.
        7. **Lifestyle** : Research has shown that the same risk factors associated with heart disease may also increase the risk of Alzheimer's disease
        ''')
        newline(2)
        ALZ_age_vs_prevention = Image.open('Images/age_vs_prevention.jpg')
        st.image(ALZ_age_vs_prevention,caption='Correlation of age vs spread of Alzheimers', use_column_width=True)
        return None

    def treatment(self):
        newline(1)
        st.markdown('## Treatment and Prevention')
        st.markdown('''
        While there is no cure for Alzheimer’s disease or a way to stop or slow its progression, there are drug and non-drug options that may help treat symptoms. Understanding available options can help individuals living with the disease and their caregivers to cope with symptoms and improve quality of life.
        \n
        Alzheimer's disease is not a preventable condition. However, a number of lifestyle risk factors for Alzheimer's can be modified. Evidence suggests that changes in diet, exercise and habits — steps to reduce the risk of cardiovascular disease — may also lower your risk of developing Alzheimer's disease and other disorders that cause dementia.
        ''')
        return None

class Headers():

    def mainHead(self):
        st.title('Detection of Alzheimer using MRI and fMRI images')
        st.subheader('Introduction to Cognitive Neuroscience')
        st.markdown('''
        Data obtained from ADNI and Oasis dataset, and from brain MRI information available online.
        ''')
        return None

    def about(self):
        st.sidebar.header('About Alzheimer')
        st.sidebar.markdown('''
        Alzheimer's disease is a progressive disorder that causes brain cells to waste away (degenerate) and die ....
        ''')
        return None

    def scanConsole(self):
        st.sidebar.header('Scan for Alzheimers')
        st.sidebar.markdown("ML model which identifies probability of Alzheimers based on X-Ray image.")
        return None

    def scanInst(self):
        newline(2)
        st.header('Alzheimers detection model')
        st.markdown('A Machine Learning model, trained to identify probability of accurately predicting the occurance of Alzheimers disease in the uploaded image of the patient.')
        return None

    def contributions(self):
        st.sidebar.header('Made by :')
        st.sidebar.markdown('''
            1. B Raja Narasimhan
            2. Saumya Bhatt
            3. Shashank Mashusudan
            4. Mudit Srivastava
            5. Teshyansh Vatsyayan
            ''')
        return None

class DetailedInfo():

    def get_info(self, result):
        default = 'ERROR GENERATING RESULT'
        return getattr(self, 'result_' + str(result), lambda: default)()

    def result_1(self):
        st.error('Patient Probably has Mild Dementia')
        st.markdown('Our neural engine has diagnosed you with showing **mild dementia**. Following signs may be an indicator for you:')
        st.markdown('''
        1. Maintaining checkbooks and/or ledgers of any kind.
        2. Preparing complex meals and recepies.
        3. Following complex schedules and routines
        ''')
        newline(1)
        st.markdown('If you are facing any of the above difficulties, please vist your nearest doctor for more detailed analysis and checkup.')

    def result_2(self):
        st.error('Patient Probably has Moderate Dementia')
        st.markdown('Our neural engine has diagnosed you with showing **moderate dementia**. Following signs may be an indicator for you:')
        st.markdown('''
        1. Difficulties in simple food preparation, houshold chores or daily work.
        2. Feeling more and more agitated and confused.
        3. Showing signs of Insomnia
        ''')
        st.markdown('If you are facing any of the above difficulties, please vist your nearest doctor for more detailed analysis and checkup.')

    def result_3(self):
        st.balloons()
        st.success('Patient Probably has No Dementia')
        st.markdown('''
        Relax! Our neural engine says you probably don't have Dementia! However, be on look out for its symptoms in you and your loved ones.
        ''')

    def result_4(self):
        st.warning('Patient Probably has Very Mild Dementia')
        st.markdown('''
        Our neural engine has diagnosed you with showing **very mild Dementia**. Although you currently may not be exhibiting any obvious signs of dementia, it still is recommended to check for it with your home doctor.
        ''')