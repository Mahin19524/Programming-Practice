import time
import random
import string

# def generate_passage():
#     words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'watermelon', 'kiwi', 'strawberry', 'blueberry', 'raspberry']
#     passage = ' '.join(random.choices(words, k=30))  # Generate a passage with 30 random words
#     return passage

def calculate_accuracy(correct_words, typed_words):
    if not correct_words:
        return 0
    correct_count = sum(1 for cw, tw in zip(correct_words, typed_words) if cw == tw)
    accuracy = (correct_count / len(correct_words)) * 100
    return accuracy

def calculate_wpm(text, elapsed_time):
    words = text.split()
    word_count = len(words)
    minutes = elapsed_time / 60
    wpm = word_count / minutes if minutes > 0 else 0
    return wpm

def main():
    print("Welcome to the Words Per Minute (WPM) checker!")
    print("Type the following passage as fast and accurately as you can:")
    passage = "Hey my name is Mahin Ahmed and i am a programmer and i am the best programmer in the world"
    print(passage)
    input("Press Enter when you are ready to start typing.")

    start_time = time.time()
    user_input = input("Start typing: ").strip()
    end_time = time.time()

    elapsed_time = end_time - start_time
    wpm = calculate_wpm(user_input, elapsed_time)

    correct_words = passage.split()
    typed_words = user_input.split()

    accuracy = calculate_accuracy(correct_words, typed_words)

    print("\nResults:")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Words per minute (WPM): {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
