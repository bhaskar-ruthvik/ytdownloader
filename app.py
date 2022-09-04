from website import create_app
from pytube import YouTube

app = create_app()
if __name__ == "__main__":
    app.run(debug=True)