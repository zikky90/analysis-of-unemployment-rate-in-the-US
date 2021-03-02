#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()


# In[3]:


def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


# In[13]:


links={'GDP':'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/clean_gdp.csv',       'unemployment':'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/clean_unemployment.csv'}


# In[7]:


import pandas as pd


# In[16]:


df_gdp = pd.read_csv(links["GDP"]) #dataframe that contains GDP data


# In[17]:


df_gdp.head() #to display 5 rows


# In[18]:


df_unemployment = pd.read_csv(links["unemployment"]) #dataframe for unemployment data


# In[19]:


df_unemployment.head() #5 rows of unemployment data


# In[20]:


result_employ = df_unemployment[(df_unemployment.unemployment>8.5)]
print(result_employ) #where unemployment is greater than 8.5


# In[23]:


x = df_gdp['date'] #let the plotting function x be date
gdp_change = df_gdp['change-current'] # let change cureent be gdp_change
unemployment = df_unemployment['unemployment'] #for the unemployment column
title = 'unemployment' #assign title to the unemployment column
file_name = "index.html" #for file_name column


# In[24]:


make_dashboard(x = x, gdp_change = gdp_change, unemployment = unemployment, title = title, file_name = file_name) #plotting


# In[ ]:




