# CONTENT-BASED MOVIE RECOMMENDATION SYSTEM
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaoji (Jay) Wang - SPRING 2024 Semester
- Author: Yashwanth Atluri
- GitHub: https://github.com/YASHCHOWDARY/UMBC-DATA606-Capstone
- Linkedin: https://www.linkedin.com/in/yashwanthatluri/


## 2. BACKGROUND
* The project aims to build a predictive model to Design and implement a content-based movie recommendation system that leverages movie features and user preferences to deliver       personalized and accurate movie suggestions, enhancing user engagement and satisfaction.

* Research Questions :
   1. How can movie features be optimally combined for effective content-based recommendations?
   2. How can user profiles dynamically evolve for improved accuracy in content-based movie suggestions?
   3. Which metrics best evaluate the performance of content-based movie recommendation systems?

## 3. DATA

Description : 

1. Data Source : *[Kaggle](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset/data)*. :link:

2. Data Size 
   > - Movies.csv = 560kb
   > - Rating.csv = 2.5MB


3. Data Shape
   - Movies.csv
    > - Number of rows    = 10329
    > - Number of columns =  3
    
   - Rating.csv  
   > - Number of rows = 105339
   > - Number of columns  = 4

4. What does each row represent?(a patient, a school, a crime, etc.)
The "Movies Dataset" contains movie-related information, including columns such as movie ID, title, and genres, with examples like unique identifiers (movieId), movie titles, and associated genres.  The "Ratings Dataset" comprises information on user-movie interactions, with columns like user ID, movie ID, rating (on a scale, e.g., 1 to 5 stars), and timestamp, featuring unique identifiers for users (userId) and movies (movieId).

5. Data dictionary:


                                   Movies.csv
| Column Name  | Data Type | Definition                                          | Potential Values (Categorical)   |
|--------------|-----------|-----------------------------------------------------|----------------------------------|
| movieId      | int       | Unique identifier for each movie                    | '189'                            |
| title        | str       | Movie title                                         | 'Toy story'                      |
| genres       | str       | Genres associated with the movie                    | Action, Comedy, Drama, ...       |
| releaseYear  | int       | Year the movie was released                         | '1991'                           |

                                   Rating.csv
| Column Name  | Data Type | Definition                                          | Potential Values (Categorical)   |
|--------------|-----------|-----------------------------------------------------|----------------------------------|
| userId       | int       | Unique identifier for each user                     | 1,2,3..                          |
| movieId      | int       | Unique identifier for each movie                    | 170,165..                        |
| rating       | float     | User rating for the movie (e.g., on a scale 1-5)    | 1.0, 2.5, 4.5, ...               |
| timestamp    | datetime  | Timestamp of when the rating was given              | 1217895807                       |
                             
5. Which variable/column will be your target/label in your ML model?
    - Movies                 
6. Which variables/columns may selected as features/predictors for your ML models?
   - genres
   - rating 
