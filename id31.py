from node import Node
import math
from parse import parse


def ID3(examples,  default):

    def build_tree(examples, attr, default):
        if len(set(i['Class'] for i in examples)) == 1:
            return Node(next(iter(set(i['Class'] for i in examples))))
        if len([i for i in examples[0].keys() if i != 'Class']) == 0:
            return Node(label=default)
        entropy_total = - (len([list(i.values())[0] for i in examples if i['Class'] == '0'])/len(examples)) * math.log2(len([list(i.values())[0] for i in examples if i['Class'] == '0'])/len(
            examples)) - (len([list(i.values())[0] for i in examples if i['Class'] == '1'])/len(examples)) * math.log2(len([list(i.values())[0] for i in examples if i['Class'] == '1'])/len(examples))
        IG_values = {}

        for j in list(examples[0].keys())[:-1]:
            if len([i for i in examples if i[j] == '0']) > 0 and len([i for i in examples if i[j] == '0' and i['Class'] == '1']) > 0:
                if len([i for i in examples if i[j] == '1']) > 0 and len([i for i in examples if i[j] == '1' and i['Class'] == '1']) > 0:

                    l1 = - (len([i for i in examples if i[j] == '1' and i['Class'] == '1']) / len([i for i in examples if i[j] == '1'])) * \
                        math.log2((len([i for i in examples if i[j] == '1' and i['Class']== '1']) / len([i for i in examples if i[j] == '1'])))
                    l2 = - (len([i for i in examples if i[j] == '1' and i['Class'] == '0']) / len([i for i in examples if i[j] == '1'])) * \
                        math.log2((len([i for i in examples if i[j] == '1' and i['Class']== '0']) / len([i for i in examples if i[j] == '1'])))
                    entropy_one = l1+l2
                    print("entropy ones for ", j, "is ", entropy_one)

                    l1 = - (len([i for i in examples if i[j] == '0' and i['Class'] == '1']) / len([i for i in examples if i[j] == '0'])) * \
                        math.log2((len([i for i in examples if i[j] == '0' and i['Class']== '1']) / len([i for i in examples if i[j] == '0'])))
                    if (len([i for i in examples if i[j] == '0' and i['Class'] == '0']) / len([i for i in examples if i[j] == '0'])) == 0:
                        l2 = 0
                    else:
                        l2 = - (len([i for i in examples if i[j] == '0' and i['Class'] == '0']) / len([i for i in examples if i[j] == '0'])) * math.log2(
                            (len([i for i in examples if i[j] == '0' and i['Class'] == '0']) / len([i for i in examples if i[j] == '0'])))
                    entropy_zero = l1+l2
                    print("entropy zero for ", j, "is ", entropy_zero)

                    IG_value = entropy_total - ((len([i for i in examples if i['Class'] == '0'])/len(examples))*entropy_zero) - (
                        (len([i for i in examples if i['Class'] == '1'])/len(examples))*entropy_one)
                    print("IG of ", j, " is ", IG_value)
                    IG_values[j] = IG_value
        node = Node()
        if IG_values:
            node.label = [key for key, value in IG_values.items(
            ) if value == max(IG_values.values())][0]

        else:
            # Handle the case when IG_values is empty
            node.label = default  # Or set it to a suitable default value

        print(node)
        # filtered_examples = [{k: v for k, v in d.items() if k != node} for d in examples]

        for i in range(2):
            subset1 = [example for example in examples if example.get(
                node.label) == str(i)]
            subset = [{k: v for k, v in d.items() if k != node.label} for d in subset1]
            if not subset:
                subtree = Node(label=default)
            else:
                subtree = build_tree(subset, [i for i in attr if i != node.label], default)
            node.children[i] = subtree
        return node
    attr = [i for i in examples[0].keys() if i != 'Class']
    decision_tree = build_tree(examples, attr, default)
    return decision_tree

def graph(node):
    if node.children:
        print(node.label)
        for value,child in node.children.items():
            print(f"Value:{value}")
            graph(child)
    else:
        print(f"Leaf Node : Class{node.label}")
    

def prune(node, examples):
    '''
    Takes in a trained tree and a validation set of examples.  Prunes nodes in order
    to improve accuracy on the validation data; the precise pruning strategy is up to you.
    '''


def test(node, examples):
    '''
    Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
    of examples the tree classifies correctly).
    '''


def evaluate(node, example):
    '''
    Takes in a tree and one example.  Returns the Class value that the tree
    assigns to the example.
    '''


if __name__ == "__main__":
    examples = parse("tennis.data")
    default = 0
    result = ID3(examples, default)
    graph(result)
    r = evaluate(result, examples)
    print(r)
