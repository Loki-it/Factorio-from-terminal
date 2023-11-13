import curses
import time
import curses
import time
import random

risorse = ["ferro","rame","carbone"]

scelta_minerale = random.choice(risorse)
print(scelta_minerale)

def main(stdscr):
    # Inizializza la libreria curses
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.clear()

    # Dimensioni della griglia di gioco
    grid_height = 20
    grid_width = 40

    # Posizione iniziale del giocatore
    player_y = grid_height // 2
    player_x = grid_width // 2

    # Risorse sulla mappa
    resource_map = [['*' if random.random() < 0.2 else '.' for _ in range(grid_width)] for _ in range(grid_height)]

    # Risorse raccolte
    resources = {
        "Ferro": 0,
        "Rame": 0,
        "Carbone": 0
    }

    # Lista degli scavatori
    scavengers = []

    while True:
        # Pulisci lo schermo
        stdscr.clear()

        # Ottieni le dimensioni della finestra
        sh, sw = stdscr.getmaxyx()

        # Disegna il menu delle risorse
        stdscr.addstr(0, 0, "Risorse:")
        row = 1
        for resource, quantity in resources.items():
            stdscr.addstr(row, 2, f"{resource}: {quantity}")
            row += 1

        # Disegna la griglia con risorse
        for i in range(grid_height):
            for j in range(grid_width):
                tile = resource_map[i][j]
                #stdscr.addch(i + 2, j * 2, ord(tile))

        # Disegna il giocatore
        stdscr.addch(player_y + 2, player_x * 2, ord('X'))

        # Disegna gli scavatori
        for scavenger in scavengers:
            y, x, resource_type = scavenger
            stdscr.addch(y + 2, x * 2, ord(resource_type))

        # Aggiorna lo schermo
        stdscr.refresh()

        # Ottieni l'input dell'utente
        user_input = stdscr.getch()

        # Muovi il giocatore
        if user_input == curses.KEY_UP:
            player_y -= 1
        elif user_input == curses.KEY_DOWN:
            player_y += 1
        elif user_input == curses.KEY_LEFT:
            player_x -= 1
        elif user_input == curses.KEY_RIGHT:
            player_x += 1
        elif user_input == ord('q'):
            break
        elif user_input == ord(' '):
            scavengers.append((player_y, player_x, resource_map[player_y][player_x]))
            resource_map[player_y][player_x] = '.'

        # Raccolta risorse
        new_scavengers = []
        for scavenger in scavengers:
            y, x, resource_type = scavenger
            if resource_type != '.':
                resources[resource_type] += 1
            else:
                new_scavengers.append(scavenger)
        scavengers = new_scavengers

        # Aggiorna lo schermo
        stdscr.refresh()

        # Aggiorna ogni secondo
        time.sleep(0.01)

if __name__ == "__main__":
    curses.wrapper(main)
