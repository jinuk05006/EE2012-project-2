import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def plotting_equation():
    while True:
        x = np.linspace(0,40,1000)
        function=input("Please key in pdf or cdf.\n")
        print(f"your input is {function}.\n")
        if function=="pdf":
            y = (1/3)*np.exp(-(x/3))
            z = (1/4)*np.exp(-(x/4))
            a = (1/5)*np.exp(-(x/5))
        if function=="cdf":
            y = 1-np.exp(-(1/3)*x)
            z = 1-np.exp(-(1/4)*x)
            a = 1-np.exp(-(1/5)*x)
        fig = plt.figure(figsize = (10, 5))
        # Plotting both the curves simultaneously
        plt.plot(x, y, color='r', label='lambda=1/3') 
        plt.plot(x, z, color='g', label='lambda=1/4')
        plt.plot(x, a, color="b", label="lambda=1/5")

        plt.xlabel("x value")
        plt.ylabel(f"{function}")
        plt.title(f"{function} Graphs at different lambda values")
        # Adding legend, which helps us recognize the curve according to it's color
        plt.legend()
        plt.show()

        def integrand(t, x):
            return (1/t)*np.exp(-(x/t))

        if function == "pdf":
            pdf_integration(lambda x:integrand(3,x),lambda x: integrand(4,x),lambda x: integrand(5,x))

def pdf_integration(y,z,a):
    start_range = int(input("Please input your minimum value."))
    p_y = integrate.quad(y,start_range,np.inf)[0]
    p_z = integrate.quad(z,start_range,np.inf)[0]
    p_a = integrate.quad(a,start_range,np.inf)[0]
    print(f"P(X>{start_range}|t = 3) = {p_y}, \nP(X>{start_range}]t = 4) = {p_z}, \nP(X>{start_range}|t = 5) = {p_a}")

plotting_equation()
