from Production import IF, AND, THEN, forward_chain
from data import poker_data


def transitive_rule():
    return IF(
        AND('(?x) beats (?y)', '(?y) beats (?z)'),
        THEN('(?x) beats (?z)')
    )

# Apply the transitive rule
if __name__ == "__main__":
    inferred_poker_data = forward_chain([transitive_rule()], poker_data, apply_only_one=False)
    print("Inferred Poker Hands Relationships:")
    for relation in inferred_poker_data:
        print(relation)
