'''File used to inialize, run webserver, and create the app object'''
from website import create_app

app = create_app()

if __name__ == '__main__':
    # Runs the app in debug mode
    # only runs the webserver when the main file is called
    # this is for production purposes only
    app.run(debug=True)