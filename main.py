# Simple code to solve the integral of a function using trapezoidal and simpson's rule
from sympy import sympify, symbols


# calculate the integral using trapezoidal rule
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f.subs(x, a) + f.subs(x, b))
    for i in range(1, n):
        s += f.subs(x, a + i * h)
    return s * h


# calculate the integral using the Simpson's rule
def simpson_rule(f, a, b, n):
    h = (b - a) / n
    s = f.subs(x, a) + f.subs(x, b)
    for i in range(1, n, 2):
        s += 4 * f.subs(x, a + i * h)
    for i in range(2, n - 1, 2):
        s += 2 * f.subs(x, a + i * h)
    return s * h / 3


# ask if the inputs are floats and integers or strings like sin, cos tan, euler, pi
print("RECUERDA ESCRIBIR * PARA MULTIPLICAR, ** para elevar Y NO DEJAR ESPACIOS ENTRE LOS VALORES")
print("para euler escriba E (en mayus), para pi escriba pi")
print("para seno escriba sin(), para coseno escriba cos(), para tangente escriba tan()")
print("para logaritmo natural escriba ln(), para logaritmo base 10 escriba log()")
print("para raiz cuadrada escriba sqrt()")
arriba = input("Ingrese el limite superior: ")
abajo = input("Ingrese el limite inferior: ")
funcion = input("Ingrese la funcion a integrar: ")
cantidad = int(input("Ingrese la cantidad de intervalos: "))


# use sympy parse to convert the string to a sympy expression (the values may include euler, pi, sin, cos, tan, ln,
# log, sqrt)
x = symbols('x')
f = sympify(funcion)
a = sympify(abajo)
b = sympify(arriba)

# Calculate the integral using Simpson's function and trapezoidal rule function
integral_simpson = simpson_rule(f, a, b, cantidad)
integral_trapezoidal = trapezoidal_rule(f, a, b, cantidad)

# Print the results
print("El resultado de la integral con la regla de Simpson es: ", integral_simpson.evalf())
print("El resultado de la integral con la regla del trapecio es: ", integral_trapezoidal.evalf())

# Error calculation

# Trapezoidal rule error = E<=k*(b-a)^3/(12*n^2)
# Simpson's rule error = E<=k*(b-a)^5/(180*n^4)

# K is the maximum value of the second derivative for trapezoidal and fourth for Simpson's of the function
# on the interval [a, b]

k_simpson = f.diff(x,4)
k_trapezoidal = f.diff(x,2)
error_trapezoidal = (k_trapezoidal*(b - a) ** 3) / (12 * cantidad ** 2)
error_simpson = (k_simpson*(b - a) ** 5) / (180 * cantidad ** 4)

# Print the errors
print("El error de la regla del trapecio es: ", error_trapezoidal.evalf())
print("El error de la regla de Simpson es: ", error_simpson.evalf())
