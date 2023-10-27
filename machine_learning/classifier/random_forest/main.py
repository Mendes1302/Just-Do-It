from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from music_style import Mustyle
import uvicorn

class MustyleAPI:
    def __init__(self):
        """
        Initializes the MustyleAPI with a FastAPI instance.

        The constructor sets up the FastAPI application and middleware for Cross-Origin Resource Sharing (CORS).

        Attributes:
            app (FastAPI): The FastAPI application.
        """
        self.app = FastAPI(
            title="Mustyle API",
            description="An API for predicting music style",
            version="1.0.0"
        )

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )


    def setup_routes(self):
        """
        Set up API routes and their corresponding handlers.

        This method defines the API routes using FastAPI decorators and associates them with appropriate handler functions.
        """

        @self.app.get("/")
        def read_root():
            """
            Root endpoint.

            Returns a welcome message when accessing the root endpoint.
            """
            return {'hello': 'Welcome to Mustyle!!!'}


        @self.app.get("/api/v1/predict_style")
        async def predict_style(song: str):
            """
            Predict the music style for a given song.

            Args:
                song (str): The lyrics of the song for which you want to predict the music style.

            Returns:
                dict: A dictionary containing the predicted music style and prediction accuracy.
            """
            if not song:
                raise HTTPException(status_code=400, detail="The 'song' parameter is required.")
        
            music = Mustyle()
            classify = music.download_model("ai_component_cla_lyrics.mustyle")
            music.set_classify(classify)
            results = music.predict_value(song)
  
            return {"results": results}


    def run(self, host="127.0.0.1", port=8000):
        """
        Start the FastAPI application.

        Args:
            host (str): The host IP address or hostname to bind to.
            port (int): The port number to listen on.
        """
        self.setup_routes()
        uvicorn.run(self.app, host=host, port=port)


if __name__ == "__main__":
    mapi = MustyleAPI()
    mapi.run()