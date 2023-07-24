class Personaje:
    ENERGIA_INICIAL = 6
    POSICION_INICIAL = 0
    ATAQUE_PUNIO = "P"
    ATAQUE_PATADA = "K"
    PUNTO_GOLPE_ESPECIAL = 1

    PERSONA_TYNON = "Tynon"
    PERSONA_ARNALDOR = "Arnaldor"

    def __init__(self, nombre, movimientos, golpes, combos):
        self.nombre = nombre
        self.movimientos = movimientos
        self.golpes = golpes
        self.puntos_energia = self.ENERGIA_INICIAL
        self.combos = combos
        self.posicion_array = self.POSICION_INICIAL

    def total_movimientos(self, movimientos):
        return self.total_caracteres_array(array=movimientos)

    def total_golpes(self, golpes):
        return self.total_caracteres_array(array=golpes)

    def total_caracteres_array(self, array):
        total_caracteres = 0

        for elemento in array:
            total_caracteres += len(elemento)

        return total_caracteres

    def atacar(self, player_atacado):
        if self.posicion_array < len(self.movimientos):
            combo = self.movimientos[self.posicion_array] + self.golpes[self.posicion_array]
            combo_personaje = self.encontrar_combo_personaje(combo)
            if combo_personaje:
                self.aplicar_ataque(combo_personaje, player_atacado, combo)
                self.posicion_array += 1
                return self.verificar_victoria(player_atacado=player_atacado)
            else:
                return self.realizar_ataque_generador(player_atacado, combo)
        else:
            return False

    def encontrar_combo_personaje(self, combo):
        for combo_personaje in self.combos:
            if combo.endswith(combo_personaje.combinacion):
                return combo_personaje
        return None

    def aplicar_ataque(self, combo_personaje, player_atacado, combo):
        player_atacado.puntos_energia -= combo_personaje.energia_quita
        movimiento = combo_personaje.n_movimiento
        avanza = " avanza y" if len(combo) != len(combo_personaje.combinacion) else ""
        if self.ATAQUE_PUNIO in combo:
            print(f"{self.nombre}{avanza} conecta un {movimiento}")
        else:
            print(f"{self.nombre}{avanza} usa un {movimiento}")

    def realizar_ataque_generador(self, player_atacado, combo):
        nombre_atacado = player_atacado.nombre
        if combo.endswith(self.ATAQUE_PUNIO):
            player_atacado.puntos_energia -= self.PUNTO_GOLPE_ESPECIAL
            if len(combo) != 1:
                print(f"{self.nombre} avanza y da un puñetazo al pobre {nombre_atacado}")
            else:
                print(f"{self.nombre} le da un puñetazo al pobre {nombre_atacado}")
        elif combo.endswith(self.ATAQUE_PATADA):
            player_atacado.puntos_energia -= self.PUNTO_GOLPE_ESPECIAL
            if len(combo) != 1:
                print(f"{self.nombre} avanza y le da una patada a {nombre_atacado}")
            else:
                print(f"{self.nombre} le da una patada")
        else:
            print(self.nombre + " se mueve")

        self.posicion_array += 1
        return self.verificar_victoria(player_atacado=player_atacado)

    def verificar_victoria(self, player_atacado):
        if player_atacado.puntos_energia <= 0:
            self.mensaje_ganador(ganador=self)
            return True
        else:
            return False

    def mensaje_ganador(self, ganador):
        print(ganador.nombre + " gana la pelea y aún le queda " + str(ganador.puntos_energia) + " de energía")