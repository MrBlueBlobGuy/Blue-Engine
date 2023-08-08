import enum

import moderngl

class BufferRegister:
    def __init__(self):
        self.buffers = []

    def register(self, buffer):
        self.buffers.append(buffer)

    def delete(self):
        for i in self.buffers:
            i.delete()

class Buffer:
    def __init__(self, data, app) -> None:
        self._buffer = 0
        self.ctx = app.ctx
        self.type = type

        app.buffer_register.register(self)

    def bind_data(self):
        # TODO: Add a way to bind data to a buffer
        pass

    def delete(self):
        self._buffer.release()