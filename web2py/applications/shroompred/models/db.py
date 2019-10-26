# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(configuration.get('db.uri'),
             pool_size=configuration.get('db.pool_size'),
             migrate_enabled=configuration.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = [] 
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=configuration.get('host.names'))

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
auth.settings.extra_fields['auth_user'] = []
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else configuration.get('smtp.server')
mail.settings.sender = configuration.get('smtp.sender')
mail.settings.login = configuration.get('smtp.login')
mail.settings.tls = configuration.get('smtp.tls') or False
mail.settings.ssl = configuration.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------  
# read more at http://dev.w3.org/html5/markup/meta.name.html               
# -------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')
response.show_toolbar = configuration.get('app.toolbar')

# -------------------------------------------------------------------------
# your http://google.com/analytics id                                      
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get('google.analytics_id')

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configuration.get('scheduler.heartbeat'))

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)

attr_list = {"cap_shape":{"bell":"b","conical":"c","convex":"x","flat":"f"," knobbed":"k","sunken":"s"},
"cap_surface":{"fibrous":"f","grooves":"g","scaly":"y","smooth":"s"},
"cap_color":{"brown":"n","buff":"b","cinnamon":"c","gray":"g","green":"r","pink":"p","purple":"u","red":"e","white":"w","yellow":"y"},
"bruises":{"bruises":"t","no":"f"},
"odor":{"almond":"a","anise":"l","creosote":"c","fishy":"y","foul":"f","musty":"m","none":"n","pungent":"p","spicy":"s"},
"gill_attachment":{"attached":"a","descending":"d","free":"f","notched":"n"},
"gill_spacing":{"close":"c","crowded":"w","distant":"d"},
"gill_size":{"broad":"b","narrow":"n"},
"gill_color":{"black":"k","brown":"n","buff":"b","chocolate":"h","gray":"g"," green":"r","orange":"o","pink":"p","purple":"u","red":"e","white":"w","yellow":"y"},
"stalk_shape":{"enlarging":"e","tapering":"t"},
"stalk_root":{"bulbous":"b","club":"c","cup":"u","equal":"e","rhizomorphs":"z","rooted":"r","missing":"?"},
"stalk_surface_above_ring":{"fibrous":"f","scaly":"y","silky":"k","smooth":"s"},
"stalk_surface_below_ring":{"fibrous":"f","scaly":"y","silky":"k","smooth":"s"},
"stalk_color_above_ring":{"brown":"n","buff":"b","cinnamon":"c","gray":"g","orange":"o","pink":"p","red":"e","white":"w","yellow":"y"},
"stalk_color_below_ring":{"brown":"n","buff":"b","cinnamon":"c","gray":"g","orange":"o","pink":"p","red":"e","white":"w","yellow":"y"},
"veil_type":{"partial":"p","universal":"u"},
"veil_color":{"brown":"n","orange":"o","white":"w","yellow":"y"},
"ring_number":{"none":"n","one":"o","two":"t"},
"ring_type":{"cobwebby":"c","evanescent":"e","flaring":"f","large":"l","none":"n","pendant":"p","sheathing":"s","zone":"z"},
"spore_print_color":{"black":"k","brown":"n","buff":"b","chocolate":"h","green":"r","orange":"o","purple":"u","white":"w","yellow":"y"},
"population":{"abundant":"a","clustered":"c","numerous":"n","scattered":"s","several":"v","solitary":"y"},
"habitat":{"grasses":"g","leaves":"l","meadows":"m","paths":"p","urban":"u","waste":"w","woods":"d"}}

inv_attr_list={}
for i in list(attr_list.keys()):
    inv_attr_list[i] = {v: k for k, v in attr_list[i].items()}

    # Create vars in order
    orderlist = ["cap_shape",
               "cap_surface",
               "cap_color",
               "bruises",
               "odor",
               "gill_attachment",
               "gill_spacing",
               "gill_size",
               "gill_color",
               "stalk_shape",
               "stalk_root",
               "stalk_surface_above_ring",
               "stalk_surface_below_ring",
               "stalk_color_above_ring",
               "stalk_color_below_ring",
               "veil_type",
               "veil_color",
               "ring_number",
               "ring_type",
               "spore_print_color",
               "population",
               "habitat"]


defaults = [
  'x',
  'y',
  'n',
  'f',
  'n',
  'f',
  'c',
  'b',
  'b',
  't',
  'b',
  's',
  's',
  'w',
  'w',
  'p',
  'w',
  'o',
  'p',
  'w',
  'v',
  'd']

if request.vars.on_defaults=="t":
    on_defaults = True
else:
    on_defaults = False

db.define_table("shroom_attr",
                Field("cap_shape", requires=IS_IN_SET(list(attr_list["cap_shape"].keys())), default=inv_attr_list["cap_shape"][defaults[0]] if on_defaults else None),
                Field("cap_surface", requires=IS_IN_SET(list(attr_list["cap_surface"].keys())), default=inv_attr_list["cap_surface"][defaults[1]] if on_defaults else None),
                Field("cap_color", requires=IS_IN_SET(list(attr_list["cap_color"].keys())), default=inv_attr_list["cap_color"][defaults[2]] if on_defaults else None),
                Field("bruises", requires=IS_IN_SET(list(attr_list["bruises"].keys())), default=inv_attr_list["bruises"][defaults[3]] if on_defaults else None),
                Field("odor", requires=IS_IN_SET(list(attr_list["odor"].keys())), default=inv_attr_list["odor"][defaults[4]] if on_defaults else None),
                Field("gill_attachment", requires=IS_IN_SET(list(attr_list["gill_attachment"].keys())), default=inv_attr_list["gill_attachment"][defaults[5]] if on_defaults else None),
                Field("gill_spacing", requires=IS_IN_SET(list(attr_list["gill_spacing"].keys())), default=inv_attr_list["gill_spacing"][defaults[6]] if on_defaults else None),
                Field("gill_size", requires=IS_IN_SET(list(attr_list["gill_size"].keys())), default=inv_attr_list["gill_size"][defaults[7]] if on_defaults else None),
                Field("gill_color", requires=IS_IN_SET(list(attr_list["gill_color"].keys())), default=inv_attr_list["gill_color"][defaults[8]] if on_defaults else None),
                Field("stalk_shape", requires=IS_IN_SET(list(attr_list["stalk_shape"].keys())), default=inv_attr_list["stalk_shape"][defaults[9]] if on_defaults else None),
                Field("stalk_root", requires=IS_IN_SET(list(attr_list["stalk_root"].keys())), default=inv_attr_list["stalk_root"][defaults[10]] if on_defaults else None),
                Field("stalk_surface_above_ring", requires=IS_IN_SET(list(attr_list["stalk_surface_above_ring"].keys())), default=inv_attr_list["stalk_surface_above_ring"][defaults[11]] if on_defaults else None),
                Field("stalk_surface_below_ring", requires=IS_IN_SET(list(attr_list["stalk_surface_below_ring"].keys())), default=inv_attr_list["stalk_surface_below_ring"][defaults[12]] if on_defaults else None),
                Field("stalk_color_above_ring", requires=IS_IN_SET(list(attr_list["stalk_color_above_ring"].keys())), default=inv_attr_list["stalk_color_above_ring"][defaults[13]] if on_defaults else None),
                Field("stalk_color_below_ring", requires=IS_IN_SET(list(attr_list["stalk_color_below_ring"].keys())), default=inv_attr_list["stalk_color_below_ring"][defaults[14]] if on_defaults else None),
                Field("veil_type", requires=IS_IN_SET(list(attr_list["veil_type"].keys())), default=inv_attr_list["veil_type"][defaults[15]] if on_defaults else None),
                Field("veil_color", requires=IS_IN_SET(list(attr_list["veil_color"].keys())), default=inv_attr_list["veil_color"][defaults[16]] if on_defaults else None),
                Field("ring_number", requires=IS_IN_SET(list(attr_list["ring_number"].keys())), default=inv_attr_list["ring_number"][defaults[17]] if on_defaults else None),
                Field("ring_type", requires=IS_IN_SET(list(attr_list["ring_type"].keys())), default=inv_attr_list["ring_type"][defaults[18]] if on_defaults else None),
                Field("spore_print_color", requires=IS_IN_SET(list(attr_list["spore_print_color"].keys())), default=inv_attr_list["spore_print_color"][defaults[19]] if on_defaults else None),
                Field("population", requires=IS_IN_SET(list(attr_list["population"].keys())), default=inv_attr_list["population"][defaults[20]] if on_defaults else None),
                Field("habitat", requires=IS_IN_SET(list(attr_list["habitat"].keys())), default=inv_attr_list["habitat"][defaults[21]] if on_defaults else None),
                Field("prediction", readable=False, writable=False),
                Field("source_tracking", requires=IS_IN_SET(["frontend", "rest"]), readable=False, writable=False)
)

def predict(varslist):

    if varslist[0][6]=='d' or varslist[0][11]=='u' or varslist[0][16]=='u':
        return "unknown"

    import pandas as pd
    import pickle, os
    modelfile = open(os.path.join(request.folder, 'static/ml/model/final_model.pkl'), 'rb')
    datafile = open(os.path.join(request.folder, 'static/ml/data/mushrooms.csv'), 'r')

    model = pickle.load(modelfile)
    df= pd.read_csv(datafile)

    test = pd.get_dummies(df.append(pd.DataFrame(varslist, columns=[i for i in df.columns]), ignore_index=True, )).drop(
        ['class_e', 'class_p'], axis=1).iloc[-1:]

    try:
        return "edible" if model.predict(test) == 1 else "poisonous"
    except:
        print(len(test.columns))
        for i in test.columns:
            print(i)
        return "error"
