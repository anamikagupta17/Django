from django.dispatch import Signal,receiver

#create signal 
nofitifaction=Signal(providing_args=['request','user']) #these request or user is not getting check so its not compalsary


#receiver function
@receiver(nofitifaction)
def show_notification(sender,**kwargs):
    print('---------------------------------')
    print('Sender :',sender)
    print(f'Kwargs : {kwargs}')
    print('Notification')
    print('-------------------------')