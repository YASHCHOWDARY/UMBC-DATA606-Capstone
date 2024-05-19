# CONTENT-BASED MOVIE RECOMMENDATION SYSTEM

**Prepared for UMBC Data Science Master Degree Capstone by Dr Chaoji (Jay) Wang - SPRING 2024 Semester**

**Author: Yashwanth Atluri**
- **GitHub:** [YASHCHOWDARY/UMBC-DATA606-Capstone](https://github.com/YASHCHOWDARY/UMBC-DATA606-Capstone)
- **LinkedIn:** [yashwanthatluri](https://www.linkedin.com/in/yashwanthatluri/)

## 2. BACKGROUND
The project aims to build a predictive model to design and implement a content-based movie recommendation system that leverages movie features and user preferences to deliver personalized and accurate movie suggestions, enhancing user engagement and satisfaction.

### Research Questions:
1. How can movie features be optimally combined for effective content-based recommendations?
2. How can user profiles dynamically evolve for improved accuracy in content-based movie suggestions?
3. Which metrics best evaluate the performance of content-based movie recommendation systems?

## 3. DATA

### Description:
1. **Data Source:** [Kaggle](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset/data).

2. **Data Size:**
   - Movies.csv = 560KB
   - Rating.csv = 2.5MB

3. **Data Shape:**
   - **Movies.csv**
     - Number of rows: 10,329
     - Number of columns: 3
    
   - **Rating.csv**
     - Number of rows: 105,339
     - Number of columns: 4

4. **What does each row represent?**
   - The "Movies Dataset" contains movie-related information, including columns such as movie ID, title, and genres, with examples like unique identifiers (movieId), movie titles, and associated genres.
   - The "Ratings Dataset" comprises information on user-movie interactions, with columns like user ID, movie ID, rating (on a scale, e.g., 1 to 5 stars), and timestamp, featuring unique identifiers for users (userId) and movies (movieId).

5. **Data Dictionary:**

   **Movies.csv**
   | Column Name | Data Type | Definition                                      | Potential Values (Categorical) |
   |-------------|-----------|-------------------------------------------------|--------------------------------|
   | movieId     | int       | Unique identifier for each movie                | '189'                          |
   | title       | str       | Movie title                                     | 'Toy story'                    |
   | genres      | str       | Genres associated with the movie                | Action, Comedy, Drama, ...     |
   | releaseYear | int       | Year the movie was released                     | '1991'                         |

   **Rating.csv**
   | Column Name | Data Type | Definition                                      | Potential Values (Categorical) |
   |-------------|-----------|-------------------------------------------------|--------------------------------|
   | userId      | int       | Unique identifier for each user                 | 1,2,3..                        |
   | movieId     | int       | Unique identifier for each movie                | 170,165..                      |
   | rating      | float     | User rating for the movie (e.g., on a scale 1-5)| 1.0, 2.5, 4.5, ...             |
   | timestamp   | datetime  | Timestamp of when the rating was given          | 1217895807                     |

6. **Which variable/column will be your target/label in your ML model?**
   - Movies

7. **Which variables/columns may be selected as features/predictors for your ML models?**
   - genres
   - rating
## Exploratory Data Analysis (EDA)

### Top 10 Most Relevant Genres in Movies Dataset

![Top 10 Genres](docs/Top 10 Most revalent Genres in Movies Dataset.png)

### Top 20 Movies with Highest Ratings in Rating Dataset

![Top 20 Movies Ratings](docs/Top 20 movies with highest rating.png)

## Data Cleansing

### Handling Missing Values:

No missing values were detected in the dataset, ensuring that all records contain complete information.

### Handling Duplicate Rows:

No duplicate rows were found in the dataset, indicating data consistency and preventing redundancy.

## Model Development

### Predictive Analytics Techniques:
- For our recommendation systems, we will utilize two primary approaches: content-based filtering and collaborative filtering. Content-based filtering will focus on the properties of the items themselves, while collaborative filtering will leverage user interaction data to make predictions.

### Training Methodology:
- Our training process for content-based filtering involves several steps: first, we will preprocess the textual data to standardize and clean it. Next, we will apply Term Frequency-Inverse Document Frequency (TF-IDF) vectorization to convert text into a numerical format that can be easily processed. We will then use cosine similarity to measure the similarity between different items based on their vectorized forms. For collaborative filtering, we will adopt the nearest neighbors algorithm, which finds and uses the most similar user profiles to predict preferences for a given user.

### Required Python Libraries:
- We will leverage several Python libraries for model development and evaluation:
  - Libraries suitable for handling TF-IDF vectorization, calculating cosine similarities for content-based recommendation, and implementing the Nearest Neighbors algorithm for collaborative filtering.
  - pandas: This library is crucial for efficient data manipulation and preprocessing, allowing us to prepare our datasets for the modeling phase.

### Development Platforms:
- The development and training of our models can be conducted in various settings to accommodate different preferences and resources:
  - Locally, using tools like Jupyter Notebook provides an interactive coding environment and facilitates direct observation of code execution and results.
  - Cloud-based environments such as Google Colab and GitHub CodeSpaces offer scalable resources and ease of access without needing local setup, making them ideal for collaborative projects and high-performance computations.

### Web App Development:
- Developed a web application using Streamlit for users to interact with our trained recommendation models.

Streamlit app: [https://umbc-data606-capstone-crhlha4w5mdbxeanodzkvg.streamlit.app/]
