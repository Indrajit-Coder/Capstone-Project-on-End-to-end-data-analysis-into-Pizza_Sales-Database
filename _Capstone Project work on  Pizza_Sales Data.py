#!/usr/bin/env python
# coding: utf-8

# # Capstone Project Work on "Pizza_Sales" Database

# ![](Pizza_Image.webp)

# In[3]:


#import the libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.offline import iplot


# In[5]:


#import the dataset
data= pd.read_csv('pizza_sales.csv')
data.head()


# In[6]:


#Checking if there are any null values in the dataset
data.isnull().sum()


# In[7]:


#info of the dataset to check the column names, data-types
data.info()


# In[8]:


# import the database
data= pd.read_csv('pizza_sales.csv')
data.tail()


# In[9]:


#Checking the rows and columns in the dataset
data.shape


# # Exploratory Data Analysis on "pizza_sales" Database

# In[10]:


# Data frame
import pandas as pd
data = pd.read_csv('pizza_sales.csv')
data['Month']=data['order_date'].apply


# In[11]:


data.dtypes


# In[12]:


data['Month'].unique()


# In[13]:


data['unit_price']=data['unit_price'].astype(float)


# In[14]:


data['quantity']=data['quantity'].astype(int)


# In[15]:


data['Pizza_Sales']=data['quantity']*data['unit_price']
data.head(5)


# In[16]:


data.groupby('Month')['Pizza_Sales'].sum()


# In[23]:


# Import "pizza_sales" database into Bar Chart 
months=range(1,13)
plt.bar(months,data.groupby('Month')['Pizza_Sales'].sum())
plt.xticks(months)
plt.ylabel('Pizza_Sales')
plt.xlabel('Month Number')
plt.show()


# In[24]:


# Import "pizza_sales" database into Bar Chart 
months=range(1,13)
plt.bar(data.groupby('quantity')['quantity'].count().index,data.groupby('quantity')['quantity'].count())
plt.xticks(rotation='horizontal')
plt.ylabel('pizza_category')
plt.xlabel('quantity')
plt.show()


# In[26]:


# Import "pizza_sales" database into Bar Chart 
months=range(1,13)
plt.bar(data.groupby('pizza_size')['pizza_size'].count().index,data.groupby('pizza_size')['pizza_size'].count())
plt.xticks(rotation='vertical')
plt.ylabel('pizza_category')
plt.xlabel('pizza_size')
plt.show()


# In[31]:


# Define horizontal Bar Graph using matplotlib
plt.figure(figsize=(10, 5))
sns.barplot(x='total_price',y='pizza_name',data = pd.read_csv('pizza_sales.csv'))
plt.title('total_price vs pizza_name (Top 10)')
plt.xlabel('total_price')
plt.ylabel('pizza_name')
plt.show()


# In[33]:


# Assuming 'data' is your DataFrame 
pizza_id = data['pizza_id'].value_counts() 
pizza_id_counts = data['pizza_name_id'].value_counts()
# Using Matplotlib to create a count plot 
plt.figure(figsize=(50,30)) 
plt.bar(pizza_id_counts.index, pizza_id_counts, color='Blue') 
plt.title('Count Plot of pizza_id') 
plt.xlabel('pizza_id') 
plt.ylabel('pizza_name_id') 
plt.show() 


# In[34]:


# Set Seaborn style 
sns.set_style("darkgrid") 
 
# Identify numerical columns 
numerical_columns = data.select_dtypes(include=["int64", "float64"]).columns 
 
# Plot distribution of each numerical feature 
plt.figure(figsize=(14, len(numerical_columns) * 3)) 
for idx, feature in enumerate(numerical_columns, 1): 
   plt.subplot(len(numerical_columns), 2, idx) 
   sns.histplot(data[feature], kde=True) 
   plt.title(f"{feature} | Skewness: {round(data[feature].skew(), 2)}") 
 
# Adjust layout and show plots 
plt.tight_layout() 
plt.show() 


# In[35]:


# Set the color palette 
sns.set_palette("Pastel1") 
  
# Assuming 'data' is your DataFrame 
plt.figure(figsize=(10, 6)) 
  
# Using Seaborn to create a pair plot with the specified color palette 
sns.pairplot(data) 
  
plt.suptitle('Pair Plot for DataFrame') 
plt.show() 


# In[36]:


# Pie Charts using Matplotlib in Python
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
# Mesurment of Total_Price of various Pizza_Category
x = np.array([13.25,16,18.50,20.75])
mylabels = ["Classic","Veggie","Supreme","Chicken"]
plt.pie(x, labels = mylabels)
plt.show()


# In[37]:


# Pie Charts using Matplotlib in Python
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
# Mesurment of Pizza_Size vs Total_Price
labels = ('Regular','Medium','Large','X-Large','XX-Large')
sizes = ([14,18,25,10,5])
plt.pie(sizes, labels = labels, autopct = '%1.f%%', counterclock = False)
#Display th figure
plt.show()


# In[44]:


# Scatterplot using Seaborn in Python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
Countries_data = pd.read_csv('pizza_sales.csv')

sns.scatterplot(x = data['pizza_size'], y = data['pizza_category'], hue = Countries_data['pizza_id'])


# In[46]:


# Boxplot using seaborn in Python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv('pizza_sales.csv')
sns.boxplot(data["pizza_id"])


# In[47]:


data.describe()


# In[52]:


# Boxplot using seaborn in Python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

plt.figure(figsize=(30,10))
sns.boxplot(x = "pizza_name", y = "quantity",data = pd.read_csv('pizza_sales.csv'))


# In[57]:


# Boxplot using seaborn in Python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
data = pd.read_csv('pizza_sales.csv')
sns.boxplot(x = "pizza_name", y = "order_id",data = pd.read_csv('pizza_sales.csv'))


# In[62]:


# Barplot using seaborn in Python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

plt.figure(figsize=(30,10))
data = pd.read_csv('pizza_sales.csv')
sns.barplot(x = "pizza_name_id", y = "order_id", data=pd.read_csv('pizza_sales.csv'))


# ### Topic of Correlation Matrix

# In[72]:


# Define Correlation Matrix using Seaborn in Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

numeric_cols = data.select_dtypes(include=np.number).columns                                         
plt.figure(figsize=(12, 8))
sns.heatmap(data[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# In[73]:


# import different types of Bar graphs using Python
data.hist(bins = 20, figsize = (20,20), color = 'green')
plt.show()


# In[75]:


# Define vertical Bar Graph using matplotlib 
data_grouped = data.groupby('pizza_name').sum().reset_index()
plt.figure(figsize=(15, 10))                                             
goalplot = sns.barplot(x='pizza_name', y='order_id', data=data_grouped)
plt.title('Pizza_Name vs Order_id Bar Chart')
plt.xlabel('Pizza_Name')
plt.ylabel('Order_id')

for p in goalplot.patches:
    goalplot.annotate(format(p.get_height(), '.1f'), 
                      (p.get_x() + p.get_width() / 2., p.get_height()), 
                      ha='center', va='center', 
                      xytext=(0, 10), 
                      textcoords='offset points')

plt.xticks(rotation=90)
plt.show()  


# In[80]:


# Define Seaborn Chart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.jointplot(data['pizza_category'])


# In[88]:


# Define Seaborn Chart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.jointplot(data['pizza_id'],kind="hex")


# In[5]:


# Define Seaborn Chart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data =  pd.read_csv('pizza_sales.csv')
sns.pairplot(data[['pizza_id','quantity','total_price']])


# In[99]:


# Define Seaborn Chart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.lmplot(x='pizza_id',y= 'quantity',data = pd.read_csv('pizza_sales.csv'))


# In[98]:


# Define Seaborn Chart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.lmplot(x='pizza_id',y='quantity',hue ="pizza_size",data = pd.read_csv('pizza_sales.csv'))


# # Thank You So Much !!
