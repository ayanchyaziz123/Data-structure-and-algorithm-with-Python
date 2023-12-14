def nstep(n: int)-> None:
    if n == 0: return 1
    if n < 0: return 0
    return nstep(n-1) + nstep(n-2)
print(nstep(4))