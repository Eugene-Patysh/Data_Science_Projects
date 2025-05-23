"""The guess the number game
The computer makes its own guesses and guesses the number using the halving algorithm
"""

import numpy as np
        

def predict_by_half_dividing(number: int = 1, min_predict_number: int = 0, max_predict_number: int = 100) -> int:
    """Guessing a number using the halving algorithm

    Args:
        number (int, optional): Predicted number. Defaults to 1.
        min_predict_number (int, optional): Min predict number. Defaults to 0.
        max_predict_number (int, optional): Max predict number. Defaults to 100.

    Returns:
        int: Number of attempts
    """
    count = 0
    
    lst = list(range(min_predict_number, max_predict_number+1))        
    
    while True:
        count += 1

        array_lenth = len(lst)
        index = array_lenth//2
        
        if number == lst[index]:
            break
        
        lst = lst[index:] if number > lst[index] else lst[:index]
        
    return count


def score_game(random_predict) -> int:
    """Determination of the average number of attempts of the prediction function over 1000 approaches

    Args:
        random_predict ([type]): predict fuction

    Returns:
        int: average number of attempts
    """
    count_ls = []
    min_value = 0
    max_value = 100
    
    #np.random.seed(1)  # recreate the same random inputs every time
    random_array = np.random.randint(min_value, max_value, size=(1000))  # guesses the number

    for number in random_array:
        count_ls.append(random_predict(number, min_value, max_value))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses a number in an average of {score} attempts.")
    return score


if __name__ == "__main__":
    # RUN
    score_game(predict_by_half_dividing)