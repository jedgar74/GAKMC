# GAKMC

﻿El programa requiere tener instalado python 3 en su versión 5 o superior. Además, deben instalarse las librerías necesarias para ejecutarlo. se recomienda utilizar el  comando pip3 de la siguiente manera

> pip3 install numpy

Para ejecutar el programa se utiliza el código Execute.py. El programa tiene dos formas de configurarse. La primera mediante un archivo json cuyo nombre es scenario,  que se encuentra en la carpeta files/scenario. En este archivo se encuentran los parámetros necesarios para ejecutar el programa ---en la línea 36 de el archivo Execute.py se hace la ejecución mediante este método. La otra posibilidad es modificar directamente en el constructor de la clase Simulation los parámetros necesarios. Para ejecutar este método se evita llamar a los parámetros. Ver línea 35 del archivo Execute.py.

> python3 Execute.py
