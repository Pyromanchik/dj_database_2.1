from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=256)
    subject = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=256)
    teachers = models.ManyToManyField(Teacher, related_name='students', verbose_name='Учителя')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        ordering = ['name']

    def __str__(self):
        return self.name