from django.db import models

class Table(models.Model):

    username = models.CharField('Name', max_length=50)
    password = models.CharField('Password', max_length=50)

    def __str__(self):
        return self.username


class Edit(models.Model):
    username = models.CharField('Логин', max_length=500, blank=False, null=True)
    name = models.CharField('ФИО', max_length=500, blank=False, null=True)
    age = models.IntegerField('Ваш возраст', blank=False, null=True)
    skills = models.TextField('Ваши навыки', max_length=500, blank=False, null=True)
    job_places = models.TextField('Предыдущая работа', max_length=500, blank=False, null=True)
    money = models.IntegerField('Зарплатные ожидания', blank=False, null=True)

    def __str__(self):
        return self.username

    def get_value(self):
        return [self.username, self.name, self.age, self.skills, self.job_places, self.money]


