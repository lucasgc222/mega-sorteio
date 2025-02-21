import random

TOTAL_NUMBERS = 6
MIN_RANGE = 1
MAX_RANGE = 60
MIN_BET_NUMBERS = 6
MAX_BET_NUMBERS = 20


def get_winning_numbers():
    winning_numbers = random.sample(range(MIN_RANGE, MAX_RANGE + 1), TOTAL_NUMBERS)
    return sorted(winning_numbers)


def get_bet_numbers():
    qty = 0
    while not (MIN_BET_NUMBERS <= qty <= MAX_BET_NUMBERS):
        try:
            qty = int(input("Quantidade de números da aposta (entre 6 e 20): "))
            if not (MIN_BET_NUMBERS <= qty <= MAX_BET_NUMBERS):
                print("Por favor, digite um número entre 6 e 20.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    return qty


def make_bet():
    bet = []
    i = 1
    qty_numbers = get_bet_numbers()
    while len(bet) < qty_numbers:
        try:
            number = int(
                input(
                    f"{i}º número - Digite um número entre {MIN_RANGE} e {MAX_RANGE}: "
                )
            )
            if number < MIN_RANGE or number > MAX_RANGE:
                print(
                    f"Número fora do intervalo ({MIN_RANGE}-{MAX_RANGE})! Tente novamente!"
                )
            elif number in bet:
                print("Número já registrado! Tente novamente!")
            else:
                bet.append(number)
                i += 1
        except ValueError:
            print(
                "Entrada inválida. Por favor, digite um número inteiro e dentro do intervalo permitido."
            )
    return sorted(bet)


def check_matches(bet, winning_numbers):
    matches = len(set(bet) & set(winning_numbers))
    won = matches == len(winning_numbers)
    return won, matches


def main():
    winning_numbers = get_winning_numbers()
    bet = make_bet()

    won, matches = check_matches(bet, winning_numbers)

    if won:
        print("Você ganhou na Mega!")
    else:
        print(f"\nVocê perdeu e acertou {matches} número(s).")

    print("\nNúmeros Sorteados: ", winning_numbers)
    print("Sua aposta:        ", bet)


if __name__ == "__main__":
    main()
