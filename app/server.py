import falcon

class Ping:
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        resp.media = {"ping": "ok"}

app = falcon.App()
app.add_route("/ping", Ping())