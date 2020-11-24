import text
import time
import torch

import streamlit as st
import numpy as np

from backend import generate_results
from text import DetailedInfo

ALZ = text.Info()
Head = text.Headers()

def progress():

    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)

class Progress():

    def __enter__(self):
            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.1)
                my_bar.progress(percent_complete + 1)
            return None
        
    def __exit__(self, val1, val2, val3):
        return None

# st.text(torch.cuda.is_available())
Head.mainHead()
Head.about()
if st.sidebar.checkbox('Read more', key='mainReadMore'):
    ALZ.intro()
    ALZ.symptoms()
    ALZ.preserved()
    ALZ.causes()
    ALZ.treatment()


Head.scanConsole()
if st.sidebar.checkbox('Open Console'):
    Head.scanInst()
    col1, col2 = st.beta_columns([3,1])
    file_buffer = col1.file_uploader('Upload X-Ray image here', type=['png','jpg'])
    col2.markdown('\n')
    col2.markdown('\n')
    submit = col2.button('Generate Result')

    if submit:
        if file_buffer is not None:
            with Progress():
                result = generate_results(file_buffer)
                report = DetailedInfo()
                report.get_info(result)
        else:
            st.error('Please upload an image file first!')

Head.contributions()