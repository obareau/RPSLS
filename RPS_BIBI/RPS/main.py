import random
from symbols import Symbol, Hand, AvailableHands


def welcome() -> None:
    """Prints the welcome message."""
    print("Welcome to the [Rock|Paper|Scissors|Spoke|Lizard] game!")
    print()


def askPlayer() -> None:
    """Prints the user prompt for choosing the hand symbol."""
    print("Which symbol do you take?")
    for data in Symbol:
        print("{}. {}".format(data.value, data.name))


def getPlayerSymbol() -> Symbol:
    """Gets the input from the player when asking the symbol to choose."""
    playerSymbol: Symbol = None

    while not Symbol.contains(playerSymbol):
        askPlayer()

        try:
            playerInputValue: int = int(input())
        except:
            print("I'm expecting a NUMBER!!!")
            continue

        if Symbol.MIN.value <= playerInputValue <= Symbol.MAX.value:
            return Symbol(playerInputValue)
        else:
            print("Enter one of the numbers in the list!")


def tryAgain() -> bool:
    """Asks the player if wanting to play again."""
    print("Try again? (y/n)")
    answer: str = input()

    if answer == 'n' or answer == 'N':
        return False
    elif answer != 'y' and answer != 'Y':
        print("I suppose it means yes!")
        return True
    return True


if __name__ == '__main__':
    AllHands: AvailableHands = AvailableHands()
    welcome()

    continuePlaying: bool = True

    while continuePlaying:
        playerSymbol: Symbol = getPlayerSymbol()
        playerHand: Hand = AllHands.hand(playerSymbol)
        computerSymbol: Symbol = Symbol(random.randint(Symbol.MIN.value, Symbol.MAX.value))
        computerHand: Hand = AllHands.hand(computerSymbol)

        if playerHand == computerHand:
            print("Draw!")
        else:
            if playerHand.winsAgainst(computerHand):
                print("You win!! {} {} {}!".format(
                        playerHand.symbol,
                        playerHand.action(computerHand),
                        computerHand.symbol
                    )
                )
            elif computerHand.winsAgainst(playerHand):
                print("You lose!! {} {} {}...".format(
                        computerHand.symbol,
                        computerHand.action(playerHand),
                        playerHand.symbol
                    )
                )

        continuePlaying = tryAgain()

    print("Have a nice day!")
