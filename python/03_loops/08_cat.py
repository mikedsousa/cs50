# i = 0
# while i < 3:
#   print("meow")
#   i += 1

def main():
  number = get_number()
  meow(number)
  
def get_number():
  while True:
    n = int(input("What's x? "))
    if n > 0:
      break
  return n
  
def meow(n):
  for _ in range(n):
    print("meow")
  
main()