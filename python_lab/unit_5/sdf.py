import matplotlib.pyplot as plt

# Restaurant names
restaurants = [
    "Pizza Palace",
    "Burger Hub",
    "Spice Garden",
    "Food Corner",
    "Chinese House"
]

# Number of orders
orders = [120, 90, 150, 70, 100]

# Creating bar plot
plt.bar(restaurants, orders)

# Adding title
plt.title("Restaurant-Wise Order Comparison")

# Adding labels
plt.xlabel("Restaurants")
plt.ylabel("Number of Orders")

# Display graph
plt.show()