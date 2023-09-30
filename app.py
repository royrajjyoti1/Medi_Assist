import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from medical import output_fun ,remark ,remark_hindi, recommend_Medication ,recommend_Medication_hindi , extract_from_content_v2
import time


def main():
    
    st.set_page_config(page_title=" Medi Assist", page_icon=":clock330:",layout="wide")
    col1,col2=st.columns([1,2])
    col1.header("Medi Assist ",divider='rainbow')
    
    
    with st.container():
        st.subheader(":blue[Please upload your medical prescription]")
        image_url = st.text_input("Enter the URL of the image")
        image_width = 500 
        if image_url:
            with st.status("Processing...", expanded=True) as status:
                
                result=output_fun(image_url)
                generated_remark=remark(result)
                generated_Medication=recommend_Medication(generated_remark) 
                
                status.update(label="Process completed!", state="complete", expanded=False)
            
            
            try:
                col2.image(image_url, caption='Your Image', width=image_width)
                col1,col2,col3,col4,col5=st.columns([1,1,1,1,1])
                
                if col1.button("Blood Report Summary"):
                    st.subheader("You clicked Summary!",divider='rainbow')
                    st.text(result)
                    st.success('Done!')
                        
                    
                if col2.button("Generate Remark"):
                    st.subheader("You clicked Remark!",divider='rainbow')
                    st.text(generated_remark)
                    st.success('Done!')
                    
                    
                if col3.button("Generate Remark in Hindi"):
                    st.subheader("You clicked Remark in Hindi!",divider='rainbow')
                    generated_remark_in_hindi=remark_hindi(generated_remark)
                    #print("generated_remark_hindi",generated_remark_in_hindi)
                    st.text(generated_remark_in_hindi)
                    
                    st.success('Done!')
                    
                if col4.button("Recommend Medication"):
                    st.subheader("You clicked Recommend Medication!",divider='rainbow')
                    #print("generated_Medication",generated_Medication)
                    st.text(generated_Medication)
                    st.success('Done!')
                    
                    
                if col5.button("Recommend Medication in Hindi"):
                    st.subheader("You clicked Recommend Medication in Hindi!",divider='rainbow')
                    generated_Medication_in_hindi=recommend_Medication_hindi(generated_Medication)
                    #print("generated_Medication in hindi",generated_Medication_in_hindi)
                    st.text(generated_Medication_in_hindi)
                    st.success('Done!')

            except Exception as ex:
                st.error(f"Error opening image: {str(ex)}")
        
        
        
        
            
        


            
            # Add two buttons
        







if __name__=='__main__':
    main()