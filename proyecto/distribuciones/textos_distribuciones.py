def texto(distribucion='',acumulada=False):
    
    if distribucion == 'Binomial':

        if not acumulada:
            texto = """
            ##
            ## Distribución Binomial
            
            La distribución de probabilidad binomial es una distribución discreta.
            
            Se asocia con un experimento de múltiples pasos que se llama experimento binomial.

            Forma de calcularlo
            $$
            \\binom{n}{k}*{p}*(1-p)^{n-k}
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
            """

    elif distribucion == 'Geometrica':
            
        if not acumulada:
            texto = """
            ##
            ## Distribución Geometrica
            
            Forma de calcularlo
            $$
            p*(1-p)^{x-1}
            $$
            
            
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
            
            """
            
    return texto
