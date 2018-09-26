Para iniciar se llama a la clase Temperaturas que recibe dos elementos, 
el primero un numero del 0 al 24 que se refiere a la hora del dia que se quiere modelar 
y el segundo termino debe ser un 1 o un 0, un 0 si el valor de rho con el que se quiere 
trabajar es 0 y el 1 si el valor de rho es el que se muestra en la guia.
Luego se tiene que llamar a la funcion de la clase _geografia() que recibe nada
pero crea toda la geografia del problema con las temperaturas iniciales dependiendo de
la hora puesta anteriormente, luego se tiene que llamar a la funcion start() que permite comenzar
a iterar sobre la matriz hasta que los valores de esta convergen, y por ultimo se llama a la funcion grafico()
que su funcion es mostrar en pantalla la matriz resultante luego de iterar.
Por defecto el valor de omega es el optimo, (funcion _omega()), si se desea cambiar el valor de omega 
se tiene que hacer a mano cambiandolo en la funcion start().
