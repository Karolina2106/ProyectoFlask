class Config(object):  #Configura que nuestro servidor se active modo debug o modo desarrollo 
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True