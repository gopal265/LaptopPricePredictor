import streamlit as st 
import numpy as np
import pickle
st.title('Laptop Price Prediction')

pipe = pickle.load(open('pipe.pkl','rb'))
laptop = pickle.load(open('laptop.pkl','rb'))

# brand 

company = st.selectbox('Brand',laptop['Company'].unique())

# type of laptop

type = st.selectbox('Type',laptop['TypeName'].unique())

# Ram 
ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

# weight 

weight = st.number_input(label='weight of laptop')

# TouchScreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])

# IPS

ips = st.selectbox('IPS',['No','Yes'])


# screen size 
screen_size = st.number_input('Screen Size')

# resolution


resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

# cpu 

cpu = st.selectbox('CPU',laptop['Cpu_Brand'].unique())


# hdd

hdd = st.selectbox('HDD (in GB)',[0,128,256,512,1024,2048])

# ssd

ssd = st.selectbox('SSD (in GB',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',laptop['Gpu_Brand'].unique())

os = st.selectbox('OS',laptop['os'].unique())

if st.button('Predict Price') :
    # query 
   

    if touchscreen == 'Yes' :
        touchscreen = 1 
    else :
        touchscreen = 0
    
    if ips == 'Yes' :
        ips = 1
    else : 
        ips = 0 

    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1]) 
    ppi = ((x_res)**2 + (y_res)**2)**0.5/screen_size      


    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.title(int(np.exp(pipe.predict(query))))

