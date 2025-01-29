# Movie Recommendation System

This project is a **Movie Recommendation System** built using **Flask** and **Pandas**. It allows users to select movie genres and get personalized movie recommendations based on average ratings.

## Features
- 🎯 **Personalized Recommendations**: Get movie recommendations based on selected genres.
- 🔍 **Smart Search**: Filter movies easily by genre.
- ⭐ **Rating System**: Recommendations include average ratings and number of ratings.

## Installation
### Prerequisites
- Python 3.x
- Flask
- Pandas

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/movie-recommendation-system.git
   cd movie-recommendation-system
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Place the required CSV files inside the `data/` directory:
   - `movies.csv`
   - `ratings.csv`

## Running the Application
1. Start the Flask server:
   ```sh
   python app.py
   ```
2. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## API Endpoints
### 1. Home Page
- **Route**: `/`
- **Method**: GET
- **Description**: Loads the homepage with a list of genres.

### 2. Get Recommendations
- **Route**: `/api/recommend`
- **Method**: POST
- **Request Body** (JSON):
  ```json
  {
    "genres": ["Comedy", "Drama"]
  }
  ```
- **Response** (JSON):
  ```json
  [
    {
      "title": "Movie Name",
      "rating": 4.5,
      "num_ratings": 200
    }
  ]
  ```

## File Structure
```
├── app.py             # Flask backend
├── templates/
│   ├── index.html     # Main frontend UI
├── data/
│   ├── movies.csv     # Movie dataset
│   ├── ratings.csv    # Ratings dataset
├── static/            # CSS, JS files (if needed)
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
```

## Author
Created by **Priyanshu Upadhyay**



