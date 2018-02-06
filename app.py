#!/usr/bin/env python3
import connexion
import logging

logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('swagger/jt-ams.yaml', base_path='/api/jt-ams/v0.1')

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=12012, server='gevent')
