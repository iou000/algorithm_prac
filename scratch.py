from itertools import product

data = ['A', 'B', 'C']
result = list(product(data,repeat=1)) # 2개를 뽑는 모든 조합 구하기 nCr => n! / (n-r)!r! == nPr / r!
print(result) #[('A', 'B'), ('A', 'C'), ('B', 'C')]