
#def add(a, b):
    pass  # ...


#def output(a, b, sum):
    pass  # ...


#def main():
    #a, b = input_two_numbers()
    #sum = add(a, b)

    #output(a, b, sum)


#if __name__ == '__main__':
    #main()


def add(id, ie):
    ig=id+ie
    return ig
   


def output(ig):
   print("The sum is:",ig)
    
   

while True:

    a=input("Enter the number:")
    b=input("Enter the number:")
    ia=int(a)
    ib=int(b)
    ic=add(ia,ib)
    if ic=='done':break
    output(ic)
    