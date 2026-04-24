import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--p", type=int, help="p for rsa")
parser.add_argument("--q", type=int, help="q for rsa")
parser.add_argument("--e", type=int, help="exponent e")
parser.add_argument("--n", type=int, help="mod n")
parser.add_argument("--phin", type=int, help="totient n")
parser.add_argument("--m", type=int, help="message x")
args = parser.parse_args()

def rsa_process(p=args.p, q=args.q, e=args.e, n=args.n, phin=args.phin, m=args.m):
    if n is None and p is not None and q is not None:
        n = p * q
    
    if phin is None and p is not None and q is not None:
        phin = (p - 1) * (q - 1)
    
    exponent_e = e if e is not None else 65537
    
    d = None
    if phin is not None:
        try:
            d = pow(exponent_e, -1, phin)
        except ValueError:
            d = None
            
    if m is None or n is None or n <= 1:
        return "impossible to compute given parameters"

    result = pow(m, exponent_e, n)
    print("p:", p,
        "q:", q,
        "e:", exponent_e,
        "d:", d,
        "n:", n,
        "phin:", phin,
        "m:", m,
        "result:", result)
    return 

rsa_process()