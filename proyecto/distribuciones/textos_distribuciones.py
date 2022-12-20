# Crear un texto a partir del tipo de distribución
def texto(distribucion,acumulada):
    
    if distribucion == 'Binomial':

        if not acumulada:
            texto = """
            ##
            ## Distribución Binomial
            
            La distribución binomial se entiende como una serie de pruebas o ensayos
            en la que solo podemos tener 2 resultados (éxito o fracaso), siendo el éxito
            nuestra variable aleatoria.
            
            Forma de calcularlo
            $$
            \\binom{n}{k}*{p}*(1-p)^{n-k}
            $$

            Donde:
            * n - Número de ensayos/experimentos
            * k - Número de éxitos
            * p - Probabilidad de éxito
            
            """
        else:
            texto = """
            ##
            ## Distribución Binomial (ACUMULADA)
            
            Para una variable aleatoria, la función de distribución acumulativa está definida por:
            
            $$
            
            $$
                        
            """

    elif distribucion == 'Exponencial':

        if not acumulada:
            texto = """
            ##
            ## Distribución Exponencial
            
            La distribución exponencial suele referirse a la cantidad de tiempo que transcurre hasta que se produce algún evento específico. Por ejemplo, la cantidad de tiempo (que comienza ahora) hasta que se produzca un terremoto tiene una distribución exponencial.

            Forma de calcularlo
            $$
            \lambda e^{-\lambda x}
            $$

            Donde:
            * \lambda -
            * e - número de euler
            * x -  
            
            """

        else:
            texto = """
            ##
            ## Distribución Exponencial (ACUMULADA)
            
            La distribución exponencial suele referirse a la cantidad de tiempo que transcurre hasta que se produce algún evento específico. Por ejemplo, la cantidad de tiempo (que comienza ahora) hasta que se produzca un terremoto tiene una distribución exponencial.

            Forma de calcularlo
            $$
            \lambda e^{-\lambda x}
            $$

            Donde:
            * \lambda -
            * e - número de euler
            * x -  
            
            """

    elif distribucion == 'Poisson':
        
        if not acumulada:
            texto = """
            ##
            ## Distribución Poisson
            
            La distribución de Poisson es una distribución de probabilidad discreta que expresa, a partir de una frecuencia de ocurrencia media, la probabilidad de que ocurra un determinado número de eventos durante cierto período de tiempo. Concretamente, se especializa en la probabilidad de ocurrencia de sucesos con probabilidades muy pequeñas, o sucesos raros. 

            Forma de calcularlo
            $$
            \\frac{\lambda ^{k} e^{-\lambda}}{k!}
            $$

            Donde:
            * n -
            * k -
            * p -
            
            """

        else:

            texto = """
            ##
            ## Distribución Poisson (ACUMULADA)
            
            La suma de variables aleatorias de Poisson independientes es otra variable
            aleatoria de Poisson cuyo parámetro es la suma de los parámetros de las
            originales. Dicho de otra manera, si

            $$
            X_{i}
            $$
            
            son N variables aleatorias de Poisson independientes, entonces
            
            $$
            \\frac{\lambda ^{k} e^{-\lambda}}{k!}
            $$

            """
            
    elif distribucion == 'Geometrica':
            
        if not acumulada:
            texto = """
            ##
            ## Distribución Geometrica
            
            La distribución geométrica es un modelo adecuado para aquellos procesos en los
            que se repiten pruebas hasta la consecución del éxito a resultado deseado.

            Forma de calcularlo
            $$
            P(X=x) = p*(1-p)^{x-1}
            $$

            Donde:
            * p -
            * x -
            
            """

        else:
            texto = """
            ##
            ## Distribución Geometrica (ACUMULADA)
            
            Forma de calcularlo
            $$
            p*(1-p)^{x-1}
            $$

            Donde:
            * p -
            * x -
            
            """

    else:

        if not acumulada:
            texto = """
            ##
            ## Distribución Normal
            
            Forma de calcularlo
            $$
            \\frac{1}{\sigma \sqrt{2 \pi} } e^{-\\frac{(x-\mu)}{\sigma}}
            $$
            
            Donde:
            * x -
            * \sigma -
            * \mu -
            
            """

        else:
            texto = """
            ##
            ## Distribución Normal (ACUMULADA)
            
            Forma de calcularlo
            $$
            \\frac{1}{\sigma \sqrt{2 \pi} } e^{-\\frac{(x-\mu)}{\sigma}}
            $$
            
            Donde:
            * x -
            * \sigma -
            * \mu -
            
            """
            
    return texto
