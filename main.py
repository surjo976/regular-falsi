# Defining Function
def f(x):
    return 4*x*x*x-6*x*x+7*x-2.3

# Implementing False Position Method
def falsePosition(a,b,e):
    x0 = 1
    print('\n\n******* FALSE POSITION METHOD IMPLEMENTATION *******')
    condition = True
    while condition:
        x2 = ((a*f(b))-(b*f(a)))/(f(b)-f(a))
        print("=============================")
        print('Iteration: %d \nRoot Obtained = %0.6f \nEstimate Error = %0.6f' % (x0, x2, f(x2)))

        if f(a) * f(x2) < 0:
            b = x2
            dx=b-a
        else:
            a = x2
            dx=b-a

        x0 = x0 + 1
        condition = abs(f(x2)) > e and x0<=10 and f(x2)!=0
    print("----------------------------------")
    print("==============Finally=============")
    print('Iteration-%d \nRoot Obtained = %0.6f \nEstimate Error = %0.6f' % (x0-1, x2, f(x2)))

# Input Section
a = float(input('First Guess: '))
b = float(input('Second Guess: '))
e = float(input('Tolerable Error: '))

# Checking Correctness of initial guess values and false positioning
if f(a) * f(b) > 0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    falsePosition(a,b,e)