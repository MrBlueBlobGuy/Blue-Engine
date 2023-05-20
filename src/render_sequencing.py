import threading

class RenderThread(threading.Thread):
    def __init__(self, render_function, thread_id) -> None:
        threading.Thread.__init__(self)
        self.render_function = render_function
        self.thread_id = thread_id

    def run(self) -> None:
        self.render_function()

