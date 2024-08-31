from socketify import App
import ujson
import time

app = App()
app.json_serializer(ujson)
router = app.router()

@router.get("/")
def home(res, req):
    print("request made!")
    res.end({"a":"Hello World!"})

@router.get("/hello")
def hello(res, req):

   res.end("Hello API!")

if __name__ == "__main__":
    app.listen(3000, lambda config: print("Listening on port http://localhost:%d now\n" % (config.port)))
    app.run()