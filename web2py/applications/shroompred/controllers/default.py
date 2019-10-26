# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    response.flash = T("Welcome to ShroomPred") if session.visited != 1 else None
    session.visited = 1
    # Form to acquire user input
    if request.args==['1']:
        session.on_defaults = False
        del session.formvars
        session.edible = None

    form = SQLFORM(db.shroom_attr)

    if session.formvars:
        if session.formvars['id']:
            del session.formvars['id']
        form.vars = session.formvars

    form.elements('form')[0]['_class'] = "bg-white rounded pb_form_v1"
    form.elements('input')[-1]['_class'] = "btn btn-primary btn-lg btn-block pb_btn-pill btn-shadow-blue"
    form.elements('input')[-1].parent['_class'] += ' mx-auto'
    form.elements('input')[-1].parent['_style'] = 'padding-top:15px;'
    for i in form.elements('label'):
        i['_class'] += ' text-wrap'
    form.components.insert(0, XML('<h2 class="mb-4 mt-0 text-center">Enter Mushroom Attributes</h2>'))

    # Store result

    if request.args==['3']:
        import random
        for i in orderlist:
            form.vars[i] = random.choice(list(attr_list[i].keys()))

    if request.args==['2']:
        import random, os
        import pandas as pd
        datafile = open(os.path.join(request.folder, 'static/ml/data/mushrooms.csv'), 'r')
        df = pd.read_csv(datafile)
        lim_attr_list={}
        for i in range(len(df.columns[1:])):
            lim_attr_list[orderlist[i]] = [inv_attr_list[orderlist[i]][j] for j in list(df[df.columns[i+1]].unique())]
        for i in orderlist:
            form.vars[i] = random.choice(list(lim_attr_list[i]))

    if form.process().accepted:
        session.formvars = form.vars
        varslist=[['e']]
        for i in orderlist:
            varslist[0].append(attr_list[i][form.vars[i]])
        session.edible = predict(varslist)
        db(db.shroom_attr.id==form.vars.id).update(prediction=session.edible, source_tracking="frontend")
        redirect('index')
        response.flash = T("Success")

    elif form.errors:
        session.formvars = form.vars
        response.flash = T("Errors")
    else:
        session.formvars = form.vars
    
    # Redirect to result



    return dict(message=T('Welcome to Shroompred'), form=form, edible=session.edible)


def faq():
    return dict()

def restdoc():
    return dict()

def history():
    db.shroom_attr.prediction.readable=True
    db.shroom_attr.source_tracking.readable=True
    db.shroom_attr.id.readable=False
    grid=SQLFORM.smartgrid(db.shroom_attr, csv=False)
    return dict(grid=grid)

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
