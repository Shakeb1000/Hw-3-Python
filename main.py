#Author: Shakeb Siddiqui sms8508@psu.edu

def digit_sum(n):
  if n == 0 :
    return 0
  else:
    return n % 10 + digit_sum(n// 10)

def run():
  n=int(input("Enter an int: "))
  mynum=digit_sum(n)
  print(f"sum of digits of {n} is {mynum}.")

if __name__ == "__main__":
  run()