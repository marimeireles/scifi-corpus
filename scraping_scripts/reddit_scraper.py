import praw
import json

reddit = praw.Reddit(
    client_id="",  # replace with your client id
    client_secret="",  # replace with your client secret
    user_agent="",
)

# Add a subreddit name here, without the r/
subreddit = reddit.subreddit("")

# A list to store each post as a separate dictionary
posts = []

for submission in subreddit.new(limit=None):
    text = submission.selftext
    # Split the post into paragraphs
    paragraphs = text.split('\n')
    # Add each paragraph as a separate entry in the 'posts' list
    for paragraph in paragraphs:
        if paragraph:  # Ignore empty paragraphs
            post = {
                "instruction": "",
                "input": "",
                "output": paragraph
            }
            posts.append(post)

# Save the posts to a JSON file
with open('output_file.json', 'w') as f:
    json.dump(posts, f)
