# Mustyle - Music Genre Classification

Mustyle is a Python program for classifying music genres based on song lyrics. It uses a RandomForest classification model and is designed to work with Portuguese song lyrics. This README provides instructions on how to use the program and what it does.

## Features

- Loads a dataset of song lyrics.
- Performs data preprocessing, including cleaning and normalizing lyrics.
- Trains a classification model using a RandomForest classifier.
- Displays model evaluation metrics, including a classification report.
- Predicts the music genre of a song based on its lyrics.
- Saves the trained model for future use.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (3.10+)
- Required Python packages (install using `pip`):
  - scikit-learn
  - pandas
  - nltk
  - joblib

### Usage (Component)
  1. Import Libraries
   ```python
    # Import the necessary libraries
    import joblib
   ```
  2. Load the Trained Model
   ```python
    # Specify the path to the saved model file
    component_name = 'ai_component_cla_lyrics.mustyle'
    
    # Load the trained classification model using joblib
    component_ai = joblib.load(component_name)
   ```
  3. Make Predictions
   ```python
    # Input the lyrics of a song you want to classify
    song_lyrics = "This is the lyrics of a song."
    
    # Use the trained model to predict the music genre probabilities
    genre_probabilities = component_ai.predict_proba([song_lyrics])
    
    # Display the predicted genre probabilities
    print(genre_probabilities)
   ```

  4. Complete Code Example
   ```python
    import joblib
    
    component_name = 'ai_component_cla_lyrics.mustyle'
    song_lyrics = "This is the lyrics of a song."
    component_ai = joblib.load(component_name)
    genre_probabilities = component_ai.predict_proba([song_lyrics])
    
    print(genre_probabilities)

   ```
