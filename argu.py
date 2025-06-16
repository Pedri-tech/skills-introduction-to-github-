def netp(lp, disc=0,tax=0.05):
    return lp * (1 - disc) * (1 + tax)
print(netp(500))