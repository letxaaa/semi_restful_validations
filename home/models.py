from django.db import models
from datetime import datetime

# Create your models here.

class ShowManager(models.Manager):
    def validate(self, data):
        errors = []
        if len(data['title']) < 2:
            errors.append('Title needs to be at least 2 characters')
        if len(data,['network']) < 3:
            errors.append('Network needs to be at least 3 characters')
        if len(data['description']) != 0 and len(data['description']) < 10:
            errors.append('Description needs to be at least 10 characters')
        if len(data['release_date']) == '':
            errors.append('Invalid Date')
        else:
            converted_date = datetime.strftime(data['release_date'], '%Y-%m-%d')
            if converted_date > datetime.now():
               errors.append('Invalid Date')

        return errors

    def validate_edit(self, data, id):
        errors = self.validate(data)

        if self.exclude(id=id).filter(title=data['title']):
            errors.append('Title already in use!')