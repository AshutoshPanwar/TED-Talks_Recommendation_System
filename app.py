from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import pearsonr
import string
import nltk
from nltk.corpus import stopwords
import re

# Initialize Flask application
app = Flask(__name__)

# Load your cleaned TED Talks dataset
df = pd.read_csv('tedx_dataset.csv')

# Assuming 'title' and 'author' are suitable for content-based recommendation
data = df[['title', 'author', 'date', 'views', 'likes', 'link']]

# Preprocess text data
nltk.download('stopwords')

def preprocess_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    stopwords_set = set(stopwords.words('english'))
    cleaned_text = ' '.join(word for word in text.lower().split() if word not in stopwords_set)
    return cleaned_text

# Preprocess the 'title' column
data['title_cleaned'] = data['title'].apply(preprocess_text)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(analyzer='word', max_features=1000)
tfidf_matrix = vectorizer.fit_transform(data['title_cleaned'])

# Function to extract TED Talk ID from URL
def get_ted_id(url):
    """
    Extracts the TED Talk ID from the URL.
    Returns None if the URL format is invalid.
    """
    try:
        talk_id = re.search(r'talks/([^/]+)', url)
        if talk_id:
            return talk_id.group(1)
        else:
            return None
    except Exception as e:
        print(f"Error extracting TED Talk ID: {e}")
        return None

# Function to get similarities
def get_similarities(talk_content, tfidf_matrix):
    talk_tfidf = vectorizer.transform([talk_content])
    cosine_similarities = cosine_similarity(talk_tfidf, tfidf_matrix)
    pearson_correlations = [pearsonr(talk_tfidf.toarray().flatten(), tfidf_vector.toarray().flatten())[0]
                            for tfidf_vector in tfidf_matrix]

    return cosine_similarities[0], pearson_correlations

# Function to recommend talks
def recommend_talks(talk_content, data, tfidf_matrix):
    cosine_similarities, pearson_correlations = get_similarities(talk_content, tfidf_matrix)

    # Combine similarities with original data
    data['cosine_similarity'] = cosine_similarities
    data['pearson_correlation'] = pearson_correlations

    # Sort by similarities
    recommended_talks = data.sort_values(by=['cosine_similarity', 'pearson_correlation'], ascending=[False, False])

    return recommended_talks[['title', 'author', 'date', 'views', 'likes', 'link']].head(20)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and show recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user input (talk content)
    talk_content = request.form.get('talk_content')

    # Get recommendations
    recommendations = recommend_talks(talk_content, data, tfidf_matrix)

    # Pass recommendations and get_ted_id function to template
    return render_template('recommendations.html', recommendations=recommendations, get_ted_id=get_ted_id)

if __name__ == '__main__':
    app.run(debug=True)
