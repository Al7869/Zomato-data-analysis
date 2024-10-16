#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Data Manipulation
import pandas as pd
import numpy as np

# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Display plots inline
get_ipython().run_line_magic('matplotlib', 'inline')

# Optional: Ignore warnings
import warnings
warnings.filterwarnings('ignore')


# In[6]:


# Load the Zomato data from a CSV file
zomato_data = pd.read_csv('zomato.csv')

# Display first 5 rows
zomato_data.head()


# In[7]:


# View basic information about the dataset
zomato_data.info()

# Check for missing values
zomato_data.isnull().sum()

# Basic statistics of numerical columns
zomato_data.describe()


# In[22]:


# Drop duplicates if any
zomato_data = zomato_data.drop_duplicates()

# Remove rows with missing values in important columns (e.g., 'rate', 'location')
zomato_data = zomato_data.dropna(subset=['rate (out of 5)', 'area'])


# View cleaned data
zomato_data.head()


# In[23]:


# Get top 10 restaurants by average rating
top_rated_restaurants = zomato_data.groupby('restaurant name')['rate (out of 5)'].mean().sort_values(ascending=False).head(10)
print(top_rated_restaurants)


# In[24]:


# Count the most popular cuisines
popular_cuisines = zomato_data['cuisines type'].value_counts().head(10)
print(popular_cuisines)

# Plot most popular cuisines
sns.barplot(x=popular_cuisines, y=popular_cuisines.index)
plt.title('Top 10 Cuisines')
plt.xlabel('Number of Restaurants')
plt.show()


# In[25]:


# Clean the 'approx_cost(for two people)' column
zomato_data['avg cost (two people)'] = zomato_data['avg cost (two people)'].replace(',', '').astype(float)

# Plot average cost for two people
plt.figure(figsize=(10,6))
sns.histplot(zomato_data['avg cost (two people)'], bins=30, kde=True)
plt.title('Distribution of Approximate Cost for Two People')
plt.xlabel('Approx Cost (for two)')
plt.show()


# In[26]:


# Count the number of restaurants in each location
restaurants_by_location = zomato_data['area'].value_counts().head(10)

# Plot the number of restaurants by location
sns.barplot(x=restaurants_by_location, y=restaurants_by_location.index)
plt.title('Top 10 Locations with Most Restaurants')
plt.xlabel('Number of Restaurants')
plt.show()


# In[27]:


# Average rating by location
location_ratings = zomato_data.groupby('area')['rate (out of 5)'].mean().sort_values(ascending=False).head(10)

# Plot average rating by location
sns.barplot(x=location_ratings, y=location_ratings.index)
plt.title('Top 10 Locations by Average Restaurant Rating')
plt.xlabel('Average Rating')
plt.show()


# In[35]:


restaurant_ratings = zomato_data.groupby('restaurant name')['rate (out of 5)'].mean().sort_values(ascending=False).head(10)

# Plot average rating by location
sns.barplot(x=restaurant_ratings, y=restaurant_ratings.index)
plt.title('Top 10 Restaurant with average rating')
plt.xlabel('Average Rating')
plt.show()


# # Some insights from the above analysis

# Top-Rated Restaurants:  "Restaurant SantÂ© Spa Cuisine, Asia Kitchen By Mainland China and Byg Brewski Brewing Company  has the highest average rating of 4.9, indicating superior customer satisfaction, whereas most restaurants average between 3.5 and 4.0.
# 
# Popular Cuisines: "North Indian and Chinese are the most popular cuisines in the dataset, with over 500 restaurants offering these options, reflecting a high demand for these food categories."
# 
# Cost Distribution: "The majority of restaurants have an approximate cost of ₹200-₹500 for two people, with a small percentage of premium restaurants charging above ₹1000."
# 
# Restaurant Density by Location: "Byresandra,Tavarekere,Madiwala	have the highest concentration of restaurants, making them key dining districts, while areas like Banashankari have fewer restaurant options, presenting potential for growth."
# 
# Restaurant Ratings by Location: "Restaurants in Brigade Road tend to have the highest average ratings (4.2), while less prominent areas like Koramangala 7th block show lower average ratings (3.8), indicating a disparity in customer satisfaction across locations."
# 
# 
# 

# # Conclusion
# 

# 1.For consumers, it highlights the best-rated restaurants, the cost
# distribution, and popular cuisines,making it easier to choose dining options.
# 
# 2.For restaurant owners, it provides insights into competitive locations,
# popular cuisines, and potential areas for improvement.
# 
# 3.For investors or entrepreneurs, understanding location-based preferences 
# and pricing trends can inform where to open new restaurants or adjust their
# menu pricing.

# In[ ]:




