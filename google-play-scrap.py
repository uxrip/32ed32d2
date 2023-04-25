import csv
from google_play_scraper import Sort, reviews_all

def save_reviews_to_csv(reviews, file_name):
    with open(file_name, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["author_name", "rating", "content"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for review in reviews:
            writer.writerow(review)

if __name__ == "__main__":
    app_id = "com.xtb.xmobile2"  # Replace with your app_id

    all_reviews = reviews_all(
        app_id,
        sleep_milliseconds=0,  # Defaults to 0.
        lang="pl",  # Defaults to 'en'.
        country="pl",  # Defaults to 'us'.
        sort=Sort.NEWEST,  # Defaults to Sort.MOST_RELEVANT.
    )

    reviews_to_save = []
    for review in all_reviews:
        reviews_to_save.append({
            "author_name": review["userName"],
            "rating": review["score"],
            "content": review["content"]
        })

    save_reviews_to_csv(reviews_to_save, "google_play_reviews.csv")

    print("Reviews successfully saved to google_play_reviews.csv")

