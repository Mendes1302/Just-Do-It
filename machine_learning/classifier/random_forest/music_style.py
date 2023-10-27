from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
from sklearn import metrics
from os import environ
import pandas as pd
import joblib 
import nltk
nltk.download('stopwords')

class Mustyle:
    def __init__(self) -> None:
        """
        Class for music genre classification based on song lyrics.
        
        Initializes the data, including the DataFrame with song lyrics,
        the list of Portuguese stopwords, and variables to store the model and test data.
        """
        __url = "http://robsonfernandes.net/cci/dataset_genero_musical.xlsx"
        self._df_lyrics = pd.read_excel(__url, engine="openpyxl")
        self._list_stops_words = stopwords.words("portuguese")
        self.classify = None
        self.X_test = None
        self.y_test = None


    def data_pre_processing(self) -> None:
        """
        Performs data preprocessing, including cleaning and normalizing song lyrics.
        """
        _df_lyrics = self._df_lyrics
        _df_lyrics.dropna(inplace=True)
        _df_lyrics["musica"].replace(r'[^\w\s]','', regex=True, inplace=True)
        _df_lyrics["musica"] = _df_lyrics['musica'].str.lower()
        _df_lyrics["musica"].replace('\n',' ', regex=True, inplace=True)
        self._df_lyrics = _df_lyrics


    def show_metrics(self) -> None:
        """
        Displays model metrics, including the classification report.
        """
        preds = self.classify.predict(self.X_test)
        print(metrics.classification_report(self.y_test, preds))


    def training_model(self, ngram = (1, 3), n_estimators = 200) -> None:
        """
        Trains the classification model based on song lyrics.

        Args:
        - ngram (tuple): Range of n-grams to consider (default: (1, 3)).
        - n_estimators (int): Number of estimators in the RandomForest model (default: 200).
        """
        X_train, X_test, y_train, y_test = train_test_split(self._df_lyrics["musica"], 
                                                            self._df_lyrics["genero"],
                                                            test_size=0.30, 
                                                            random_state=42) 
        classify = Pipeline(
                [('vect', CountVectorizer(stop_words= self._list_stops_words, ngram_range=ngram)),
                 ('clf',  RandomForestClassifier(n_estimators=n_estimators)),
                 ])
        
        classify.fit(X_train, y_train)

        self.classify = classify
        self.X_test = X_test
        self.y_test = y_test

        self.show_metrics()


    def predict_value(self, song) -> pd.DataFrame:
        """
        Predicts the music genre based on a song's lyrics.

        Args:
        - song (str): Lyrics of the song to be classified.

        Returns:
        - results (DataFrame): DataFrame with music genre classes and prediction values.
        """
        classes = self.classify.classes_.tolist()
        predict_value = self.classify.predict_proba([song]).tolist()[0]
        dict_values = {"classes": classes,
                       "predict_value": predict_value}
        results = pd.DataFrame(dict_values)               
        results.sort_values(by=['predict_value'], ascending=False, inplace=True)
        print(results.classes[0], " = ", results.predict_value[0], "%")

        return {results.classes[0]: results.predict_value[0]}


    def save_model(self, component_name) -> None:
        """
        Saves the trained model to a file using the joblib library.

        Args:
        - component_name (str): Name of the file where the model will be saved.
        """
        joblib.dump(self.classify, component_name)


    def download_model(self, component_name):
        """
        Loads a model using joblib.load from the path specified in the environment variable with the given name.

        Args:
            component_name (str): The name of the environment variable that contains the path to the model.

        Returns:
            object: The model loaded from the path specified in the environment variable.

        Raises:
            KeyError: If the environment variable with the name `component_name` is not defined.
            
        Example:
            To load a model with the name "my_model" from the environment variable, you can use:

            >>> my_class = YourClass()
            >>> loaded_model = my_class.download_model("ai_component_cla_lyrics.mustyle")
        """
        return joblib.load(environ[component_name])
   
    
    def set_classify(self, classify):
        """
        Sets the instance variable `classify` to a specified value, after download_model.

        Args:
            classify: The value you want to set for the `classify` variable.

        Returns:
            None

        Example:
            To set the `classify` variable to True, you can use:

            >>> my_class = YourClass()
            >>> my_class.set_classify(classify)
        """
        self.classify = classify