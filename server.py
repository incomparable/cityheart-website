from flask import Flask, request, make_response, render_template, jsonify,\
                    session, url_for, redirect

app = Flask(__name__, static_path='/static')
@app.route('/')
def home():
    templateData = {'title': 'Login Page'}
    return render_template('index.html', **templateData)


@app.route('/about')
def about():
    templateData = {'title': 'About page'}
    return render_template('about.html', **templateData)


@app.route('/features')
def features():
    templateData = {'title': 'features page'}
    return render_template('features.html', **templateData)


@app.route('/location')
def location():
    templateData = {'title': 'location page'}
    return render_template('location.html', **templateData)


@app.route('/layout')
def layout():
    templateData = {'title': 'layout page'}
    return render_template('layout.html', **templateData)


@app.route('/opportunities')
def opportunities():
    templateData = {'title': 'opportunities page'}
    return render_template('opportunities.html', **templateData)


#############################################
#                                           #
#                  MAIN SERVER              #
#                                           #
#############################################
if __name__ == '__main__':
    app.run(debug=True)
