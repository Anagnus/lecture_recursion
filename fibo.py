def recursive_ntb_fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return recursive_ntb_fibo(n-1)+recursive_ntb_fibo(n-2)


def main():
    n=int(input("Počet členu fibonacciho posloupnosti:"))
    seq=[recursive_ntb_fibo(num) for num in range(n+1)]
    print(seq)
    pass


if __name__ == "__main__":
    main()
