# -*- coding: utf-8 -*-
# try something like
import json

def index():
    return dict()

def gen_varslist():
    testlist = {}

    import random, os

    import pandas as pd
    #df = pd.read_csv("/home/rh/dsprojects/shroompred/data/raw/mushrooms.csv")
    datafile = open(os.path.join(request.folder, 'static/ml/data/mushrooms.csv'), 'r')
    df = pd.read_csv(datafile)
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
        try:
            bodyvars=json.loads(body.decode('UTF-8'))
        except:
            raise HTTP(400, "400 Bad Request: Unable to parse request")
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

    shroom_atrr = {}

    if request.vars.short=='0':
        try:
            for i in orderlist:
                if bodyvars[i] not in list(attr_list[i].keys()):
                    raise HTTP(400, "400 Bad Request: Mushroom attribute not found")
                else:
                    varlist[0].append(bodyvars[i])
                    shroom_atrr[i] = bodyvars[i]
        except:
            raise HTTP(400)
    elif request.vars.short=='1':
        try:
            for i in orderlist:
                if bodyvars[i] not in list(inv_attr_list[i].keys()):
                    raise HTTP(400, "400 Bad Request: Mushroom attribute not found")
                else:
                    varlist[0].append(attr_list[bodyvars[i]])
                    shroom_atrr[i] = inv_attr_list[i][bodyvars[i]]
        except:
            raise HTTP(400)
    else:
        raise HTTP(400, "400 Bad Request: URL variable unavailable")

    pred = predict(varlist)
    shroom_atrr["prediction"] = pred
    shroom_atrr["source_tracking"] = "backend"

    db.shroom_attr.insert(**shroom_atrr)

    return response.json({'edible': pred})
