"""
Datos de entrada
Precio por compra de contado = p = int
Recargo (Interes) de la compra a cuotas = r = float


Datos de salida
Porcentaje de cobro por el recargo (interes) del computador por cuota = ic = int

"""
# Entradas
p=int(input("Inserte el precio de la compra de contado "))
r=float(input(" Inserte el Recargo (Interes) de la compra a cobrar por cada cuota "))



# Caja Negra 
cn=(p/12) # Cuota normal sin recargos
rc=(((p/12)*(r/100))+cn)# Representa la cuota en conjunto al recargo (interes generado) para cada cuota
ic=(((rc-cn)*100)/cn) # Representa el impacto que tiene el recargo o los intereses en el incremento de la cuota


# Salidas
print(" Porcentaje de cobro por el recargo (interes) del computador por cuota ", ic ," % ")
print(" La cuota a pagar en conjunto al recargo o interes mensual sera de ", rc)
