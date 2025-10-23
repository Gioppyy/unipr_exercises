class Ghost(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._visible = True

    def move(self, arena: Arena):
        aw, ah = arena.size()
        dx = choice([-4, 0, 4])
        dy = choice([-4, 0, 4])
        self._x = (self._x + dx) % aw
        self._y = (self._y + dy) % ah

        if randrange(100) == 0:
            self._visible = not self._visible
        if randrange(1000) == 0:
            arena.spawn(Ball(self.pos()))

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h

    def sprite(self) -> Point:
        if self._visible:
            return 20, 0
        return 20, 20
