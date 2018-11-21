import pandas as pd
import random
import numpy as np
r_cols = ['user_id', 'movie_id', 'rating']
rating = pd.read_csv('C:/gaurav/project/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('C:/gaurav/project/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, rating)
#print(rating)
ratings2=pd.merge(ratings,rating)
#print(ratings2)
movieRatings = ratings2.pivot_table(index=['user_id'],columns=['title','movie_id'],values='rating')
import numpy as np
movieStats = ratings2.groupby('movie_id').agg({'rating': [np.size, np.mean]})
popularMovies = movieStats['rating']['size'] >= 300
popular=movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:50]
#print("movie id's are ",popular.index)
#print(len(popular.index))
movieStats1 = ratings2.groupby('title').agg({'rating': [np.size, np.mean]})
popularMovies1 = movieStats1['rating']['size'] >= 300
popular1=movieStats1[popularMovies1].sort_values([('rating', 'mean')], ascending=False)[:34]
#print(popular1.index)
#print(len(popular.index))
#print(m)
