import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad



def plotting_equation():
  while True:
    x = np.linspace(0,40,1000)
    x_fill=np.linspace(5,40, 1000)
    
    function=input("Please key in pdf or cdf.(type exit to quit)\n")
    if function=='exit':
        break
    print(f"your input is {function}.\n")
    def the_pdf_eq(t, x):
        return (1/t)*np.exp(-(x/t))
    def the_cdf_eq(t, x):
        return 1-np.exp(-(1/t)*x)
    def integrad_eq(eq, start, end):
        return quad(eq, start, end )[0]
    y_p=integrad_eq(lambda x:the_pdf_eq(3,x), 5, np.inf)
    z_p=integrad_eq(lambda x:the_pdf_eq(4,x), 5, np.inf)
    a_p=integrad_eq(lambda x:the_pdf_eq(5,x), 5, np.inf)

    print(f"The p when lambda is 1/3 is {y_p}.\n")
    print(f"The p when lambda is 1/4 is {z_p}.\n")
    print(f"The p when lambda is 1/5 is {a_p}.\n")

    if function=="pdf":
        y = the_pdf_eq(3,x)
        z = the_pdf_eq(4,x)
        a = the_pdf_eq(5,x)
        #fig = plt.figure(figsize = (10, 5))
        plt.plot(x, y, color='r', label=f"t=3 ; lambda=1/3 , p={y_p}")
        plt.plot(x, z, color='g', label=f"t=4 ; lambda=1/4 , p={z_p}")
        plt.plot(x, a, color="b", label=f"t=5 ; lambda=1/5 , p={a_p}")
        plt.fill_between(x_fill,the_pdf_eq(3, x_fill),color="r", alpha=0.5)
        plt.fill_between(x_fill,the_pdf_eq(4, x_fill),color="g", alpha=0.5)
        plt.fill_between(x_fill,the_pdf_eq(5, x_fill),color="b", alpha=0.5)
        plt.xlabel("x value")
        plt.ylabel(f"{function}")
        plt.title(f"{function} Graphs at different lambda values")

    if function=="cdf":
        y = the_cdf_eq(3, x)
        z = the_cdf_eq(4, x)
        a = the_cdf_eq(5, x)
        plt.plot(x, y, color='r', label=f"t=3 ; lambda=1/3 , p={y_p}")
        plt.plot(x, z, color='g', label=f"t=4 ; lambda=1/4 , p={z_p}")
        plt.plot(x, a, color="b", label=f"t=5 ; lambda=1/5 , p={a_p}")
        
        plt.xlabel("x value")
        plt.ylabel(f"{function}")
        plt.title(f"{function} Graphs at different lambda values")
        
    plt.legend()
    plt.show()

  return   
    
    
print(plotting_equation())
