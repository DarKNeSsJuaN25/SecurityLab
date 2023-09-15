# SecurityLab

Para garentizar la seguridad, creamos un endpoint de /login para que el usuario obtenga un TOKEN gracias al API_KEY. Una vez realizado esto, el usuario podra acceder al /group01 usando dicho TOKEN.

![image](https://github.com/DarKNeSsJuaN25/SecurityLab/assets/68095284/b285da6c-b916-479a-b7a6-1bb77fc212a1)

Resultado: 

![image](https://github.com/DarKNeSsJuaN25/SecurityLab/assets/68095284/bee086f1-798c-412b-917d-94d0b60433ea)

# SQL Inyection

Para lograr una mejor seguridad, basta con agregar la siguiente linea:

![image](https://github.com/DarKNeSsJuaN25/SecurityLab/assets/68095284/007f24b3-57b7-42e6-b9de-664d236c0cf2)

De esta manera, los valores de user_arg y pass_arg se tratan como parámetros y no como parte de la consulta SQL, lo que protege tu aplicación contra la inyección SQL.
