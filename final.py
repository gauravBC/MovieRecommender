import pandas as pd
import csv
import random
import numpy as np
t=list
t=[ 50,  98, 127, 174, 313, 172, 173, 100, 168,  56,  79, 181, 195,
            210, 269,   1,  69, 204, 423, 258,   7, 257, 237, 117, 222, 286,
            151, 300, 288, 121, 405, 294, 748]
df = pd.DataFrame(data=np.array(t), index=range(33), columns=['movie_id'])
#print(popular)
#df.insert(0,'movie_id':[50, 98, 127, 174, 313, 172, 173, 100, 168, 56, 79, 181, 195, 210, 269, 1, 69, 204, 423, 258, 7, 257, 237, 117, 222, 286, 151, 300, 288, 121 ,405, 294, 748, 50, 98, 127, 174, 313])
t2=['Star Wars (1977)', 'Silence of the Lambs, The (1991)',
       'Godfather, The (1972)', 'Raiders of the Lost Ark (1981)',
       'Titanic (1997)', 'Empire Strikes Back, The (1980)',
       'Princess Bride, The (1987)', 'Fargo (1996)',
       'Monty Python and the Holy Grail (1974)', 'Pulp Fiction (1994)',
       'Fugitive, The (1993)', 'Return of the Jedi (1983)',
       'Terminator, The (1984)', 'Indiana Jones and the Last Crusade (1989)',
       'Full Monty, The (1997)', 'Toy Story (1995)', 'Forrest Gump (1994)', 'Back to the Future (1985)',
       'E.T. the Extra-Terrestrial (1982)', 'Contact (1997)',
       'Twelve Monkeys (1995)', 'Men in Black (1997)', 'Jerry Maguire (1996)',
       'Rock, The (1996)', 'Star Trek: First Contact (1996)',
       'English Patient, The (1996)',
       'Willy Wonka and the Chocolate Factory (1971)', 'Air Force One (1997)',
       'Scream (1996)', 'Independence Day (ID4) (1996)',
       'Mission: Impossible (1996)', 'Liar Liar (1997)', 'Saint, The (1997)']
#print("id's len is ",len(t))
#print("Movies length is ",len(t2))

raw_data={'movie_id' : t, 'title' : t2}
xyz=pd.DataFrame(data=raw_data,columns=['movie_id','title'])
top3=xyz.take(np.random.permutation(len(xyz))[:3])
print("three popular and high rated movies are ")
print(top3.to_string(index=False))
m=list()
for index, row in top3.iterrows():
    m.append(row['movie_id'])
print('rate the above movies in order')
x=0
a=0
while x<3 :
    a=int(input())
    if a>=0 and a<=5:
        m.append(a)
        x=x+1
    else:
        print("enter a rating btwn 0-5")
t=list
t=m
r_cols = ['user_id', 'movie_id', 'rating']
ratings1 = pd.read_csv('C:/Users/Hewlett packard/PycharmProjects/learning/database/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")
m_cols = ['movie_id', 'title']
movies = pd.read_csv('C:/gaurav/project/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")
ratings1.loc[0,'movie_id'] =t[0]
ratings1.loc[0,'rating'] =t[3]
ratings1.loc[1,'movie_id'] =t[1]
ratings1.loc[1,'rating'] =t[4]
ratings1.loc[2,'movie_id'] =t[2]
ratings1.loc[2,'rating'] =t[5]
ratings = pd.merge(movies, ratings1)
userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
corrMatrix = userRatings.corr(method='pearson', min_periods=100)
myRatings = userRatings.loc[945].dropna()
print("the ratings which you gave")
print(myRatings)
#print(len(myRatings))
print(" ")
simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    #print("Adding sims for " + myRatings.index[i] + "...")
    # Retrieve similar movies to this one that I rated
    sims = corrMatrix[myRatings.index[i]].dropna()
    # Now scale its similarity by how well I rated this movie
    sims = sims.map(lambda x: x * myRatings[i])
    # Add the score to the list of similarity candidate
    simCandidates = simCandidates.append(sims)

#Glance at our results so far:
#print ("sorting...")
simCandidates.sort_values(inplace = True, ascending = False)
#print(simCandidates.head(10))
simCandidates = simCandidates.groupby(simCandidates.index).sum()
simCandidates.sort_values(inplace = True, ascending = False)
#print(simCandidates.head(10))
filteredSims = simCandidates.drop(myRatings.index)
print(" ")
print("Recommended movies are")
print(" ")
print(filteredSims.head(10))

