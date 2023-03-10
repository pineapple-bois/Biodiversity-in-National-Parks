# Biodiversity in National Parks

This is my second [Codecademy](https://www.codecademy.com/pages/data-science-career-specializations) portfolio project.

It was an open-ended exploratory data analysis project where we would discover any patterns to the types of species that become endangered. 

----

### We were given two datasets; 

----

#### `species_info.csv` containing information on the different species in the National Parks along with their conservation status.

With columns; 

- `category` - class of animal
- `scientific_name` - the scientific name of each species
- `common_name` - the common names of each species
- `conservation_status` - each species’ current conservation status

This dataset was an abridged version of a similar set on [Kaggle](https://www.kaggle.com/datasets/nationalparkservice/park-biodiversity?select=species.csv)

----

#### `observations.csv`; contains information from recorded sightings of different species over a seven-day period.

With columns; 

- `scientific_name` - the scientific name of each species
- `park_name` - National Park where species were found
- `observations` - the number of times each species was observed at park in the past 7 days

This dataset was entirely fictional. 
Merging the two gave the opportunity to explore trends within `species_info.csv`

----

### Four National Parks in the United States of America were represented.

<img src="Images/National Park Map.png"/>

----

### The focus of the project was biodiversity. 
#### I decided to centre my analysis on birds of prey both protected and non-protected.

----

Birds of prey, also known as raptors, are considered important 'indicator species' of biodiversity. They perform an important role in maintaining the balance of ecosystems by controlling populations of small mammals, reptiles and other birds. 

Raptors are top predators and occupy a high trophic level, making them sensitive to changes in the food web and in their prey populations. As such, changes in raptor populations can indicate shifts in ecosystem health and the presence of toxic substances, such as pesticides and heavy metals. 

Raptors require large territories and diverse habitats to survive making them effective indicators of the overall health of ecosystems. As species with a long lifespan and low reproductive rate, they are very sensitive to long-term environmental changes, such as habitat loss and degradation. 

----

#### Technologies used:
```
Git Zsh
Jupyter Notebooks
```
#### Libraries used:
```
pandas
matplotlib.pyplot
matplotlib.patches
seaborn
numpy
```
#### Techniques used:
```
DataFrame manipulation
Data wrangling using regex
Visualisations
```
#### Images:

- Images were sourced royalty free from [Pixabay](https://pixabay.com)
- Map of the USA from [Google Earth](https://earth.google.com/web/@39.00737915,-95.31864374,-81.61621475a,5326276.02988026d,35y,0h,0t,0r)

#### References:

- [Wikipedia](https://en.wikipedia.org/wiki/Bird_of_prey)
- [US National Parks Service](https://www.nps.gov/index.htm)

----