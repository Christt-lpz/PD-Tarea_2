# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 23:59:04 2021

@author: chris
"""

import  streamlit as  st
import  pandas  as  pd
"""
# Uber
"""
source ='https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'
#data=(pd.read_csv(source)
#      .rename(columns={'Lat':'lat', 'Lon':'lon'})
      
#      )

@st.cache
def dowload_data():
    data=(pd.read_csv(source)
      .rename(columns={'Lat':'lat', 'Lon':'lon'}))
    
    return  data
    
data=dowload_data()



"""
### Filto por registro
"""
paginas = int(len(data) /1000)



slider = st.slider('Selection  page ',1, paginas) 

#data.loc[0:1000]
#st.sidebar.write('the range  selected  is ', type(slider) )



st.write("Pagina ", slider)
if slider==1:
    st.write("Registros  0 - 1000")
    data[0:1001]
    
else:
    st.write("Registros " , slider*1000 ,  ' - ' , (slider*1000)+1000 )
    data[slider*1000:(slider*1000)+1001]
   
    
st.write("-------------------------------------------------")   
st.write("-------------------------------------------------")   
    
    
"""
### Filtro por fecha y hora
"""
    
st.write("Ser realiza el filto por fecha y hora del mes de septiembre 2014")
    
    
#Dia = st.slider('Seleccione dia ',1, 30) 
Horaconsulta = st.slider('Seleccione hora',0, 24) 
    
    
    
dataA=data 
dataA=dataA["Date/Time"].str.split(expand=True)


#st.write(dataA)

dataB=dataA 
dataB=dataB[1].str.split(':',expand=True)

dataB=dataB.rename(columns={0:'Hora',1:'Minutos',2:'Segundos'})


#df.columns.values
#st.write(dataB.columns.values)

df = data.assign(hora=dataB["Hora"]) 


valor=int(Horaconsulta)
st.write(df[df['hora']==str(valor)])



st.write("-------------------------------------------------")   
st.write("-------------------------------------------------")   
    


    
    
    
    