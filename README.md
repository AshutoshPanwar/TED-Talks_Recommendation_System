![](./static/Assets/Home_preview.png)

<h1 align="center"> 🚨TED Talk Recommendation System🚨 </h1>

This project is a web-based recommendation system for TED Talks. It uses a content-based recommendation approach leveraging TF-IDF vectorization and cosine similarity to suggest similar TED Talks based on user-provided input.

## The Problem and the Solution

### The Problem

With thousands of TED Talks available, users often find it challenging to discover new talks that align with their interests based on the content of talks they have already enjoyed. Traditional recommendation systems may not effectively capture the content nuances necessary for accurate suggestions.

### The Solution

This project addresses the problem by implementing a content-based recommendation system. By analyzing the textual content of TED Talk titles, the system suggests similar talks using TF-IDF vectorization and cosine similarity. This method ensures that recommendations are based on the actual content, providing more relevant and personalized suggestions.

## Features

-   **Content-Based Recommendations**: Suggests TED Talks based on the content similarity of titles.
-   **TF-IDF Vectorization**: Utilizes TF-IDF vectorization to represent the textual data.
-   **Cosine Similarity**: Computes similarities between the user input and existing TED Talks.
-   **Flask Web Application**: Provides a simple web interface for users to input text and receive recommendations.

## Live Demo

-   **Live Link**: [TED Talk Recommendation System](https://ted-talks-recommendation-system.onrender.com/)
-   **Backup Link**: [TED Talk Recommendation System (Backup)](https://billowing-water-1149.ploomberapp.io/)

## Requirements

-   Python 3.x
-   Flask
-   pandas
-   scikit-learn
-   scipy
-   nltk
-   re

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/ted-talk-recommendation.git
    cd ted-talk-recommendation
    ```

2. **Create a virtual environment and activate it**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Download NLTK stopwords**:

    ```python
    import nltk
    nltk.download('stopwords')
    ```

5. **Ensure you have the TED Talks dataset**:
    - Place your cleaned `tedx_dataset.csv` file in the project directory.

## Usage

1. **Run the Flask application**:

    ```bash
    flask run
    ```

2. **Access the web application**:

    - Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Get recommendations**:
    - Enter a TED Talk title or content into the input field and submit to receive recommendations.

## Result Output

When a user inputs a TED Talk title or content, the system processes the input and provides a list of recommended TED Talks. Each recommendation includes:

-   **Title**: The title of the recommended TED Talk.
-   **Author**: The speaker of the recommended TED Talk.
-   **Date**: The publication date of the recommended TED Talk.
-   **Views**: The number of views the recommended TED Talk has received.

Example of result output:

![](./static/Assets/recommendatin_page.png)

## Project Structure

-   `app.py`: Main Flask application file.
-   `templates/`: Contains HTML templates for the web interface.
    -   `index.html`: Home page template.
    -   `recommendations.html`: Template to display recommendations.
-   `tedx_dataset.csv`: Dataset containing TED Talks information (make sure to place it in the project root).

## If you like my work, You can follow me on

-   **LinkedIn:** https://www.linkedin.com/in/ashutoshpanwar1100/
-   **GitHub:** https://github.com/AshutoshPanwar
-   **Twitter:** https://x.com/Ashu_Panwar1100
-   Made with ❤️ by Ashutosh Panwar
