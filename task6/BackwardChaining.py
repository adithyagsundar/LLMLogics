from Production import AND, OR, NOT, IF, THEN, match, populate, simplify

def backchain_to_goal_tree(rules, hypothesis):
    subgoals = [hypothesis]
    
    for rule in rules:
        consequent = rule.consequent()

        if isinstance(consequent, (AND, OR, NOT)):
            for sub_consequent in consequent.conditions():
                subgoals.append(backchain_to_goal_tree(rules, sub_consequent))
        elif isinstance(consequent, str):
            bindings = match(consequent, hypothesis)
            if bindings is not None:
                antecedent = rule.antecedent()
                populated_antecedent = populate(antecedent, bindings)
                subgoals.append(backchain_to_goal_tree(rules, populated_antecedent))
        else:
            print(f"Error: Unexpected consequent type {type(consequent)}")
    
    return simplify(OR(*subgoals))

from data import zookeeper_rules

if __name__ == "__main__":
    hypothesis = 'blank is a mammal'
    goal_tree = backchain_to_goal_tree(zookeeper_rules, hypothesis)
    print("Goal Tree for the Hypothesis '{}':".format(hypothesis))
    print(goal_tree)
