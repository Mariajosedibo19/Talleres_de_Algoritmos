"""
Datos de entrada

Cantidad inicial invertida en el banco = dinero_inicial = int
Porcentaje de interes generado al cual paga su banco = int_banco = float


Datos de salida
Dinero final que tendra en su cuenta = dinero_final = int
Cuanto dinero se generara por el concepto de intereses = intereses = int

"""
# Entradas

dinero_inicial= int(input(" Digite la Cantidad que va a invertir en el banco "))
int_banco= float(input("Porcentaje de interes generado al cual paga su banco "))

# Caja Negra 

intereses = (dinero_inicial*int_banco/100) 
if (intereses > 100_000):
    
# Datos de Salida  
    print(f"El valor que tendra al final en su cuenta y que volvera a reinvertir es de {intereses+dinero_inicial}",(f"y el dinero que le fue generado por los intereses es de {intereses}"))
else:
    print(f"El valor que tendra al final de su cuenta sera de {intereses+dinero_inicial} y el valor a reinvertir sera de {dinero_inicial}")







