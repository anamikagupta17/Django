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
using: name of tempalte engine to use for loading template

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
*widget: in rendering the fields : default widget : TextInput

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

form Fields:formField(**kwargs)
name=forms.CharField(min_lenth,max-lenth,strip,empty_value='df',erro_message={'required':"Enter your message"})
strip: remove space from string before and after by default it is True
empty_value : set some value as a empty so it will not give error while submitting

agree=forms.BooleanField(label='I agree')
price =forms.IntegerField(min_value=10,max_value=20)
rate =forms.DecimalField(min_value=10,max_value=20,decimal_place=1)
ft =forms.FloatField(min_value=10,max_value=20)

there are many form feilds

validation for specific fields (specially for custom validation for a field)
syntax: need to write in forms.py
def clean_fieldname(self):
     valname=self.cleaned_data['fieldname']
        if len(valname) < 4:
            raise forms.ValidationError('Enter more then 3 char ')
        return valname

validationof django form at once(speciallay when custom validation)
clean():
cleaned_data = super().clean() : parent class validation logic also maintained

field error : {{field.errors}} it will return in <ul class='errorlist'>
error hooks : error_css_class='error' and required_css_class='required' : this will add one error and requried occur

ModelForm: get rid of writing data 2 times(forms.py,models.py) : remove redendency
(when we need same data in form which we wanted to insert)

*for updating data in model form we can create instance  and update data
 pi=Student.objects.get(pk=1) : model class object
 fm=StudentRegistration(request.POST,instance=pi) #instance for update

 dynamic url
 str:<my_id> : by default str
 path converter
 int:<int:my_id> : convert int or 0
 slug:<slug:my_id>: string with ASCII number,underscore and hyphen eg:egab-d23
path(route,view,kwargs,name) 
kwargs : dictionary 
{'check':'ok'}

custom path converter 
to_python: Converts the input value into the expected Python data type
to_url:  convert input value to the url format 

**ModelForm  :(get data of from fields with  different types) 
 class Reg(froms.ModelForm):
   class Meta:
     model=User
     fields =['id','name'] : fields name which we want to fetch (Fields Name)
     or 
     fields ='__all__' : set all fields (__all__)
     or
     exclude=['name']: this will exclude name and set all other (exclude)


** ModelFrom Inheritance     :
 # can use form API(normal form) anf modelFrom in a single class ,however modelFrom  appears first in MRO
 # child from class inherit Parent class and also can inherit meta class of parent (if child class don't have meta then it will take parents meta class)
 eg : 
 fields in model : student_name,teacher_name,email,password (means using one table)
 class Student(froms.ModelForm):
   class Meta:
    model=User
    fields =['student_name','email','password']

  class Teacher(Students):
    class Meta(Student.Meta):
     fields =['teacher_name','email','password']    

 message Level : that define what kind of message is there eg: SUCCESSS,INFO,WARNING
 message tags : we can use for css   eg: success ,info 
 message automatically goes to the template
get_level(): get current Level
eg: messages.get_level(req) 
set_level():can set level 
eg: messages.set_level(req,)

** by default debug level will not display untill you are not setting apart from that all level (higher) will display

** we can change tag names in settings.py.
from django.contrib.messages import constants as  messages
 MESSAGE_TAGS={
   messages_s.ERROR:'danger'
 }

get_messages(request):this will get messages outside template like in any python file
eg: msg=messages.get_messages(request) 


Authentication: means validating  user or anything
Authorization : process to check the rights for the authenticated user

**by default admin has all permissions
""perms : store all the permissions of logged in user

**permissions: create automatic  when we create model(view,add,delete,change)


Cookies : stored in client machine
Cookies limitation in django :
*can increate loading time first time if more data
*can only store 4060 byte data not more then this
*user can missuse detail


session:stored in server side
** store a session id in cookies client machine  and that seesion id stored in db as session key
** session stored in database
** by default session expire after 2 weeks
flush : delete session from cookies and database

** for path,timezone,session_cookie_age.. we need to  do all in settings py.file
session_httponly : if true then in client side we can not access cookies  by using javascript

***
if want to set session age for all then we can set in settings.py : session_cookie_age  =10(sec)
**
request.seesion.modified=True : this will modify session time (till given time means age) 

Session in file:(it will store seesion data in file in place of db)
in settings.py need to rewrite seesion engine and need need to set seesion path
SESSION_ENGINE='Django.contrib.seesion.backends.file'
SESSION_FILE_PATH=BASE_DIR/'session'  :session is folder name


Cache:store data to sppedup your site
we can store 
 1.full site,2.view base,3.template fragment(any part of html code)
 can store in 
1: db 
2. file
3. local memory


** set time : TIME_ZONE = 'Asia/Kolkata' in settings .py also USE_TZ=False
1 Full site or per Site
need to add 2 middleware in settings.py
DB:
 need to define Cache tables and type  in settings.py
syntax:
CACHES= {
  'default':{
      'BACKEND':'django.core.cache.backends.db.DatabaseCache',
      'LOCATION':'enroll_cache'
  }
}

need to run commond to create cache table : python manage.py createcachetable

file: need to set
CACHES= {
  'default':{
      'BACKEND':'django.core.cache.backends.filebased.FileBasedCache',
      'LOCATION':'C:\Users\Anamika Gupta\Desktop\Python\Django\P28Cache\P28Cache\cache'  #file path
  }
}

local memory : this is by default if no one else is specified
CACHES= {
  'default':{
      'BACKEND':'django.core.cache.backends.locmem.LocMemCache',
      'LOCATION':'unique-snowflake'  #by default any name
  }
}

eg: P28Cache(on change of course html file, new changes will display only when cache expire)

2. Per View(for per url diiferenct ache will create)
need to add 2 middleware in settings.py
from djnago.views.decorators.cache import cache_page
@cache_page(timeout,cache,key_prefix)
or 
can use in url also
urlpatterns=[
path('', cage_page(40)(views.home) ,name='home'),
]
timeout:cache timeout in seconds
cache:cache
key_prefix:any key (will overide depend on view)

3 tempalte fragment cache:
{% load cache %}  : need to add in html at the top
{% cache timeout name variable using="" %} {% endcahce name%} : code insdie this block will be cached
using : this will be last tag for cache eg : using='localcache' if not abilabe then will use default

**if timeout None then it will cache for forver



Low Level Cache API : cache set of code when data didnt change frequently(no need to add middilewares)


Signals:
1.sender:who sends signal
2.signal : signal
3.reciver:who recive signal

can use 2 methods
1. using: user_logged_in.connect(login_success,sender=User)
2. using decorators

need to add signals in apps.py and init.py

**can use signals for getting the ip of user or login count,track login or track failed login  or many things....

Custom Signals: (we don't add anything in apps.py and init.py:reminder)
send() : does not catch exceptions //used for sending signals
send_robust():can exceptions  //used for sending signals


Middleware: (midiaters)
 It is framework of hooks,its low level plugin
*built in middleware : in settings.py there are many middlewares
*custom middleware:

eg:  sender ->request -> middileware1 ,middileware2,..... ->reciver(view) response  vice versa
 middileware also can respond (means send response)
** middilewares can live any where in python
after creating middileware need to add in settings.py in a order for activating

**get_response: goes to next middleware or view (if no  next middileware then go to the view)

Middleware Hooks: these hooks we can use only in class based middilewares
process_view(req,view_fnc,view_args,view_kwargs):
process_exception(req,exception): for handling exceptions ,it should run either None  or httpResponse
process_template_response(request,response):call just after view finish,it return templateResponse from view or from middilewares

built in middilewares:
these all define in common middileware
**APPEND_SLASH : True in url if you don't give / at the end it take automatic if True else will not dispay view
**PREPEND_WWW:True take www by fedault if not given
**MessageMiddleware:for message
**SessionMiddleWare: for session
**AuthMiddleware : authentication
etc....
in settings.py : APPEND_SLASH=False we can do chnages(no recommanded)

##middilewares set globally


Query Set API : used for database to fetch ,order,filter,...
eg :
all():fetching all data
students=Student.objects.all() 
print('Sql Query : ',students.query) # only for query set

filter(**kwargs): return queryset always with matching data
exclude(**kwarges): return not matching data
order by(*fields):  in case of name order using uni code number not alphapet number so difference Capital or small
 'fields':Ascending oreder
 '-field':decending order

reverse() : rever of data
values(): return dictionary list if no values given
disticnt(): repmve duplicate
values_list(): return tuples for name we need to give Name=Ture
using(alias): in case of multiple db eg: students=Student.objects.using('default')
date(field,kind,order=ASC,txinfo=None)
 field: field name
 kind:year,month,day week...

datetimes(field,kind,order=ASC,txinfo=None) : return datetime
none(): return empty query set
union(*other_qs,all=False):   combine 2 or more
 query sets  select only distict value if you want allow duplicate need to set all=True
 columns shoud be equal in all tables

intersection(*other_qs):
difference(*other_qs): get the difference data
raw(query,params=None,translation=None): for custom query
AND,OR : combine to query set eg 1: stu=Student.objects.filter(marks=80) & Student.objects.filter(city='Lucknow')
eg 2: stu=Student.objects.filter(Q(marks=80)& Q(id=2))
 
** these all above method return query set

 methods  return single query set:
  get(pk or colname):return single object,col name should be unique
  first(): return first matched object by default order by primary key
  last():return last matched object by default order by primary key
  latest(field) : return latest object(new)
  earliest(field): return earliest (old)
  exists(): return true if queryset have result else false

method not retun new query set  :
create(): insert and save data in table
get_or_create(default=nONE,**kwargs): get if exist else create
update():first filter then update and update work on query set only
students=Student.objects.filter(name='Anamika').update(city='Lucknow')
update_or_create(default=nONE,**kwargs): update if exist else create create only if not given field are set to null
bulk_create(objs):create multiple,need to give list of objects and
  this method will not trigger pre_save and post_save signals
  also will not work in child inheritance 

bulk_update(objs,field,batch_size=None):update bulk date can not update primary key
batch_size : control  how many objects save in one query
in_bulk(): take list of field values[id,name]

delete(): delete data


Field Lookups: mainly used for sql where clause 
syntax:field__lookuptype=value
 exact: exact match ,case sensitive
 iexact: exact match with case insensitive
 date,time,sec,hour,mintue: look works with only datetime type datatype
 year,week,day,weekday,quarter: both date and datetime both


** Aggregate function works on query set

Q object: encapsulate a collection of keywords

Model Inheritance Abstract Class: it will  used when we need common information in many models or model class
 abstract class  will not create db table or manger(object)
 neet to add class Meta and abstact =True thn only a model class will be Abstract class
 child class can override base class method,objects
 eg P41

 Multi Table Inheritance: each model have there own table means base class and child class both will have tables
 connect tables by forieg key (child class inherit fields of baseclass)
 (one to one relation)
 eg: P42

 Proxy Model:want to change behaviour of model (behave differently)(use for different behaviour)
 it create proxy of original model ,need to set proxy attribute of meta class True
 ** proxy model need to inherit from one non-abstract clsss(means class shoud not be abstract class)
 ** can't inherit from multiple non-abstrct class
 ** proxy model can inherit from any number of proxy model
 eg:43 (create one table but display in both models  and if insert in onetable but  will display for both models)


 Model Mangaer: in model db objects is a Mangaer ( by default : objects=models.Manager(), already define so no need to set this)
 we can chnage manager name in model we can change manager name.
 eg : P44

 Custom Model Manager: for custom queries we use this to save time
  * used in modifying  initial queryset
  * can add extra custom manger methods 

Model Realionship : we can give choice who can add page or not (page means other table record)
 1. One to One eg: can only have one to one record in 2 tables only 1-1 row in each table
    *CASCADE : if user deleted then all pages or record in other table with that user will be deleted
    *PROTECT : can not delete user because page created with this user
    ** Reverse Deletion: if we wanted to delete user on delete of page then need to create signals(post_delete) and write custom code 
    syntax: in signals.py
    @reciver(post_delete,sender=Page)
    def delete_related_user(sender,instance,**kwargs):
    instance.user.delete()
 2. One to many : one user create multiple post or pages
 3. many to many :multiple users can write one song or vice versa



 Class Based View: well organised code,clean code, specific method for get and post,reuse code
 1.base view
    .View: need to write get,post function depend on request
    .TempalteView :renders given template and capture parameter of url  
    .RedirectView : redirect to a given url
 2.generic view: reusablitiy for common task,predefined code for showing ,adding..
   .Display View: list view,detail view : for displaying data
   .Editing View : form view,Create view,Delete View,Update View
   .Date View : date view,archive view,month archive,date archive...
   
   List View: by default template Name( eg modalClassname_list )
   Detail View : will give detail of a object for that Need a pk or slug becsue that is detailed view
   Form View : to show form and get form data
   Create View: it will give from and also save data into db
   Update View: update data in same create form
   Delete View : Delete data


 ##**kwargs : when multiple keyword arguments need to pass can fetch by key
 ##*args : argument without keywords can fetch by index


 Authentication View: we will get predefined login,logout,change password,reset password..... in auth 
  for using these all we need to include url and need to create templates


  **for testing mail  in local to get reset link in console we can add in setting 
  : EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
  for changing by default login redirect , add in setting :LOGIN_REDIRECT_URL='/dashboard/'


  login decorator: if login required set then any page will be display when logged in else redirect to login
  eg: @login_required
  @staff_member_required: only for staff. staff can see the view

django.contrib.auth.view :
 LoginView: django.contrib.auth.view.LoginView
 LogutView: django.contrib.auth.view.LogutView,Password,.....


 connect other db settings.py:
 DATABASE={
  'default':
  {
    'ENGINE':'django.db.backends.mysql', //django.db.backends.oracle or postgres for oracle,postgres same for others
    'NAME':'db_name',
    'USER':'root',
    'PASSWORD':'',
    'HOST':'localhost',
    'PORT':'port number'#optional
  }
 }

 Pagination : one page to other page with next/previous links
 FBV(FunctionBasedView): if we give string in url then it will redirect to first page and if int then redirect to last page
 CBV(ClassBasedView) : only in 'last' case we write then redirect to last page else error,for error handling need to right a method 


 Django Security: Django provide some protections and also user need to take care of few 
 XSS(Cross Site Scripting) Protection
 CSRF(Cross Site Request Forgery) Protection
 SQL Injection Protection
 Click Jacking Protection
 SSL/HTTPS # you should use for your site
 Host Header Validation
 Refferrer Policy
 Session Security
 User Upload Content

 * keep your SECRET_KEY always secret for every project
 * limit the accessbility of cache system and db using firewll :good ieda