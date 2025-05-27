# ------------------------------------------------------
# Airbnb India Top 500 Dataset Analysis (Pure Pandas)
# Author: [SUCHET MAHAJAN]
# Goal: Explore and analyze listing data to derive insights
# ------------------------------------------------------


import pandas as pd

df = pd.read_csv(r"C:\Users\suche\Downloads\Airbnb_India_Top_500.csv")


# View basic info

print(df.info())         # Displays summary information about the DataFrame, including column names, non-null counts, and data types
print(df.shape)          # give us shape of the data which (500,9)
print(df.head())         # top 5 data
print(df.columns)        # address', 'isHostedBySuperhost', 'location/lat', 'location/lng',
print(df.isnull().sum()) # Giving sum of null value '''  

#------------------------------------
# Step 2: Data Cleaning & Preparation
#------------------------------------

# Extract city from address(important for city-level analysis)
df['city'] = df['address'].apply(lambda x : x.split(',') [0].strip())

# Create price per guest column (used in later capacity analysis)
df['price per guest'] = df['pricing/rate/amount'] / df['numberOfGuests'] 


# ------------------------------------------
# Step 3: Define Business Questions
# ------------------------------------------
# 1. Which cities have the most listings?
# 2. How does price vary by city and room type?
# 3. Do superhosts charge more or get higher ratings?
# 4. What’s the relationship between capacity and price?
# 5. Which listings are most expensive or cheapest?
# 6. Is there a correlation between price, rating, and guests?

# ------------------------------------------
# Step 4: Location-Based Analysis
# ------------------------------------------

# Top cities by number of listings
top_cities = df['city'].value_counts().head(20)
print(top_cities)

# average price per city
average_price_city = df.groupby('city')['pricing/rate/amount'].mean().sort_values(ascending = False) 
print(average_price_city.head(10))

# Superhost listing counts per city (True/False counts)
superhost_dist = df.groupby('city')['isHostedBySuperhost'].value_counts().sort_values(ascending = False) 
print(superhost_dist.head(10))

#  Superhost distribution per city (percentage of True/False)
superhost_dist = df.groupby('city')['isHostedBySuperhost'].value_counts(normalize=True).unstack().fillna(0)
print(superhost_dist.head(10))


# ------------------------------------------
# Step 5: Pricing Analysis
# ------------------------------------------

# 💸 Price stats
print(df['pricing/rate/amount'].describe())

# 🛏️ Average price by room type
price_per_room = df.groupby('roomType')['pricing/rate/amount'].mean().sort_values(ascending = False)
print(price_per_room.head(10))

#  Top 10 most expensive listings
top_expensive = df.sort_values(by = 'pricing/rate/amount', ascending = False).head(10)
print(top_expensive[['name', 'pricing/rate/amount', 'city']])

#  Top 10 cheapest listings
top_cheap = df.sort_values(by = 'pricing/rate/amount', ascending = True).head(10)
print(top_cheap[['name', 'pricing/rate/amount', 'city']])


# ------------------------------------------
# Step 6: Ratings & Quality Analysis
# ------------------------------------------

# Ratings summary
'''print(df['stars'].describe())'''

# Rating by room type
'''rating_by_room = df.groupby('roomType')['stars'].mean().sort_values(ascending = False).head(10)
print(rating_by_room)'''

# Ratings: Superhost vs Non-superhost
'''rating_by_superhost= df.groupby('isHostedBySuperhost')['stars'].mean()
print(rating_by_superhost)''' 

#  Cities with best-rated listings
'''top_rating_city= df.groupby('city')['stars'].mean().dropna().sort_values(ascending = False).head(10)
print(top_rating_city)'''


# ------------------------------------------
# Step 7: Capacity Analysis
# ------------------------------------------

# Capacity vs price correlation
capacity_price_corr = df[['numberOfGuests' , 'pricing/rate/amount']].corr()
print(capacity_price_corr)

# Capacity by room type
capacity_by_room = df.groupby('roomType')['numberOfGuests'].mean().sort_values(ascending=False).head(10)
print("Average capacity by room" , capacity_by_room)
 
# Average price per guest by city
price_per_guest = df.groupby('city')['price per guest'].mean().sort_values(ascending=False).head(10)
print("Average Price per Guest by City" , price_per_guest)


# ------------------------------------------
# Step 8: Combined Analysis
# ------------------------------------------

multi_corr = df[['pricing/rate/amount' , 'stars', 'numberOfGuests']].corr()
print("Multivariate Correlation Matrix", multi_corr)











   


