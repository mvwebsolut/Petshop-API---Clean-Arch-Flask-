from sqlalchemy import create_engine

class DBConnectionHandler:
    """ sqlalchemy database connection """
    def __init__(self):
        self.__connection_string = "sqlite:///database.db"
        self.session = None

    def get_engine(self):
        """ Return connection engin
        param - None
        return - engine connection to database
        """
        engine = create_engine(self.__connection_string)
        return engine
    
    


