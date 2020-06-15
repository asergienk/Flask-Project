from flask import Flask, make_response, request, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    context = {
        'text': 'This is text from context',
        'name': 'Anna'
    }
    return render_template('index.html', data = context)


@app.route('/contact')
def Contact():
    return render_template('contact.html')


@app.route('/about')
def About():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')
















if __name__ == "__main__":
    app.run(debug=True)