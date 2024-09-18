from flask import Flask, render_template, request
from movie import fetch_movie_reviews,analyze_reviews,save_bar_graph


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    movie_name = request.form['movie_name']
    
    # Here you would fetch the actual movie reviews, using placeholder reviews for now
    reviews=fetch_movie_reviews(movie_name)
    
    if reviews:
        sentiment_results = analyze_reviews(reviews)
        save_bar_graph(sentiment_results)  # Save the bar graph image
        return render_template('result.html', movie=movie_name, results=sentiment_results)
    else:
        return render_template('index.html', error="No reviews found for this movie.")


@app.route('/plot')
def plot():
    return send_file('static/sentiment_plot.png', mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
