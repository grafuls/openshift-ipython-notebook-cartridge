import os
from gevent import socket
from gevent.pywsgi import WSGIServer

import app


sock_path = "{0}run/appserver.sock".format(os.environ["OPENSHIFT_IPYTHON_NOTEBOOK_DIR"])
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.bind(sock_path)
sock.listen(256)

WSGIServer(sock, app.application).serve_forever()
