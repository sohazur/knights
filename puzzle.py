from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is either a Knight or a Knave, not both.
    Or(AKnight, AKnave), Not(And(AKnight, AKnave))
    , 
    # A says "I am both a knight and a knave."
    # If and only if I am a Knight, then I am both a Knight and a Knave.
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Both A and B are either Knight or Knave, not both.
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)), Or(BKnight, BKnave), Not(And(BKnight, BKnave)))
    , 
    # A says "We are both knaves."
    # B says nothing.
    # If and only if A is a Knight, then both A and B are Knaves.
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
# A is Knave, B is Knight
knowledge2 = And(
    # Both A and B are either Knight or Knave, not both.
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)), Or(BKnight, BKnave), Not(And(BKnight, BKnave)))
    , 
    # A says "We are the same kind."
    # B says "We are of different kinds."
    And(Biconditional(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))), Biconditional(BKnight, Or(And(AKnave, BKnight), And(AKnight, BKnave))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        # ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
