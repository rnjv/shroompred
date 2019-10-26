# -*- coding: utf-8 -*-
# try something like
import json

def index():
    return dict()

def gen_varslist():
    testlist = {}

    import random, os

    import pandas as pd
    df = pd.read_csv("/home/rh/dsprojects/shroompred/data/raw/mushrooms.csv")
    lim_attr_list = {}

    for i in range(len(df.columns[1:])):
        lim_attr_list[orderlist[i]] = [inv_attr_list[orderlist[i]][j] for j in list(df[df.columns[i + 1]].unique())]
    for i in orderlist:
        testlist[i] = random.choice(list(lim_attr_list[i]))
    varslist = {}

    for i in orderlist:
        varslist[i] = attr_list[i][testlist[i]]
    return varslist

def api():
    response.view = "generic.json"
    varlist=[['e']]
    if not request.env.request_method == 'GET': raise HTTP(403)
    body = request.body.read()
    if body:
        bodyvars=json.loads(body.decode('UTF-8'))
    else:
        raise HTTP(400, "400 Bad Request: Mushroom attributes not found")

    if request.vars.short:
        urlvars=request.vars
    else:
        raise HTTP(400, "400 Bad Request: Required URL parameter(s) not found")

    if set(list(bodyvars.keys()))==set(orderlist):
        stat="ok"
    else:
        raise HTTP(400, "400 Bad Request: Missing mushroom attributes")

    if request.vars.short=='0':
        try:
            for i in orderlist:
                varlist[0].append(bodyvars[i])
        except:
            raise HTTP(400)
    else:
        try:
            for i in orderlist:
                varlist[0].append(attr_list[bodyvars[i]])
        except:
            raise HTTP(400)
    print(varlist)
    pred = predict(varlist)

    return response.json({'edible': pred})
