from node import Node
import math
from parse import parse
def ID3(examples, default):
    attributes = [i for i in examples[0].keys()][:-1]
    ig_values = calculate_entropy(attributes, examples)
    best_attribute = max(ig_values, key=ig_values.get)
    
    node = Node(attribute=best_attribute)
    unique_values = set([i[best_attribute] for i in examples])
    
    for val in unique_values:
        subset = [i for i in examples if i[best_attribute] == val]
        if not subset:
            node.children[val] = Node(leaf=default)  # No examples, make a leaf node with default class
        else:
            node.children[val] = ID3(subset, default)  # Recurse with subset
    
    return node
"""def ID3(examples, default):

  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''
  attributes = [i for i in examples[0].keys()][:-1]
  ig_values = calculate_entropy(attributes,examples)
  print(ig_values)
  #best_ig = max(ig_values)
  #print(best_ig)
  node = [key for key,values in ig_values.items() if values == max(list(ig_values.values()))]
  print(node[0])
  subset_one = [i for i in examples if i[node[0]]=='1']
  subset_zero = [i for i in examples if i[node[0]]=='0']
  for i in subset_one:
    i.pop(node[0])
  attributes_1 = [i for i in subset_one[0].keys()][:-1]
  ig_values_1 = calculate_entropy(attributes_1,subset_one)
  print(ig_values_1)
  node_1 = [key for key,values in ig_values_1.items() if values == max(list(ig_values_1.values()))]
  print(node_1[0])

"""
def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''
  pass

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''
  pass


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
  pass

def calculate_entropy(columns,examples):
  list1 = set()
  total_entropy_1 = 0
  total_entropy_0 = 0
  total_length = 0
  list_IG = {}
  for j in examples:
    for a,b in j.items():
      list1.add(b)
      if a==list(j.items())[-1][0]:
        total_length +=1
        if b=='1':
          total_entropy_1+=1
        if b=='0':
          total_entropy_0+=1
  output_total = -(total_entropy_1/total_length)*math.log2(total_entropy_1/total_length)-(total_entropy_0/total_length)*math.log2(total_entropy_0/total_length)
  print(output_total, total_entropy_0,total_entropy_1,total_length)
  for col in columns:
    discreate_dicts = {key:0 for key in list1}
    discreate_dicts2 = {key:0 for key in list1}
    for j in examples:
      for a,b in j.items():
        i = 0
        if a==col:
          if list(j.items())[-1][1] == '1':
            discreate_dicts[b] +=1
          if list(j.items())[-1][1] == '0':
            discreate_dicts2[b] +=1
    print(discreate_dicts,discreate_dicts2)
    x1,x2 = entropy(discreate_dicts,discreate_dicts2)
    print(x1,x2)
    IG = output_total-((total_entropy_1/total_length)*x1)-(total_entropy_0/total_length)*x2
    print(IG)
    list_IG[col] = IG
  
  return list_IG
def entropy(input_value1,input_value2):
  s_total_1 = list(input_value1.values())[0]+list(input_value2.values())[0]
  input1 = (list(input_value1.values())[0])/s_total_1
  input2 = (list(input_value2.values())[0])/s_total_1
  output_1 = -input1*math.log2(input1)-input2*math.log2(input2)
  s_total_2 = list(input_value1.values())[1]+list(input_value2.values())[1]
  if s_total_2 == 0:
    input1_1 = 0
    input2_1 = 0
  else:
    input1_1 = (list(input_value1.values())[1])/s_total_2
    input2_1 = (list(input_value2.values())[1])/s_total_2
  if input2_1==0:
    output_2 = 0
  else:
    output_2 = -input1_1*math.log2(input1_1)-input2_1*math.log2(input2_1)
  return output_1,output_2
  
if __name__ == "__main__":
  x = parse("/Users/saichakradhar/Downloads/HWM1/tennis.data")
  ID3(x,0)