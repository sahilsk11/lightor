#!/usr/bin/python

import bottle

@bottle.route('/')
def index():
    tmplt = bottle.template("template.html")
    return tmplt

bottle.run(host="", port="8080")