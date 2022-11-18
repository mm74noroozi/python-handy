from flask import Flask, request
import base64
import logging
import logging_loki

logging_loki.emitter.LokiEmitter.level_tag = "level"
handler = logging_loki.LokiHandler(
   url="https://logs-prod3.grafana.net/loki/api/v1/push",
   auth=('user!?','password!?'),   
   version="1",
)
logger = logging.getLogger("checktrace")
logger.setLevel(logging.INFO)
logger.addHandler(handler)



app = Flask(__name__)

white_list_headers=[]
@app.route("/")
def index():
    return "hello"

    
@app.route("/ping/")
def ping():
    ip = request.headers.get('ar-real-ip')
    if ip : :
        client = base64.b64decode(request.args.get('q')).decode()
        service = client.split("@")[1]
        extra={"tags": {"service": service, "client": client, "ip":ip}}
        logger.info("ping",extra=extra)
        return request.args.get('q')
    return "hello"

if __name__ == "__main__":
    app.run()
