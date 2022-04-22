import random

def get_values_within_range():
    values10= [x for x in range(10)]
    print("Values under 10: "+str(values10))

    #get squared values
    squares = [x**2 for x in values10]
    print("squares: "+ str(squares))

    #get odd numbers
    odds = [x for x in range(10) if x%2 == 1]
    print("odds: "+str(odds))

    #get multiples of 5
    fiveries=[ x*5 for x in range(10)]
    print("Multiples of 5: "+str(fiveries))

    #get all numbers from a string
    string="think 2 code 1"
    nums= [x for x in string if x.isnumeric()]
    print("nums: "+ ''.join(nums))

    #get index of an item in list
    colors=['red','green','blue']
    index= [k for k,v in enumerate(colors) if v=="green"]
    print("index: "+ str(index[0]))

def delete_item():
    letters = [ x for x in 'ABCDEF']
    random.shuffle(letters)
    rem_letters=[a for a in letters if a!='F']
    print(letters, rem_letters)

if __name__ == "__main__":
    get_values_within_range()
    delete_item()