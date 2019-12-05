from django.db import models

class Course(models.Model):
    """Clase que describe los registros en la tabla de cursos Course."""
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=180)
    description = models.TextField()

    def __str__(self):
        return self.name

#class ClassName(object):
#
#    def __init__(self, arg):
#        super(, self).__init__()
#        self.arg = arg
