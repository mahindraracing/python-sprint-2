def get_feedback():
    feedback = input("Escreva seu feedback: ")
    return feedback


def avaliate_feedback(feedback, feedbacks_dict):
    key_words = {
        "good": {"great", "good", "amazing", "funny", "entertaing", "cool", "liked", "like"},
        "bad": {"awful", "bad", "horrible"} 
    }

    feedback_lower = feedback.lower()

    if any(word in feedback_lower for word in key_words["good"]):
        category = "good-feedbacks"
    elif any(word in feedback_lower for word in key_words["bad"]):
        category = "bad-feedbacks"
    else:
        category = "neutral-feedbacks"

    feedback_count = len(feedbacks_dict[category])
    feedbacks_dict[category][feedback_count] = feedback

    return feedbacks_dict

def display_feedbacks(feedbacks):
    print("\n" + "=" * 40)
    print("     Mahindra Racing Feedback Summary     ")
    print("=" * 40)

    for category in ["good-feedbacks", "bad-feedbacks", "neutral-feedbacks"]:
        print(f"\n{category.replace('-', ' ').title()}:")
        print("-" * 40)
        
        if not feedbacks[category]:
            print("No feedbacks in this category yet.")
        else:
            for index, feedback in feedbacks[category].items():
                print(f"{index + 1}. {feedback}")
        
        print("-" * 40)

    print("\nTotal Feedbacks:")
    print(f"Positive: {len(feedbacks['good-feedbacks'])}")
    print(f"Negative: {len(feedbacks['bad-feedbacks'])}")
    print(f"Neutral: {len(feedbacks['neutral-feedbacks'])}")
    print("=" * 40 + "\n")