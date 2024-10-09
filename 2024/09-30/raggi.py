#!/usr/bin/env python3

import g2d

rs = dict()
for i in range(3):
    rs[i] = int(input(f"Inserisci il raggio del cerchio numero {i+1}: "))

if not (rs[0] > rs[1] and rs[1] >  rs[2]):
    print("Errore! i raggi devono essere in ordine di grandezza!")
else:
    g2d.init_canvas((500, 500))
    colors = [(255, 0, 255), (255, 255, 0), (0, 255, 255)]
    
    for i, r in enumerate(rs.values()):
        g2d.set_color(colors[i])
        g2d.draw_circle((250,250), r)

    g2d.main_loop()