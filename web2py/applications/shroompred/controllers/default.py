# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    response.flash = T("Welcome to ShroomPred")
    # Form to acquire user input
    session.on_defaults = False

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

    if form.process().accepted:
        session.formvars = form.vars
        response.flash = T("Success")
    elif form.errors:
        session.formvars = form.vars
        response.flash = T("Erorrs")
    else:
        session.formvars = form.vars
        response.flash = T("Unknown")
    
    # Redirect to result
    
    return dict(message=T('Welcome to Shroompred'), form=form)

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
