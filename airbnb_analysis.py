# ===============================================================
# Airbnb Open Data Analysis - Complete Project
# Covers Booking Patterns, Pricing, Guest Preferences, Host Performance
# Answers 9 key analytical questions with visualizations
# ===============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# ----------------------------
# 1. Load dataset
# ----------------------------
DATA_PATH = "1730285881-Airbnb_Open_Data.xlsx"
df = pd.read_excel(DATA_PATH)

print("✅ Dataset loaded successfully!")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("\nColumns available:\n", list(df.columns))

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Basic cleaning
for col in ["price", "service_fee", "review_rate_number", "availability_365", "calculated_host_listings_count"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

df.dropna(subset=["price", "neighbourhood_group", "room_type"], how="any", inplace=True)

# Set style
sns.set(style="whitegrid", palette="viridis")
plt.rcParams["figure.figsize"] = (8, 5)

# ----------------------------
# Q1. What are the different property types in dataset?
# ----------------------------
print("\nQ1️⃣: Property types distribution:")
if "room_type" in df.columns:
    room_counts = df["room_type"].value_counts()
    print(room_counts)
    room_counts.plot(kind="bar", title="Property Types in Dataset")
    plt.xlabel("Room Type")
    plt.ylabel("Count")
    plt.show()

# ----------------------------
# Q2. Which neighbourhood group has the highest number of listings?
# ----------------------------
print("\nQ2️⃣: Neighbourhood group with highest number of listings:")
if "neighbourhood_group" in df.columns:
    group_counts = df["neighbourhood_group"].value_counts()
    print(group_counts)
    sns.barplot(x=group_counts.index, y=group_counts.values)
    plt.title("Listings per Neighbourhood Group")
    plt.xlabel("Neighbourhood Group")
    plt.ylabel("Number of Listings")
    plt.show()

# ----------------------------
# Q3. Which neighbourhood group has highest average prices?
# ----------------------------
print("\nQ3️⃣: Average price by neighbourhood group:")
if "price" in df.columns:
    avg_price = df.groupby("neighbourhood_group")["price"].mean().sort_values(ascending=False)
    print(avg_price)
    sns.barplot(x=avg_price.index, y=avg_price.values)
    plt.title("Average Price by Neighbourhood Group")
    plt.xlabel("Neighbourhood Group")
    plt.ylabel("Average Price")
    plt.show()

# ----------------------------
# Q4. Relationship between construction year and price
# ----------------------------
print("\nQ4️⃣: Relationship between Construction Year and Price:")
if "construction_year" in df.columns:
    sns.scatterplot(x="construction_year", y="price", data=df, alpha=0.5)
    plt.title("Price vs Construction Year")
    plt.xlabel("Construction Year")
    plt.ylabel("Price")
    plt.show()

# ----------------------------
# Q5. Top 10 hosts by calculated host listing count
# ----------------------------
print("\nQ5️⃣: Top 10 hosts by listing count:")
if "host_name" in df.columns and "calculated_host_listings_count" in df.columns:
    top_hosts = df.groupby("host_name")["calculated_host_listings_count"].sum().sort_values(ascending=False).head(10)
    print(top_hosts)
    sns.barplot(y=top_hosts.index, x=top_hosts.values)
    plt.title("Top 10 Hosts by Listing Count")
    plt.xlabel("Total Listings")
    plt.ylabel("Host Name")
    plt.show()

# ----------------------------
# Q6. Are verified hosts more likely to receive positive reviews?
# ----------------------------
print("\nQ6️⃣: Verified hosts and positive reviews:")
if "host_identity_verified" in df.columns and "review_rate_number" in df.columns:
    sns.boxplot(x="host_identity_verified", y="review_rate_number", data=df)
    plt.title("Review Ratings: Verified vs Non-Verified Hosts")
    plt.xlabel("Host Verified")
    plt.ylabel("Review Rating")
    plt.show()

# ----------------------------
# Q7. Correlation between price and service fee
# ----------------------------
print("\nQ7️⃣: Correlation between Price and Service Fee:")
if "service_fee" in df.columns:
    corr_val = df["price"].corr(df["service_fee"])
    print(f"Correlation: {corr_val:.2f}")
    sns.scatterplot(x="price", y="service_fee", data=df, alpha=0.5)
    plt.title(f"Price vs Service Fee (corr={corr_val:.2f})")
    plt.xlabel("Price")
    plt.ylabel("Service Fee")
    plt.show()

# ----------------------------
# Q8. Average review rate by neighbourhood and room type
# ----------------------------
print("\nQ8️⃣: Average review rate by neighbourhood group and room type:")
if "review_rate_number" in df.columns:
    avg_review = df.groupby(["neighbourhood_group", "room_type"])["review_rate_number"].mean().unstack()
    print(avg_review)
    avg_review.plot(kind="bar", title="Average Review Rate by Neighbourhood and Room Type")
    plt.ylabel("Average Review Rating")
    plt.show()

# ----------------------------
# Q9. Are hosts with more listings more available throughout the year?
# ----------------------------
print("\nQ9️⃣: Host listings count vs availability:")
if "availability_365" in df.columns:
    corr2 = df["calculated_host_listings_count"].corr(df["availability_365"])
    print(f"Correlation between Host Listing Count and Availability: {corr2:.2f}")
    sns.scatterplot(x="calculated_host_listings_count", y="availability_365", data=df, alpha=0.5)
    plt.title("Host Listing Count vs Availability 365")
    plt.xlabel("Host Listing Count")
    plt.ylabel("Availability (days/year)")
    plt.show()

# ===============================================================
# ADDITIONAL ANALYSIS SECTIONS
# ===============================================================

# 🟢 Booking Patterns
print("\n📘 Booking Patterns Analysis:")
if "reviews_per_month" in df.columns:
    sns.lineplot(x="reviews_per_month", y="price", data=df)
    plt.title("Bookings (Reviews) vs Price Trend")
    plt.xlabel("Reviews per Month (proxy for bookings)")
    plt.ylabel("Price")
    plt.show()

# 🟡 Pricing Strategies
print("\n📗 Pricing Strategies Insights:")
sns.boxplot(x="room_type", y="price", data=df)
plt.title("Price Variation by Room Type")
plt.show()

# 🔵 Guest Preferences
print("\n📙 Guest Preferences and Ratings:")
sns.boxplot(x="room_type", y="review_rate_number", data=df)
plt.title("Guest Ratings by Room Type")
plt.show()

# 🔴 Host Performance
print("\n📕 Host Performance Analysis:")
sns.scatterplot(x="calculated_host_listings_count", y="review_rate_number", data=df)
plt.title("Host Listings Count vs Review Ratings")
plt.show()

print("\n✅ All 9 questions answered and insights visualized successfully!")
