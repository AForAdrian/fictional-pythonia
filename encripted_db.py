char2index = {}
index2char= {}

for i, char in enumerate(''+string.ascii_lowercase+string.punctuation):
    char2index[char] = i
    index2char[i] = char

def string2values(str_input, max_len = 8):
    str_input = str_input[:max_len].lower()
    if(len(str_input)<max_len):
        str_input = str_input+'.'*(max_len-len(str_input))
    values = list()
    for char in(str_input):
        values.append(char2index[char])
    return th.tensor(values).long()

string2values('hello')

def one_hot(index, length):
  vect = th.zeros(length).long()
  vect[index] = 1
  return(vect)
one_hot(6,7) 

def string2onehot(str_input, max_len = 8):
    str_input = str_input[:max_len].lower()
    if(len(str_input)<max_len):
        str_input = str_input+'.'*(max_len-len(str_input))
        
    char_vectors = list()
    for char in str_input:
      vect = one_hot(char2index[char], len(index2char)).unsqueeze(0)
      char_vectors.append(vect)
    
    return th.cat(char_vectors, dim=0)
  
matrix = string2onehot('hello')
matrix.shape

def strmatch(str_a,str_b):
  vect = (string2onehot(str_a)*string2onehot(str_b)).sum(1)
  x = vect[0]
  for i in range(vect.shape[0]):
    x = x*vect[i]
  str_match=x
  
  return str_match

result = list
for key in keys:
  print((query_matrix*key).sum(1))



    
