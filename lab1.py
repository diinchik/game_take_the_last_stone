
from functools import lru_cache


# Алгоритм мінімакс
@lru_cache(None)
def minimax(stones, is_maximizing):
    if stones == 0:
        return -1 if is_maximizing else 1

    if is_maximizing:
        best_score = -float("inf")

        for move in range(1, min(3, stones) + 1):
            score = minimax(stones - move, False)
            best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for move in range(1, min(3, stones) + 1):
            score = minimax(stones - move, True)
            best_score = min(best_score, score)

        return best_score


# Вибір найкращого ходу комп'ютера
def computer_move(stones):
    best_score = -float("inf")
    best_move = 1

    for move in range(1, min(3, stones) + 1):
        score = minimax(stones - move, False)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


# Основна функція гри
def play_game():
    stones = 15

    print("=== ГРА: ЗАБЕРИ ОСТАННІЙ КАМІНЬ ===")
    print("На початку є 15 каменів.")
    print("За хід можна забрати 1, 2 або 3 камені.")
    print("Перемагає той, хто забере останній камінь!")

    while stones > 0:
        print(f"\nЗалишилось каменів: {stones}")

        # Хід користувача
        while True:
            try:
                move = int(input("Ваш хід (1-3): "))

                if 1 <= move <= min(3, stones):
                    break
                else:
                    print("Некоректний хід! Спробуйте ще раз.")

            except ValueError:
                print("Введіть ціле число!")

        stones -= move
        print(f"Ви забрали {move} каменів.")

        if stones == 0:
            print("\nВітаємо! Ви перемогли!")
            break

        # Хід комп'ютера
        move = computer_move(stones)
        stones -= move

        print(f"Комп'ютер забрав {move} каменів.")

        if stones == 0:
            print("\nКомп'ютер переміг!")
            break


if __name__ == "__main__":
    play_game()
