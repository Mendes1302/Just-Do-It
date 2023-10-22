from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
from sklearn import metrics
import pandas as pd
import numpy as np
import joblib 

class Mustyle:
    def __init__(self) -> None:
        """
        Class for music genre classification based on song lyrics.
        
        Initializes the data, including the DataFrame with song lyrics,
        the list of Portuguese stopwords, and variables to store the model and test data.
        """
        __url = "http://robsonfernandes.net/cci/dataset_genero_musical.xlsx"
        self._df_lyrics = pd.read_excel(__url)
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

        return results

    def save_model(self, component_name) -> None:
        """
        Saves the trained model to a file using the joblib library.

        Args:
        - component_name (str): Name of the file where the model will be saved.
        """
        joblib.dump(self.classify, component_name)


if __name__ == '__main__':
    song = """
                Quem me dera ao menos uma vez
                Ter de volta todo o ouro que entreguei a quem
                Conseguiu me convencer que era prova de amizade
                Se alguém levasse embora até o que eu não tinha
                Quem me dera ao menos uma vez
                Esquecer que acreditei que era por brincadeira
                Que se cortava sempre um pano de chão
                De linho nobre e pura seda
                Quem me dera ao menos uma vez
                Explicar o que ninguém consegue entender
                Que o que aconteceu ainda está por vir
                E o futuro não é mais como era antigamente
                Quem me dera ao menos uma vez
                Provar que quem tem mais do que precisa ter
                Quase sempre se convence que não tem o bastante
                Fala demais por não ter nada a dizer
                Quem me dera ao menos uma vez
                Que o mais simples fosse visto
                Como o mais importante
                Mas nos deram espelhos e vimos um mundo doente
    """
    
    mustyle = Mustyle()
    mustyle.data_pre_processing()
    mustyle.training_model()
    mustyle.predict_value(song)
    mustyle.save_model('ai_component_cla_lyrics.mustyle')