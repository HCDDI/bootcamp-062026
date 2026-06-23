import curses
import random


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(True)
    win.timeout(100)

    snake = [(sh // 2, sw // 2 + 1), (sh // 2, sw // 2), (sh // 2, sw // 2 - 1)]
    direction = curses.KEY_RIGHT
    score = 0

    def place_food():
        while True:
            food = (
                random.randint(1, sh - 2),
                random.randint(1, sw - 2),
            )
            if food not in snake:
                return food

    food = place_food()
    win.addch(food[0], food[1], "*")

    while True:
        win.clear()
        win.border()
        win.addstr(0, 2, f" Score: {score} ")
        win.addstr(0, sw - 18, " Press Q to quit ")

        for y, x in snake:
            win.addch(y, x, "#")
        win.addch(food[0], food[1], "*")

        key = win.getch()
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            if (key == curses.KEY_UP and direction != curses.KEY_DOWN) or (
                key == curses.KEY_DOWN and direction != curses.KEY_UP) or (
                key == curses.KEY_LEFT and direction != curses.KEY_RIGHT) or (
                key == curses.KEY_RIGHT and direction != curses.KEY_LEFT):
                direction = key
        elif key in [ord("q"), ord("Q")]:
            break

        head_y, head_x = snake[0]
        if direction == curses.KEY_UP:
            new_head = (head_y - 1, head_x)
        elif direction == curses.KEY_DOWN:
            new_head = (head_y + 1, head_x)
        elif direction == curses.KEY_LEFT:
            new_head = (head_y, head_x - 1)
        else:
            new_head = (head_y, head_x + 1)

        if (
            new_head[0] in [0, sh - 1]
            or new_head[1] in [0, sw - 1]
            or new_head in snake
        ):
            win.addstr(sh // 2, sw // 2 - 6, " GAME OVER ")
            win.nodelay(False)
            win.getch()
            break

        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            food = place_food()
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], " ")

        win.refresh()

    win.addstr(sh // 2 + 1, sw // 2 - 10, "Press any key to exit")
    win.getch()


if __name__ == "__main__":
    curses.wrapper(main)
