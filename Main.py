#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 13:26:09 2023

@author: shbmsk
"""

import streamlit as st

st.set_page_config(
    page_title="Bista Home",
    page_icon="",
)

st.write("# Bista Solution Inc. in LLMs")

st.sidebar.success("Choose an option.")

st.markdown(
    """
Bista Solutions is an ERP consulting and implementation company. 
We specialize in implementing business applications, including; ERP, BPM, HRMS, BI with Big Data, and e-Commerce solutions. Additionally, the company has been recognized as one of the fastest growing companies 2016 in USA by Inc 5000 with a high ranking of #773 and is also ISO 9001: 2008 certified, and HIPAA / PCI / ITAR compliant.


    ### Bista's ML services?
    - Market & stock Forecasting
    - Information extraction from invoices
    - Building LLMs based application
    
    ### Overview of LLM based Application
    - CSV & XLSX file conversation
    - SQL Database Prompt Query
    - Question Answering
    - PDF to Query
    
    
    ### Developed By
    Md. Jafril Alam Shihab
    Trainee ML Engineer
    Bista Solution Inc.
    
"""
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
