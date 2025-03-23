import pandas as pd

# CSV dosyasını yükleme
data = pd.read_csv('./Data/raw_data/recipes.csv')

# Keywords sütunundaki tüm anahtar kelimeleri temizleme ve benzersiz olanları tutma
keywords = data['Keywords'].dropna().apply(lambda x: x.strip('c()').replace('"', '').split(', '))

# Tüm anahtar kelimeleri bir listeye ekleme
all_keywords = [keyword for sublist in keywords for keyword in sublist]

# Benzersiz anahtar kelimeleri bulma
unique_keywords = set(all_keywords)

# Benzersiz anahtar kelimeleri yazdırma
for keyword in unique_keywords:
    print(keyword)
    
    
# Mahi Mahi
# Iraqi
# High In...
# Mixer
# Polynesian
# Spaghetti
# Japanese
# Breakfast Potatoes
# Tomato Sauce
# Egg Free
# Mashed Potatoes
# Weeknight
# Grapes
# High Protein
# Vietnamese
# Beef Barley Soup
# Peppers
# Marinara Sauce
# Greek
# Thanksgiving
# Low Protein
# Eggs Breakfast
# Hawaiian
# Dairy Free Foods
# Pot Roast
# Tropical Fruits
# Curries
# Corn
# Easy
# Artichoke
# Cabbage
# Collard Greens
# Poultry
# Quail
# Malaysian
# Baked Beans
# Tortilla Soup
# < 4 Hours
# Meatloaf
# Potluck
# Sudanese
# Christmas
# South African
# Deep Fried
# Whitefish
# Dutch
# Yam/Sweet Potato
# Asian
# Creole
# Roast Beef
# Canning
# Pineapple
# New Zealand
# Bean Soup
# Cherries
# Coconut Desserts
# Pork Loin
# Szechuan
# Nigerian
# Free Of...
# Fruit
# For Large Groups Holiday/Event
# Thai
# Elk
# Icelandic
# Pheasant
# Very Low Carbs
# < 60 Mins
# Beef Sauces
# Mexican
# Beef Kidney
# Scandinavian
# Mussels
# Trout
# Cajun
# Mongolian
# Kosher
# Cauliflower
# African
# Kid Friendly
# Fish Halibut
# Brown Rice
# Chicken
# Sweet
# Orange Roughy
# Beef Liver
# Lentil
# Short Grain Rice
# Summer
# Jellies
# Toddler Friendly
# Lactose Free
# Pork Crock Pot
# Australian
# Halibut
# Spanish
# Refrigerator
# Melons
# Cantonese
# Portuguese
# No Bake Cookie
# Cucumber
# Polish
# Stove Top
# Breakfast Eggs
# Candy
# Indonesian
# Savory
# Steak
# Veal
# Whole Chicken
# Spicy
# Native American
# < 30 Mins
# Sauces
# Lime Desserts
# Halloween
# Hanukkah
# Turkish
# Smoothies
# Strawberry
# Spreads
# Bear
# Bar Cookie
# No Shell Fish
# Salad Dressings
# Peruvian
# Bass
# Lime
# Pears
# Breads
# Scottish
# Avocado
# Cranberry Sauce
# Berries
# Crock Pot Slow Cooker
# Hungarian
# Chowders
# Georgian
# Austrian
# Costa Rican
# Medium Grain Rice
# Norwegian
# Soy/Tofu
# Oranges
# Baking
# Freezer
# Quick Breads
# Small Appliance
# Cuban
# Goose
# Pakistani
# Pasta Shells
# Moroccan
# Stocks
# Steam
# Chicken Stews
# Welsh
# Clear Soup
# Vegan
# Puerto Rican
# Tex Mex
# Cheese
# Pot Pie
# One Dish Meal
# Reynolds Wrap Contest
# Lunch/Snacks
# Chicken Thigh & Leg
# Deer
# College Food
# Stew
# Filipino
# Crab
# Stir Fry
# Beginner Cook
# White Rice
# For Large Groups
# Long Grain Rice
# Dessert
# Kiwifruit
# Caribbean
# Manicotti
# Savory Pies
# Nuts
# Brazilian
# Camping
# Pie
# Duck Breasts
# Honduran
# Tuna
# < 15 Mins
# Plums
# South American
# Finnish
# Cheesecake
# Egyptian
# Catfish
# Palestinian
# Cambodian
# High Fiber
# Swiss
# Duck
# Chard
# Whole Turkey
# Potato
# Colombian
# Lebanese
# Canadian
# Pressure Cooker
# Greens
# Microwave
# Squid
# Dehydrator
# Pennsylvania Dutch
# Homeopathy/Remedies
# Spring
# Papaya
# Indian
# Strawberries Desserts
# Roast
# Shakes
# Birthday
# Ramadan
# Rice
# Vegetable
# Ham
# Halloween Cocktail
# Meatballs
# Raspberries
# Grains
# Somalian
# Ecuadorean
# Wild Game
# Perch
# Gumbo
# Korean
# Southwest Asia (middle East)
# St. Patrick's Day
# Chinese New Year
# Lobster
# Beverages
# Brunch
# Winter
# Gelatin
# Belgian
# Pasta Elbow
# Oven
# Moose
# No Cook
# Desserts Easy
# Lemon
# Ethiopian
# Southwestern U.S.
# Meat
# Beef Crock Pot
# Danish
# Citrus
# Guatemalan
# Bread Machine
# Served Hot New Years
# Household Cleaner
# Yeast Breads
# Pork
# From Scratch
# Low Cholesterol
# Breakfast
# German
# Tempeh
# Inexpensive
# Cookie & Brownie
# Punch Beverage
# Broil/Grill
# Bath/Beauty
# Peanut Butter
# Oysters
# Chocolate Chip Cookies
# Apple
# Pumpkin
# Chicken Breast
# Chicken Stew
# Frozen Desserts
# Russian
# Czech
# Octopus
# Lamb/Sheep
# Navy Bean Soup
# Coconut
# Nepalese
# Whole Duck
# Labor Day
# Oatmeal
# Swedish
# Tilapia
# Mango
# Hunan
# Chinese
# Ice Cream
# Turkey Breasts
# Healthy
# Beef Sandwiches
# Crawfish
# Memorial Day
# Beef Organ Meats
# Chilean
# Spinach
# European
# Penne
# Black Beans
# High In... Diabetic Friendly
# Rabbit
# Onions
# Beans
# Chicken Livers
# Venezuelan