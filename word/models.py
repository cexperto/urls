from django.db import models


# Create your models here.
class Words(models.Model):
    id_w = models.AutoField(primary_key=True)
    url = models.CharField(max_length=300)
    words_repeat = models.CharField(max_length=300)

    class Meta:
        managed = True
        ordering = ('id_w',)
        db_table = 'words'

    def __str__(self):
        return self.url
