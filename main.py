def digit_sum(n):
  if n == 0 :
    return 0
  else:
    return n % 10 + digit_sum(n// 10)

def run():
  n=float(input("Enter an int: "))
  print(f"sum of digits of {n} is {digit_sum(n)}.")

run()