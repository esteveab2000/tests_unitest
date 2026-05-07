videojocs = [
    {
        "titol": "The Legend of Zelda",
        "any_llancament": 2017,
        "genere": "Aventura",
        "plataforma": "Nintendo Switch",
        "puntuacio": 9.7,
        "desenvolupador": {
            "nom": "Nintendo",
            "pais": "Japó"
        },
        "dlcs": ["Master Trials", "Champions' Ballad"],
        "preu": 59.99
    },
    {
        "titol": "Cyberpunk 2077",
        "any_llancament": 2020,
        "genere": "RPG",
        "plataforma": "PC",
        "puntuacio": 7.8,
        "desenvolupador": {
            "nom": "CD Projekt Red",
            "pais": "Polònia"
        },
        "dlcs": ["Phantom Liberty"],
        "preu": 29.99
    },
    {
        "titol": "FIFA 24",
        "any_llancament": 2023,
        "genere": "Esports",
        "plataforma": "PlayStation",
        "puntuacio": 8.2,
        "desenvolupador": {
            "nom": "EA Sports",
            "pais": "Estats Units"
        },
        "dlcs": [],
        "preu": 69.99
    }
]

biblioteca_personal = []

def crear_sequencia(inici, final):
    if isinstance(inici, int) and isinstance(final, int) and inici > 0 and final > 0 and inici < final:
        return list(range(inici, final + 1))
    return []

def numeros_senars_majors(llista, limit):
    if isinstance(limit, int) and llista:
        return [num for num in llista if num % 2 != 0 and num > limit]
    return []

def primera_posicio(llista, element):
    for i, elem in enumerate(llista):
        if elem == element:
            return i
    return -1

def diagonal_principal(matriu):
    if isinstance(matriu, list) and all(isinstance(fila, list) for fila in matriu):
        if len(matriu) == len(matriu[0]): 
            return [matriu[i][i] for i in range(len(matriu))]
    return []



class TestProvaEscrita01:
    """
    Classe que representa la prova escrita 01.

    Example:
        test_01 = TestProvaEscrita01()
        test_01.crear_bateria()
    """

    def __init__(self):
        """
        Inicialitza la classe de la prova escrita 01.
        """
        self.proves = []

    def afegir_prova_2(self):
        """
        Afegeix la segona prova a la bateria.

        Example:
            test_01.afegir_prova_2()
        """
        self.proves.append(self.mostrar_videojoc(videojocs[1])) 
        
    def afegir_prova_3(self):
        """
        Afegeix la tercera prova a la bateria.

        Example:
            test_01.afegir_prova_3()
        """
        self.proves.append(self.afegir_a_biblioteca("FIFA 24", videojocs, biblioteca_personal)) 
    
    def crear_bateria(self):
        """
        Crea una bateria completa de proves per a la prova escrita 01.
        
        Example:
            test_01.crear_bateria()
        """
        self.afegir_prova_2()
        self.afegir_prova_3()

    def mostrar_videojoc(self, joc):
        """
        Mostra les dades d'un videojoc: títol en majúscules, any entre parèntesis, puntuació amb estrelles i preu amb €.
        """
        titol = joc["titol"].upper()
        any_llancament = f"({joc['any_llancament']})"
        puntuacio = "⭐" * int(joc["puntuacio"])
        preu = f"{joc['preu']}€"
        return f"🎮 {titol} {any_llancament} - {puntuacio} - {preu}"

    def afegir_a_biblioteca(self, titol, videojocs, biblioteca):
        """
        Afegir un videojoc a la biblioteca personal.
        """
        joc = next((joc for joc in videojocs if joc['titol'].lower() == titol.lower()), None)
        if joc is None:
            return "❌ Joc no trobat"
        if joc in biblioteca:
            return "⚠️ Ja està a la biblioteca"
        biblioteca.append(joc)
        return "✅ Joc afegit!"

    def mostrar_proves(self):
        """
        Mostra les proves que es van afegir a la bateria de la Prova Escrita 01.
        """
        for prova in self.proves:
            print(prova)

class TestProvaEscrita02:
    """
    Classe que representa la prova escrita 02.

    Example:
        test_02 = TestProvaEscrita02()
        test_02.crear_bateria()
    """

    def __init__(self):
        """
        Inicialitza la classe de la prova escrita 02.
        """
        self.proves = []

    def afegir_prova_1(self):
        """
        Afegeix la primera prova a la bateria (Excloent l'exercici 5).
        """
        self.proves.append(crear_sequencia(5, 10)) 

    def afegir_prova_2(self):
        """
        Afegeix la segona prova a la bateria.
        """
        self.proves.append(numeros_senars_majors([3, -1, 7, 2, -1, 9, 4, 7], 3)) 

    def crear_bateria(self):
        """
        Crea una bateria completa de proves per a la prova escrita 02.
        """
        self.afegir_prova_1()
        self.afegir_prova_2()

    def mostrar_proves(self):
        """
        Mostra les proves que es van afegir a la bateria de la Prova Escrita 02.
        """
        for prova in self.proves:
            print(prova)

if __name__ == "__main__":
    # Creem les instàncies de les dues proves
    test_01 = TestProvaEscrita01()
    test_02 = TestProvaEscrita02()

    # Creem les bateries de proves
    test_01.crear_bateria()
    test_02.crear_bateria()

    print("\nProves creades per la Prova Escrita 01:")
    test_01.mostrar_proves()

    print("\nProves creades per la Prova Escrita 02:")
    test_02.mostrar_proves()
