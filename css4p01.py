# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 16:22:00 2024

@author: pmichael
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#to ignore warnings
import warnings
warnings.filterwarnings('ignore')



file = pd.read_csv("movie_dataset.csv")

df = pd.DataFrame(file)
#print(df.head())

print("\n\nAnswers to questions:\n\n")

#Highest rated movie
print(df[df["Rating"] ==df["Rating"].max()],"\n")

print("1. Highest rated movie is :","The Dark Knight\n")

#Average revenue of all movies in the datasheet
#NaN values were not cleaned out, as this will eliminate some of the from the dataframe such losing valuable information.
#Since the movies are independent, we cannot fill NANs with means or modes.

print(df.describe())
print("\n2. Average revenue of all movies in the datasheet = ",82.956376,"Millions\n")

# Average revenue of movies from 2015 to 2017
#extract data for 2015 to 2017 and describe it.

MV2015_2017 = df.loc[df["Year"].isin([2015,2016,2017])]

print(MV2015_2017.describe())
print("\n3. Average revenue of movies from 2015 to 2017 = ",63.099906,"Millions\n")

#How many movies released in 2016

print(df[df["Year"] ==2016].count())
print("\n4. Number of movies released in 2016 = ",297 ,"\n")

#How many movies directed by Christopher Nolan

print(df[df["Director"] =="Christopher Nolan"].count())

print("\n5. Number of movies directed by Christopher Nolan = ", 5,"\n" )

#Number of movies with rating>=8

print(df[df["Rating"] >=8].count())
print("\n6.Number of movies with rating of at least 8.0 = ", 78,"\n")

#median of movies directed by Christopher Nolan

by_Chris = df[df["Director"] =="Christopher Nolan"]
print(by_Chris["Rating"].median())
print("\n7. Median of movies directed by Christopher Nolan = ",8.6, "\n")

# The year with the highest average rating

by_year = df.groupby("Year")["Rating"]

print(by_year.max()," \n\n8. The year with highest average rating is :", by_year.max().idxmax(),"\n")

# % increase in number of movies between 2006 and 2016

year = df.groupby("Year")["Title"].count()

P_increase = ((year[2016] - year[2006])/year[2006])*100


print("\n9. Percentage increase is :", P_increase,"%\n")

#The most common actor in all the movies
#First split up the actors and concatenate them to a single  column.

Actors_1 = df['Actors'].str.split(",",expand=True)
Actors_1.columns = ["A","B","C","D"]
#Actors_1

# merge the columns into one
Act = pd.concat([Actors_1['A'], Actors_1['B'], Actors_1['C'], Actors_1['D']])

print(Act.describe())
print(Act.value_counts())
#Christian Bale           11
#Mark Wahlberg            11
#Both Christian Bale and Mark Wahlberg would be correct
print("\n10. The most common actor in all the movies is =","Christian Bale and Mark Wahlberg \n")

#How many unique Genre are in the datasheet
#First, split up the genres and concatenate them to a single column.

gen_1 = df['Genre'].str.split(",",expand=True)
gen_1.columns = ["A","B","C"]
#gen_1

# merge the columns into one
genre = pd.concat([gen_1['A'], gen_1['B'], gen_1['C']])

print(genre.describe())
print("\n11. The number of unique Genres in the datasheet is = ",20,"\n")

#Correlation between numerial features
#Mention atleast 5 insights
"""
1. positive strong correlation between the Metascore and Rating
2.positive strong correlation between the Revenue and Votes
3.positive correlation between the votes and Rating
4. weak negative correlation between the Revenue and Rank
5.positive correlation between the Runtime and rating, votes, revenue

PS: it would be better if one could determine the correlation between the Title, actors, directors, and numerical features
in order to advise better.

"""
#what advice can you give directors to produce better movies
"""
1. Use the best actors.
2. Keep up with technological advancements
3. Focus on Genres that generate the most revenue

"""


print("\n12. Correlation between numerial features:\n\n",df.corr(numeric_only=True))










































