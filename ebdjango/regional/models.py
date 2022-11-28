from django.db import models

class Regional(models.Model):
    regional = models.CharField(max_length=200, default=0)

    def __str__(self):
        return self.regional

    class Meta:
        db_table = 'regional'
        managed = True
        verbose_name = 'Regional'
        verbose_name_plural = 'Regional'
