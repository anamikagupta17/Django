we can instal django in virtual environemnt and globally both
    1 virtual environemnt
    * install wrapper
    * create virtual environemnt
    * inside virtual environemnt install django

    2 in cmd : pip install django
MVT(Django) Structure
views: business logics 
templates: presentation or user interface
model: database queries

django-admin startproject  projectname:  create project
python manage.py runserver: start server (inside the project folder)


directory structure
projectname:
    projectname:
        __init__.py : consider as python package(for creating pakage this file shoud be there)
        wsgi.py:(web server gateway interface):describe web server with web application and how web application chained 
             together to process a request,synchronous python apps
        asgi.py:(Asynchronous server gateway interface):successor of wsgi ,interface b/w async-capable python web servers,frameworks,apps
                for both synchronous and Asynchronous
        setting.py : contain all infomation or data about projet settings eg: db,template,validation...
        urls.py : contains infomation  of the url attached with application
        
    manage.py:used to run server, other many things

    __pycache__: cache folder creates automatically
DJANGO_SETTING_MODUL: we need to set setting module ,by default it set projectname.setting module 

** django will ot start if secret key not set

we create multiple apps in one project
create application : python manage.py startapp appname
create multiple apps : 
python manage.py startapp appname1,
python manage.py startapp appname2

after creating apps we need to intall it otherwise it won't  be recognized by django

inside app
*for every function we need to send request(HttpRequest)(this should be first parameter) and
 return response(HttpResponse)
*for every function need to set url 

steps to work in project
1 create project : django-admin startproject projectname
2 chnage directory to the django project : cd directory name
3 create django app : python manage.py startapp appname
4 add/install app  to django project  settings.py
5 write view function inside views.py
  1 open view.py
  2 import HttpResponse 
  3 write view function
  4 add url for each view function in urls.py
  5 save all

** for making each app independent creete urls.py in every application and add url for each function in the same
  application's urls.py and then add that urls.py into main project urls .py  eg: P3(project 3)

template: is a text file . it can generate any text based format(html,xml,csv,..)
 -create templates folder
 -add templates folder path in settings.py
 render(request,template_name,context=dict_name,content_type=MIME_type,status=None,using=None): 
 it combine a given template with the given context dictionary and return HttpResponse object with that rendered text
request: request object
template_name:tempalte file full name or sequence of template files
content type: mime type defualt 'text/html',
status: status code for response default 200
using: name of tempalte engine to use for loadin template

* APP_DIR shoud be true if we create 'template inside application' otherwise it will not take template and no template directory path need to give 
eg:use of template: P4 
* we can create views in sub project folder

Static Foder : for static files like images,vdo,audio,csv file ...
 -we create static foder inside main project inside that we can create other folders(css,images..) also according to need 
 -need to add directory path  to the setting .py file  : eg STATICFILES_DIRS=[static filepath]
 for using static files
  1.load static file :{% load static%}
  2.give reference of static file : {% statc filepath %}

#load template tag { % load moduleName %} : It load custom template tag set 
syntax: {%load emotag %} or {% load emotag othertag %} or {% load cry,lol from emotag%}

#static template tag { % static filename %} : used to give refrence of static files that are saved in static folder in root
syntax: { % static filename %} or {% static path/filename%} or {% static path/filename as variable %}

#{% get_static_prefix %} : it will give static folder path for refrence in place of static we can use this also for more control 

** for variable {{variable name}}

STATIC_URL: used for refrening files stored in STAIC_ROOT folder
STAIC_ROOT:absolute path to the directory where 'collectstatic' will collect staic files for deployment, by default it is null

STATICFILES_DIRS: path of our static file,and also can add multiple additional locations of static files

* for using static foder insdie application no need to do anything means n need to add path
eg: P4
** if we use same css in 2 files for the same tag or class then last one will override above one

inheritance of block
{% extends 'base.html' %} : extends use to inherit base class into html class, this shoud be the first line of html page
* child class block override parent class block 
* block is set of code, we can create multiple block in a page
sytax: {% block blockName%}{% endblock%} or {% block blockName%}{% endblock blockName%}
{{block.super}} : used for get parent class block code without overriding
eg : P5

url : return absolute path
urls.py: urlpatterns=[ path(route,views,kwargs,name)]
{%ul urlname %} : flexible when we chnage url in future
eg: P5

include for template : include html pages
{% include template_var_name %} or {% include 'abcd.html' %}

project deployment

collect all installed packages :  pip freeze >req.txt (store in any file)
create a STATIC_ROOT =base_dir/'static' : any folder for static files
zip you project
go to anywhere python site and upload it
create viretual env : mkvirtualevn myvutrualenvname --python-/usr/bin/python3.7 (your version in which project created)
then insall above pakcage : pip install -r req.txt
change in wsgi file project name and foldername in django section
add static file and path in files tab static section
collect all static files in cmd by commond: python manage.py collectstatic 
reload project 

ORM (object Realtional Mapper): enable application to intract with database(  mysql,sqllite,..)
* create database schema from defined class  or models (means create schema using python classes)
* easy to change database if we use ORM(it automatically change accordingly)
* map data into respected table

QuerySet: contains list of objects and allow to read data from db ,filter or order..
model: each model maps a single database table
modelClass:represent a table in db,each attribute reperent a db field 

model class create table like : ApplicationName_ClassName,and field s will be the table columns
sytax: class className(models.Model):
  field name=models.field Type(arg,option) : field Type: datatype,field name:column name
field name : shoud not contain more then 1 unerscore,lastword shoud not be underscore,not reserved keyword
* if we don't give primary key then it will create a column id autoincrement automatically  

how to use model
* create projectt and then create app
*in setting.py add app name which contains model.py in Installed_APP=[]
*in terminal run python manage.py makemigrations: this will create query from class
*python manage.py migrate : execute the query

Migratons:django's way to propogatechanges of model(adding,deleteing...)
makemigrations: responsible for creating new migrations based on changes in model(generate query or convert class into sql statement or query), also will create a file which contains sql statement(in python .py file) in migrations folder
sytax: python manage.py makemigrations

migrate:used to execute sql statement generated by migrations ,also will execute all applications sql statements if available.aftr execution of sql statement table will be created
syntax: python manage.py migrate


**if you make any changes in your model then you need to run makemigrations and migrate commond then only you will get  those changes in your application

sqlmigrate: dispaly the sql statement of migration
syntax: python manage.py sqlmigrate app_name dbfile_name(migration folder's files)

showmigrations:list of migrations and status


*create superuser for admin : python manage.py createsuperuser
* need to register model fro showing data into admin interface or panel :admin.site.register(Student)
* need to create adminModel class for showing all columns  or multiples columns in admin pannel 

* we shoud use django form in place of normal html becuse it is secure and automated no need to right html code

Django Form:
1.Bound Form  : have data
2.Unvound Form

steps
create a forms.py in app
then create object of form in views.py and then use that object as h template
main tag need to add manully like form,button,table,ul

from rendering options
{{form}} : will render all
{{form.as_table}}: same as above with <tr>
{{form.as_p}}:will render them wraped in tag <p> 
{{form.as_ul}}:will render them wraped in tag <li> 
{{form.name_of_field}}:will render maually as given

manage id
auto_id=False : False will not create id and remove label tag or 
auto_id='txt' # its like true
'id_%s' : in place of id_ any text
fm=StudentRegistration(auto_id='txt%s')  

configure label tags
 fm=StudentRegistration(label_suffix='  ')  : anything in place of null

form fields :
sytax=FieldType(**kwarges)

*required : by default it is True
*label : defive accordignly 
*help_text: any text like error message
*error_message:lets you override default error message
eg: FieldType(erro_message={'required':'Enter Your Name'})
*validators : provide list of validation...
*localize:enables the localization of form data input ,as well as rendered output
*widget: in rendering the fields

eg: P7Forms

**Initial value will give prefrence to the run time(view), if not there in view then willtake form one

CSRF protection: secure site from attackers
** this will add hidden input token with random value in form tag 
{% csrf_token %} 

@form Validation
is_valid() :validate data
syntax:fm.is_valid()
cleaned_data: get only validated data 
syntax: fm.cleaned_data


**nonvalidate: in html5  for not validating  but django validation will run