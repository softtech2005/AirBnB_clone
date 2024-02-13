from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())  # Assign a unique id when an instance is created
        self.created_at = datetime.today()  # Assign the current datetime when an instance is created
        self.updated_at = datetime.today()  # Assign the current datetime when an instance is created and update it every time the object is changed
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, tform))  # Convert datetime strings to datetime objects
                else:
                    setattr(self, k, v)
        else:
            models.storage.new(self)  # Add the new instance to the storage system

    def save(self):
        """Update updated_at with the current datetime and save the changes."""
        self.updated_at = datetime.today()  # Update updated_at with the current datetime
        models.storage.save()  # Save the changes to the storage system

    def to_dict(self):
        """Return a dictionary containing all keys/values of the BaseModel instance.

        Includes the key/value pair __class__ representing the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()  # Convert created_at to ISO format
        rdict["updated_at"] = self.updated_at.isoformat()  # Convert updated_at to ISO format
        rdict["__class__"] = self.__class__.__name__  # Add the class name to the dictionary
        return rdict

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)  # Format the string representation
