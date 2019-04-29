carga50 = 100
carga20 = 100
carga10 = 100
 
def sacar_dinero(cantidad):
  global carga50, carga20, carga10
  if cantidad <= 50 * carga50 + 20 * carga20 + 10 * carga10:
 
    de50 = int(cantidad / 50)
    cantidad = cantidad % 50
    if de50 >= carga50: # Si hay suficientes billetes de 50
      cantidad = cantidad + (de50 - carga50) * 50
      de50 = carga50
 
    de20 = int(cantidad / 20)
    cantidad = cantidad % 20
    if de20 >= carga20: # y hay suficientes billetes de 20
      cantidad = cantidad + (de20 - carga20) * 20
      de20 = carga20
 
    de10 = int(cantidad / 10)
    cantidad = cantidad % 10
    if de10 >= carga10: # y hay suficientes billetes de 10
      cantidad = cantidad + (de10 - carga10) * 10
      de10 = carga10
 
    # Si todo ha ido bien, la cantidad que resta por entregar es nula:
    if cantidad == 0:
      # Así que hacemos efectiva la extracción
      carga50 = carga50 - de50
      carga20 = carga20 - de20
      carga10 = carga10 - de10
      return [de50, de20, de10]
    else: # Y si no, devolvemos la lista con tres ceros:
      return [0, 0, 0]
  else:
    return [-1, -1, -1]
 
try:
    c = int(input('Cantidad a extraer: '))
    resultado=sacar_dinero(c)
    if resultado==[0,0,0]:
        print ('No hay desglose de billetes para su importe')
    elif resultado==[-1,-1,-1]:
        print ('No hay suficientes billetes')
    else:
        print ('Billetes de 50:', resultado[0])
        print ('Billetes de 20:', resultado[1])
        print ('Billetes de 10:', resultado[2])
except:
    print ('Importe incorrecto')
