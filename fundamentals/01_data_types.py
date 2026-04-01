
def DataTypes (a,b,c,d):
    print(f" {a} {type(a)}")
    print(f" {b} {type(b)}")
    print(f" {c} {type(c)}")
    print(f" {d} {type(d)}")
DataTypes(42,3.14, "Hello Aris", True)


def arithmetic (x,y):
    print(f"addition : {x+y}")
    print(f"subtraction : {x-y}")
    print(f"multiplication : {x*y}")
    print(f"Division : {x/y}")
    print(f"modulus : {x%y}")
    print(f"exponential : {x**y}")

arithmetic(17,5)

def StringSlicing(s):

    print(f"{s[5:]}")

StringSlicing ("Data Engineering")

def String_reversing(s):

    print(f"{s[::-1]}")

StringSlicing ("Data Engineering")

def String_vowels(s):
    x=0;
    for i in s:
        if i in "aeiou":
            x = x+1
    print (f"the number of vowels in {s} is {x}")

String_vowels("Data Engineering")

def display(name, role, salary):
    print(f"Hi, my name is {name}. I am training to be a {role} with a target salary of €{salary:,.2f}")
display("Aris", "Data engineer", 75000.678)



#Conversion across data types
def conversion():
    a = "2026"
    b = 42
    c = "hello"

    d = int(a)
    e = float(b)
    
    try:
        f = int(c)
    except ValueError:
        print(f"Cannot convert {c} to int")


    print(f" to string {d}: {type(d)} \n to float {e}: {type(e)} \n")

conversion()
