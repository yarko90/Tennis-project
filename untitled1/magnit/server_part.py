__author__ = 'например Андрей'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

project_dir = os.path.abspath(__file__)
sys.path.insert(0, project_dir)

from wsgi_part import WSGIApplication
app=WSGIApplication(project_dir)

from paste import httpserver
from paste.httpserver import serve
from paste.evalexception import EvalException
from paste.debug.prints import PrintDebugMiddleware
from paste.reloader import install as install_reloader

app = EvalException(app)
app = PrintDebugMiddleware(app)
install_reloader()

serve(app, host='0.0.0.0', port=8080)