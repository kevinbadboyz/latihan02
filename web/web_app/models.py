from django.db import models

class StatusModel(models.Model):
    status_choices = (('Aktif','Aktif'), ('Non-Aktif', 'Non-Aktif'))
    name = models.CharField(max_length = 100)
    description = models.TextField()
    status = models.CharField(max_length = 20, choices = status_choices, default = 'Aktif')
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.name
