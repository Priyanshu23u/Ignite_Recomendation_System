from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the data
movies_df = pd.read_csv('data/movies.csv')
ratings_df = pd.read_csv('data/ratings.csv')

# Create a merged dataset for recommendations
merged_data = pd.merge(ratings_df, movies_df, on='movieId')

def get_movie_recommendations(selected_genres, top_n=10):
    if not selected_genres:
        return []
    
    # Filter movies that contain any of the selected genres
    genre_filter = '|'.join(selected_genres)
    filtered_movies = merged_data[merged_data['genres'].str.contains(genre_filter, case=False, na=False)]
    
    if filtered_movies.empty:
        return []
    
    # Calculate average ratings and number of ratings for each movie
    movie_stats = filtered_movies.groupby('title').agg({'rating': ['mean', 'count']}).reset_index()
    
    # Flatten column names
    movie_stats.columns = ['title', 'rating', 'rating_count']
    
    # Filter movies with at least 20 ratings to ensure quality
    qualified_movies = movie_stats[movie_stats['rating_count'] >= 20]
    
    # Sort by rating and get top N movies
    top_movies = qualified_movies.sort_values(by=['rating', 'rating_count'], ascending=[False, False]).head(top_n)
    
    # Convert to dictionary format
    recommendations = top_movies.apply(
        lambda x: {
            'title': x['title'],
            'rating': round(x['rating'], 1),
            'num_ratings': int(x['rating_count'])
        }, 
        axis=1
    ).tolist()
    
    return recommendations

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/explore')
def index():
    # Extract unique genres from the dataset
    all_genres = set()
    for genres in movies_df['genres'].dropna().str.split('|'):
        all_genres.update(genres)
    
    # Remove duplicates and sort
    genres_list = sorted(list(all_genres))
    return render_template('index.html', genres=genres_list)

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    selected_genres = data.get('genres', [])
    
    try:
        recommendations = get_movie_recommendations(selected_genres)
        return jsonify({'recommendations': recommendations})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
