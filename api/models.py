from django.db import models

class Report(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = 'Report'
        verbose_name = '報告書'
        verbose_name_plural = '報告書'

    def __str__(self):
        return self.name