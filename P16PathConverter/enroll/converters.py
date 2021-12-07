class AnyCLassName:
    regex='[0-9]{4}'
    def to_python(self,value):
        return int(value)
    
    def to_url(self,value):  # this convert value to the url format 
        return f'{value:4d}' # we can use any formatting method