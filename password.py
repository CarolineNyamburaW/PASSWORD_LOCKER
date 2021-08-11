class User:
    """
    a class that generates new instances of passwords
    """

    user_list = []

     def __init__(self,first_name,last_name,password):
        """
        _init_ a method that helps to define properties for our objects.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.password = password