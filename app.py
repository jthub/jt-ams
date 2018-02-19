#!/usr/bin/env python3
import connexion
import logging
from flask_cors import CORS


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('swagger/jt-ams.yaml', base_path='/api/jt-ams/v0.1')
CORS(app.app)

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=12012, server='gevent')
