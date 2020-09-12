# MCOC2020-P1  💻 🪐 💫

## TOMÁS MUÑOZ JIMÉNEZ ✅ 

# ENTREGA1 📚 🎳 💨 

  ## GRÁFICO 📈 ⤵️
  
 ![alt text]( https://github.com/tomasmunozj/MCOC2020-P1/blob/master/BALISTICA.png?raw=true)
 
# ENTREGA2 📚 🪐🪐🪐
 
 ![alt text](https://github.com/tomasmunozj/MCOC2020-P1/blob/master/Trayectoria%20satelite.png?raw=true)
 
* ¿Cuanto debe valer Vt de modo que el satélite efectivamente orbite sin caer de vuelta dentro de la atmosfera (asuma que esta comienza a una altura de 80km) ?
  
  * En mi caso, la velocidad Vt se le debe asignar un valor de 5800 m/s para que el satelite orbite sin caer de vuelta dentro de la atmosfera.
  
* ¿Como encontró Vt ?

  * Para encontrar la velocidad Vt que se le asigno al satelite, la manera más sencilla y rápida de encontrar y comprobar, fue gráficando para distintas Vt, de modo que para algún valor de Vt, en el gráfico debiera ocurrir que el satelite pase la atmosfera en direccion a la tierra, por lo que cuando esto pasará, se debía frenar la disminución de la velocidad y por lo tanto quedarse con el valor de Vt limite que no sobrepase la atmosfera.
 
 
 ![alt text](https://github.com/tomasmunozj/MCOC2020-P1/blob/master/Distancia%20en%20funcion%20del%20tiempo%20SATELITE.png?raw=true)
 
 # ENTREGA 5 📚 🪐 💻
 
 ### A continuación, se observan los graficos pedidos, sin la implementación de J2 y J3 :
 
 ![alt text](https://github.com/tomasmunozj/MCOC2020-P1/blob/master/Figure%202020-09-07%20020216.png?raw=true)
 
 ![alt text](https://github.com/tomasmunozj/MCOC2020-P1/blob/master/Figure%202020-09-07%20030105.png?raw=true)
 
 ![alt text](https://github.com/tomasmunozj/MCOC2020-P1/blob/master/Figure%202020-09-07%20025756.png?raw=true)
 
 ### Ahora veamos algunos gráficos, con la implementación de J2 y J3
 
 ![alt text](https://github.com/tomasmunozj/MCOC2020-P1/blob/master/ENTREGA5/Figure%202020-09-11%20123059.png?raw=true)
 
 ### ALGUNOS COMENTARIOS DE LA ENTREGA ✅:
 
   * Si observamos el gráfico de la posicion en (x,y,z) sin la implementacion de J2 y J3, observamos que para todos los ejes, la variación en Kms es de 10000, oscilando entre -5000 y 5000, lo cual en este grafico de posición, es muy similar al que contiene la implementación de J2 y J3, obteniendo mejoras en tiempo, pero no así en distancia, ya que las oscilaciones siguen siendo las mismas. Por otro lado, al implementar las subdivisiones, al aumentar estas, el tiempo de ejecución es demasiado, aumentando exponencialmente con el Nº de subdivisiones.
   
   * Si observamos el otro grafico (derivas) notamos que en mi caso, las diferencias son enormes entre odeint y eulerint, partiendo por el hecho de que las derivas del satelite son diferentes entre ambas, 500 Km v/s 5000 Km, y también en odeint, el aumento de la deriva con el tiempo tiene una "linealidad" mientras que eulerint, mantiene la oscilación vista anteriormente, pero mucho más constante.
   
   * En conclusion, se puede afirmar que la implementacion de J2 y J3, si provoca un cambio, pero no tan significativo, ya que para ver grandes cambios, es necesario la implementación y desarrollo de más terminos matematicos e incluso tomar en cuenta la incidencia de la luna.
 

 
 
