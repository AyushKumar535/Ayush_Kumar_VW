from flask import Flask, render_template_string

app = Flask(__name__)

# Inappropriate word list
inappropriate_words = ["dumb", "stupid"]

# Sample comments data
comments = [
    {
        "username": "John",
        "comment": "This product is good",
        "likes": 120,
        "flagged": False
    },
    {
        "username": "Jane",
        "comment": "This product is absolutely dumb",
        "likes": 50,
        "flagged": True
    },
    {
        "username": "Max",
        "comment": "I think this is a really stupid product, wouldn't recommend it",
        "likes": 150,
        "flagged": False
    },
    {
        "username": "Alice",
        "comment": "Really long comment" + " " * 190 + "This is a detailed explanation",
        "likes": 200,
        "flagged": True
    }
]

# Function to replace inappropriate words in the comment
def filter_inappropriate_words(comment):
    for word in inappropriate_words:
        comment = comment.replace(word, "[filtered]")
    return comment

# Function to apply the transformations and filters
def process_comment(comment_data):
    username = comment_data['username'].upper()
    comment = comment_data['comment'].strip()
    comment = filter_inappropriate_words(comment)
    
    # Conditional styling
    styles = []
    if comment_data['flagged']:
        styles.append('highlighted')
    if comment_data['likes'] > 100:
        styles.append('trending')
    if len(comment) > 200:
        styles.append('long-post')

    return {
        'username': username,
        'comment': comment,
        'likes': comment_data['likes'],
        'flagged': comment_data['flagged'],
        'styles': ' '.join(styles)
    }

# Route to display the comments
@app.route('/')
def index():
    # Process each comment
    processed_comments = [process_comment(comment) for comment in comments]

    # Calculate statistics
    total_comments = len(comments)
    total_flagged_comments = len([c for c in comments if c['flagged']])
    most_liked_comment = max(comments, key=lambda x: x['likes']) if comments else None
    usernames_joined = ', '.join([c['username'].upper() for c in comments])

    # HTML Template with embedded CSS
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Comments</title>
        <style>
            /* Base styles */
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f4f4f4;
            }

            h1 {
                color: #333;
            }

            /* Styling for flagged comments */
            .highlighted {
                color: red;
            }

            /* Styling for trending comments */
            .trending {
                font-weight: bold;
            }

            /* Styling for long posts */
            .long-post {
                font-style: italic;
            }

            .flagged {
                color: red;
                font-weight: bold;
            }

            ul {
                list-style-type: none;
                padding: 0;
            }

            li {
                margin: 10px 0;
                padding: 10px;
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 5px;
            }

            li:hover {
                background-color: #f0f0f0;
            }
        </style>
    </head>
    <body>

        <h1>Comments</h1>

        <p>Total Comments: {{ total_comments }}</p>
        <p>Total Flagged Comments: {{ total_flagged_comments }}</p>
        <p>Most Liked Comment: {{ most_liked_comment.username }} with {{ most_liked_comment.likes }} likes</p>
        <p>Usernames: {{ usernames_joined }}</p>

        <ul>
            {% for comment in processed_comments %}
                <li class="{{ comment.styles }}">
                    <strong>{{ comment.username }}:</strong> {{ comment.comment }} 
                    <br>Likes: {{ comment.likes }} 
                    {% if comment.flagged %}
                        <span class="flagged">[Flagged]</span>
                    {% endif %}
                </li>
            {% endfor %}
        </ul>

    </body>
    </html>
    '''

    return render_template_string(html_content, 
                                  processed_comments=processed_comments, 
                                  total_comments=total_comments, 
                                  total_flagged_comments=total_flagged_comments, 
                                  most_liked_comment=most_liked_comment, 
                                  usernames_joined=usernames_joined)


if __name__ == '__main__':
    app.run(debug=True)