country = input('Spain') # Add country name
visits = int(12) # Number of visits
list_of_cities = input(['Madrid', 'Barcelona', 'Seville']) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(countries,number_visits, list_of_city):
  new_country = {
    "country": countries,
    "visits": number_visits,
    "cities": list_of_city,
  }
  travel_log.append(new_country)
  
# Do not change the code below 👇
add_new_country(country,visits,list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities']}.")