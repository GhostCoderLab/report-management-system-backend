from django.db import models

# コマンド：python manage.py runserver --settings config.settings.development
# コマンド：python manage.py makemigrations ares --settings config.settings.development
# コマンド：python manage.py migrate --settings config.settings.development
# SQLコマンド：DROP DATABASE app;
# SQLコマンド：CREATE DATABASE app;
# SQLコマンド：SELECT * FROM app.Report;

# SQLコマンド：USE app;INSERT INTO Report (name,level,description) VALUES('破損報告書','レベル1','壊しました。');

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