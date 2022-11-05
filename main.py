import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad



def plotting_equation():
  while True:
    x = np.linspace(0,40,1000)
    x_fill=np.linspace(5,40, 1000)
    function=input("Please key in pdf or cdf.\n")
    print(f"your input is {function}.\n")
    def the_pdf_eq(t, x):
        return (1/t)*np.exp(-(x/t))
    def the_cdf_eq(t, x):
        return 1-np.exp(-(1/t)*x)
    if function=="pdf":
        y = the_pdf_eq(3,x)
        z = the_pdf_eq(4,x)
        a = the_pdf_eq(5,x)
       
    if function=="cdf":
        y = the_cdf_eq(3, x)
        z = the_cdf_eq(4, x)
        a = the_cdf_eq(5, x)
    print(integrad_eq(lambda x:the_pdf_eq(3,x), 5, np.inf))
    fig = plt.figure(figsize = (10, 5))
    # Plotting both the curves simultaneously
    plt.plot(x, y, color='r', label='lambda=1/3')
    plt.plot(x, z, color='g', label='lambda=1/4')
    plt.plot(x, a, color="b", label="lambda=1/5")
    
    plt.fill_between(x_fill,the_pdf_eq(3, x_fill), alpha=0.5)

    plt.xlabel("x value")
    plt.ylabel(f"{function}")
    plt.title(f"{function} Graphs at different lambda values")
    
    # Adding legend, which helps us recognize the curve according to it's color
    plt.legend()
    plt.show()
    

def integrad_eq(eq, start, end):
    return quad(eq, start, end )[0]


print(plotting_equation())

