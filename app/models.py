from django.db import models




# Create your models here.
class Specialists(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
       return f'{self.title}'

class Doctors(models.Model):
    fio = models.CharField(max_length=100)
    spec =models.ForeignKey(Specialists, on_delete= models.CASCADE)
    experience = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/doctor/')

    def __str__(self):
       return f'{self.fio}'


class Entry(models.Model):
    fio = models.CharField(max_length=100,verbose_name='ФИО')
    phone_number = models.IntegerField(verbose_name='Номер телефона')
    spec = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name='Выберите специалиста')
    specname = models.ForeignKey(Specialists, on_delete=models.CASCADE , verbose_name='Выберите специальность')
    data = models.DateTimeField(verbose_name='Дата 2020-12-01 12:30')

    def __str__(self):
        return f'{self.fio}'

