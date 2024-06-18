'''File used to inialize, run webserver, and create the app object'''
from website.Backend import create_app
from flask import jsonify, Response
app = create_app()
# This is a route that returns a json object
@app.route('/api/members', methods=['GET'])
def members():
    return jsonify({"members" : ["member1", "member2", "member3"]})

if __name__ == '__main__':
    # Runs the app in debug mode
    # only runs the webserver when the main file is called
    # this is for production purposes only
    app.run(debug=True)