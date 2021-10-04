from enum import Enum


class Symbol(Enum):
    """List of symbols."""
    ROCK: int = 1
    PAPER: int = 2
    SCISSORS: int = 3
    SPOCK: int = 4
    LIZARD: int = 5
    # Add more here...
    MIN: int = ROCK
    MAX: int = LIZARD

    @classmethod
    def graphics(cls, symbol: 'Symbol'):
        """Get the graphics of the symbol."""
        Symbol.Graphics: [str] = ['💎', '📜', '✂', '🖖', '🐊']
        return cls.Graphics[symbol.value - 1]

    @classmethod
    def contains(cls, symbol: 'Symbol'):
        """Check if a symbol value is valid."""
        if symbol is None:
            return False
        return symbol.value in cls._value2member_map_


class Hand:
    """A symbol with the hand."""

    def __init__(self, symbol: Symbol) -> None:
        """Creates a new Hand instance."""
        self.m_symbol: Symbol = symbol
        self.m_loosing: {Symbol, str} = None

    def setLoosingSymbols(self, symbols: {Symbol, str}) -> None:
        """Sets the symbols loosing against the current one."""
        self.m_loosing = symbols

    def winsAgainst(self, other: 'Hand') -> bool:
        """Returns True if the current Hand wins against the other one; False otherwise."""
        return other.m_symbol in self.m_loosing

    @property
    def symbol(self) -> str:
        """Return the symbol of the hand."""
        return Symbol.graphics(self.m_symbol)

    def action(self, other: 'Hand') -> str:
        """Get the action name when the hand wins over an other symbol."""
        return self.m_loosing[other.m_symbol]

    def __eq__(self, other):
        """Check if two Hand objects represent the same."""
        return self.m_symbol == other.m_symbol


class Rock(Hand):
    """Rock hand symbol class."""

    def __init__(self):
        super().__init__(Symbol.ROCK)
        self.setLoosingSymbols({Symbol.SCISSORS: 'crushes', Symbol.LIZARD: 'crushes'})


class Paper(Hand):
    """Paper hand symbol class."""

    def __init__(self):
        super().__init__(Symbol.PAPER)
        self.setLoosingSymbols({Symbol.ROCK: 'covers', Symbol.SPOCK: 'disproves'})


class Scissors(Hand):
    """Scissors hand symbol class."""

    def __init__(self):
        super().__init__(Symbol.SCISSORS)
        self.setLoosingSymbols({Symbol.PAPER: 'cut', Symbol.LIZARD: 'decapitate'})


class Spock(Hand):
    """Spock hand symbol class."""

    def __init__(self):
        super().__init__(Symbol.SPOCK)
        self.setLoosingSymbols({Symbol.ROCK: 'vaporizes', Symbol.SCISSORS: 'smashes'})


class Lizard(Hand):
    """Lizard hand symbol class."""

    def __init__(self):
        super().__init__(Symbol.LIZARD)
        self.setLoosingSymbols({Symbol.SPOCK: 'poisons', Symbol.PAPER: 'eats'})


class AvailableHands:
    """List of the available hands."""

    def __init__(self):
        """Create a new AvailableHands instance."""
        self.m_symbolList: {Symbol, Hand} = {
            Symbol.ROCK: Rock(),
            Symbol.PAPER: Paper(),
            Symbol.SCISSORS: Scissors(),
            Symbol.SPOCK: Spock(),
            Symbol.LIZARD: Lizard()
        }

    def hand(self, symbol: Symbol) -> Hand:
        """Get the hand corresponding to the symbol."""
        return self.m_symbolList[symbol]
