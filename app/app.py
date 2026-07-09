from flask import Flask, render_template
import socket
import platform
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route("/")
def dashboard():

    hostname = socket.gethostname()

    current_time = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).strftime("%d %b %Y | %I:%M:%S %p IST")

    return render_template(
        "index.html",

        hostname=hostname,

        current_time=current_time,

        os_name=platform.system(),

        os_version=platform.release(),

        python_version=platform.python_version(),

        environment="Development",

        app_status="Running",

        deployment="Successful",

        version="v1.0.0",

        year=datetime.now().year
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )