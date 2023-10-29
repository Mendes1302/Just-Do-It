# Mustyle - Music Genre Classification

Mustyle is a Python program for classifying music genres based on song lyrics. It uses a RandomForest classification model and is designed to work with Portuguese song lyrics. This README provides instructions on how to use the program and what it does.

## Creaters
- Lucas Mendes Barbosa


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
  - uvicorn
  - fastapi

### Usage (API)

The Mustyle API allows you to predict music styles based on song lyrics. Below, you'll find information on how to use the API, along with examples of making requests.

#### API Base URL

The base URL for the Mustyle API is `http://127.0.0.1:8000/` by default. You can replace this with the appropriate URL if you deploy the API to a different location.

#### Predict Music Style

To predict the music style for a given song, you can make a GET request to the `/api/v1/predict_style` endpoint. You need to provide the song lyrics as a query parameter.

#### Endpoint
> GET /api/v1/predict_style


#### Parameters

- `song` (string): The lyrics of the song for which you want to predict the music style.

#### Example Request

You can make a GET request to the API using various tools, libraries, or programming languages. Below is an example using Python's `requests` library:

```python
import requests

# Specify the API endpoint URL
api_url = "http://127.0.0.1:8000/api/v1/predict_style"

# Define the query parameter
song_lyrics = "Your song lyrics go here"
params = {"song": song_lyrics}

# Make a GET request to the API
response = requests.get(api_url, params=params)

# Check the API response and extract the predicted style
if response.status_code == 200:
    result = response.json()
    predicted_style = result['results']['predicted_style']
    accuracy = result['results']['accuracy']
    print(f"Predicted Style: {predicted_style}")
    print(f"Accuracy: {accuracy}")
else:
    print("Error:", response.status_code, response.text)
```
#### Example Response
```
{
    "results": {
        "predicted_style": "Pop",
        "accuracy": 0.85
    }
}
```

