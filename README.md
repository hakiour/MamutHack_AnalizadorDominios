# MamutHack_AnalizadorDominios
Terrassa Haash es un proyecto nacido en la MamutHack 2019 para realizar el reto de Everis de detección automática de acoso cibernético y discruso de odio.

La idea es que,sin utilizar ninguna API, conseguir obtener enlaces relacionados con una página web, y después acceder a estás para realizar un recuento de las palabras que más aparecen y así poder relacionarlas con discursos que promueven el odio hacía alguna minoria.

Estás palabras se contrastan con un diccionario para detectar si el dominio (y los principales links asociados a este (los cuales se obtienen a través de un buscador)) son evaluados y asociados a una ranking para especificar la probabilidad de que esa página promueva discursos de odios hacía minorias.

También se muestran unas estadisticas que analizan los analisis, y en tiempo reael se actualiza la página web con las últimas consultas y palabras buscadas por cualquier usuario.

Las difultades que hemos encontrado ha sido sobretodo el no utilizar una API para gestionar las consultas, hemos tenido muchos problemas con las páginas ya que nos detectaban como bots al realizar scraping (y algunas aún lo hacen), páginas como https://www.lavanguardia.com/ es recomendada para realizar las pruebas del programa.
