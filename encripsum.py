import random
q =5678765647783792968332898437

def encrypt(x, n_shares=3):
    shares = list()
    for i in range(n_shares-1):
        shares.append(random.randint(0,q))
    
    final_share = q - sum(shares)%q +x
    shares.append(final_share)
    return tuple(shares)

def decrypt(shares):
    return sum(shares)%q

def add(a, b):
    c = list()
    
    assert(len(a)==len(b))
    for i in range(len(a)):
        c.append((a[i]+b[i])%q)
    return tuple(c)
