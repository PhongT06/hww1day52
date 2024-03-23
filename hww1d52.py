#1

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

def highlight_keywords(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]

    for review in reviews:
        highlighted_review = review
        for keyword in keywords:
            highlighted_review = highlighted_review.replace(keyword, keyword.upper())
        print(highlighted_review)

highlight_keywords(reviews)

def tally_positive_negative_words(reviews, positive_words, negative_words):
    positive_counts = []
    negative_counts = []

    for review in reviews:

        review_count = review.lower()
        positive_count = sum(review_count.count(word) for word in positive_words)
        negative_count = sum(review_count.count(word) for word in negative_words)
        positive_counts.append(positive_count)
        negative_counts.append(negative_count)

    return positive_counts, negative_counts

positive_words = ["fantastic", "good", "excellent", "great", "awesome", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

positive_counts, negative_counts = tally_positive_negative_words(reviews, positive_words, negative_words)

for i, review in enumerate(reviews):
    print(f"Review {i+1}:")
    print("Positive words:", positive_counts[i])
    print("Negative words:", negative_counts[i])
    print()

def create_summary(review):
    if len(review) <= 30:
        return review

    first_part = review[:30].rfind(' ')
    if first_part == -1:
        return review[:30] + "…"

    return review[:first_part] + "…"

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
summaries = [create_summary(review) for review in reviews]

for i, summary in enumerate(summaries):
    print(f"Summary of Review {i+1}:")
    print(summary)
    print()






































