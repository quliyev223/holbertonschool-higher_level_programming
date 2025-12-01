import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print status + titles."""
    response = requests.get(API_URL)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # If successful, process JSON
    if response.status_code == 200:
        posts = response.json()

        # Print titles of all posts
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetch posts and save them to posts.csv with id, title, and body."""
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()

        # Prepare simplified data structure
        simplified_posts = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        # Save to CSV
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(simplified_posts)
