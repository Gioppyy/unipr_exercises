#https://online.oldgames.sk/play/arcade/ghosts-n-goblins/10197

from actor import Actor, Arena, Point

def tick():
    global x_view, y_view
    g2d.clear_canvas()
    g2d.draw_image("background.png", (0, 0), (w_view, h_view), (x_view, y_view))

    keys = arena.current_keys()
    if "ArrowUp" in keys:
        y_view -= 5
    elif "ArrowDown" in keys:
        y_view += 5
    if "ArrowLeft" in keys:
        x_view -= 5
    elif "ArrowRight" in keys:
        x_view += 5

    arena.tick(g2d.current_keys())

x_view, y_view = 200, 150
w_view, h_view = 300, 200

def main():
    global g2d, arena
    import g2d
    arena = Arena((w_view, h_view))

    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
