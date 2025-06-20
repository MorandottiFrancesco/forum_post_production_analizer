import re

def split_forum_posts(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Regular expression pattern to identify the start of a new post
    pattern = r"\d{2}:\d{2}:\d{2} \w{3} \d{1,2}\w{2} \d{2} - \w+ \(\w+\):"

    # Split the text into individual posts using the pattern
    posts = re.split(pattern, text)

    # Remove any empty posts
    posts = [post.strip() for post in posts if post.strip()]

    return posts

# Example usage
file_path = 'forum_posts.txt'  # Replace with your file path
forum_posts = split_forum_posts(file_path)

# Print the individual posts
for i, post in enumerate(forum_posts):
    print(f"Post {i+1}:")
    print(post)
    print()