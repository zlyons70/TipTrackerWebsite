'''File used to inialize, run webserver, and create the app object'''
from website.Backend import create_app

app = create_app()
# This is a route that returns a json object
@app.route('/members')
def members()->dict:
    return {"members" : ["member1", "member2", "member3"]}

if __name__ == '__main__':
    # Runs the app in debug mode
    # only runs the webserver when the main file is called
    # this is for production purposes only
    app.run(debug=True)