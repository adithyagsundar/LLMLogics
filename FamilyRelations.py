from Production import IF, AND, NOT, THEN, forward_chain
from data import simpsons_data
def sibling_rule():
    return IF(
        AND('parent (?p) (?x)', 'parent (?p) (?y)', NOT('self (?x) (?y)')),
        THEN('sibling (?x) (?y)')
    )

def child_rule():
    return IF(
        'parent (?p) (?c)',
        THEN('child (?c) (?p)')
    )

def grandparent_rule():
    return IF(
        AND('parent (?p) (?c)', 'parent (?g) (?p)'),
        THEN('grandparent (?g) (?c)')
    )

def cousin_rule():
    return IF(
        AND('parent (?p1) (?x)', 'parent (?p2) (?y)', 'sibling (?p1) (?p2)', NOT('sibling (?x) (?y)')),
        THEN('cousin (?x) (?y)')
    )

def family_rules():
    rules = [
        sibling_rule(),
        child_rule(),
        grandparent_rule(),
        cousin_rule(),
        # Add more rules here as needed
    ]
    return rules


if __name__ == "__main__":
    inferred_family_relations = forward_chain(family_rules(), simpsons_data, apply_only_one=False)
    print("Inferred Family Relations:")
    for relation in inferred_family_relations:
        print(relation)
