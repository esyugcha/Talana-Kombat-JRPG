class Juego:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def seleccion_jugador_atacante(self):
        total_movimientos_player1 = self.player1.total_movimientos(self.player1.movimientos)
        total_goles_player1 = self.player1.total_golpes(self.player1.golpes)
        total_combinacion_player1 = total_movimientos_player1 + total_goles_player1

        total_movimientos_player2 = self.player2.total_movimientos(self.player2.movimientos)
        total_goles_player2 = self.player2.total_golpes(self.player2.golpes)
        total_combinacion_player2 = total_movimientos_player2 + total_goles_player2

        if total_combinacion_player1 < total_combinacion_player2:
            return self.player1
        elif total_combinacion_player1 > total_combinacion_player2:
            return self.player2

        if total_movimientos_player1 < total_movimientos_player2:
            return self.player1
        elif total_movimientos_player1 > total_movimientos_player2:
            return self.player2

        return self.player1

    def iniciar_combate(self, jugador_atacante, jugador_atacado):
        self.imprimir_mensaje_inicio_combate(jugador_atacante.nombre, jugador_atacado.nombre)
        while jugador_atacante.puntos_energia > 0 and jugador_atacado.puntos_energia > 0:
            gano = jugador_atacante.atacar(jugador_atacado)
            if not gano:
                jugador_atacado.atacar(jugador_atacante)
        self.imprimir_mensaje_fin_combate(jugador_atacante.nombre, jugador_atacado.nombre)

    def combate(self):
        if self.player1 == self.seleccion_jugador_atacante():
            self.iniciar_combate(self.player1, self.player2)
        else:
            self.iniciar_combate(self.player2, self.player1)

    def imprimir_mensaje_inicio_combate(self, jugador_atacante, jugador_atacado):
        print(f"\n{'=' * 10} ¡Comienza el combate entre {jugador_atacante} y {jugador_atacado} {'=' * 10}\n")
    def imprimir_mensaje_fin_combate(self, jugador_atacante, jugador_atacado):
        print(f"\n{'=' * 10} ¡Fin del combate entre {jugador_atacante} y {jugador_atacado} {'=' * 10}\n")
