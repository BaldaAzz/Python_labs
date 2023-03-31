import turtle as t

t.shape('turtle')
def draw_star():
    length=150

    t.lt(36)
    t.fd(length)

    for a in range(4):
        t.lt(144)
        t.fd(length)
draw_star()

