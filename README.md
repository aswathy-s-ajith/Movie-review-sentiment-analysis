# sentiment_analyser
# Movie Review Sentiment Analysis

## Overview

This project analyzes movie reviews to determine the sentiment of the comments. Users can input the name of a movie, and the application will fetch reviews, perform sentiment analysis, and display the results along with a bar graph showing the distribution of sentiments (Positive, Negative, Neutral).

## Features

- **Input Movie Name:** Users can enter the name of a movie to analyze.
- **Fetch Reviews:** Retrieves reviews for the specified movie.
- **Sentiment Analysis:** Analyzes the sentiment of each review using Natural Language Processing.
- **Visualize Results:** Displays a bar graph of sentiment distribution.

## Technologies Used

- **Flask:** Web framework for building the web application.
- **NLTK (VADER):** Sentiment analysis using VADER (Valence Aware Dictionary and sEntiment Reasoner).
- **IMDbPY:** Library to fetch movie reviews from IMDb.
- **Matplotlib:** Used to generate and save the sentiment distribution bar graph.
- **HTML/CSS:** For the user interface.

## Setup

### Prerequisites

Make sure you have Python installed. You will also need to install the following Python packages:

- Flask
- NLTK
- IMDbPY
- Matplotlib

You can install these packages using pip:

```bash
pip install flask nltk IMDbPY matplotlib
