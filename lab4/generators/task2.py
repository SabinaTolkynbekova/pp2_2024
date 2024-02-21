n = int(input())
generator_expression = (i for i in range(n+1) if i%2==0)
generator_expression_str = ', '.join(map(str, generator_expression))
print(generator_expression_str)
