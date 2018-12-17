from decimal import (
    Decimal as Dec,
    getcontext as gc
)


# Parameter defaults chosen to gain 1000+ digits within a few seconds.
def PI(maxK=70, prec=1008, disp=1007):
    gc().prec = prec
    K, M, L, X, S = 6, 1, 13591409, 1, 13591409
    for k in range(1, maxK+1):
        M = (K**3 - 16*K) * M // k**3
        L += 545140134
        X *= -262537412640768000
        S += Dec(M * L) / X
        K += 12
    pi = 426880 * Dec(10005).sqrt() / S
    pi = Dec(str(pi)[:disp])  # drop few digits of precision for accuracy
    print(f'PI(maxK={maxK} iterations, gc().prec={prec}, disp={disp} digits) ='
          f'\n{pi}')
    return pi


# PI()
# PI(317, 4501, 4500)
# PI(353, 5022, 5020)
calcPi = PI(500, 10000, 100000)
print(len(str(calcPi)))
