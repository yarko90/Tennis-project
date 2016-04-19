__author__ = 'например Андрей'
import os
from webob.exc import HTTPException

from classes_part import ControllerContext, ComponentManager, Component

class WSGIApplicationInstance(Component, ComponentManager):

    def __init__(self):
        super(WSGIApplicationInstance, self).__init__()



class WSGIApplication(object):


    def __init__(self, project_dir):

        self.instance = WSGIApplicationInstance()

    def wsgi_app(self, environ, start_response):
        context = ControllerContext(self.instance, environ)
        context.response = 'Hello Word! '
        return context.response(environ, start_response)

    def __call__(self, environ, start_response):
       return self.wsgi_app(environ, start_response)

