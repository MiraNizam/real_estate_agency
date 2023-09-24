from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField('Наличие балкона', db_index=True, null=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    new_building = models.BooleanField('Новостройка', blank=True, default=None)
    liked_by = models.ManyToManyField(User, related_name="liked_flats", verbose_name='Кто лайкнул', blank=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Claim(models.Model):
    user = models.ForeignKey(User, related_name='user_claims', on_delete=models.CASCADE, verbose_name='Кто жаловался')
    flat = models.ForeignKey(Flat, related_name='flat_claims', on_delete=models.CASCADE, verbose_name='Квартира, на которую пожаловались')
    text = models.TextField('Текст жалобы')

    def __str__(self):
        return f'{self.user} {self.flat}'


class Owner(models.Model):
    full_name = models.CharField(verbose_name='ФИО владельца', max_length=200, db_index=True)
    phonenumber = models.CharField(max_length=20, verbose_name='Номер владельца', db_index=True)
    pure_phonenumber = PhoneNumberField(blank=True, verbose_name='Нормализованный номер владельца', db_index=True)
    flats = models.ManyToManyField(Flat, related_name='owners', verbose_name='Квартиры в собственности')

    def __str__(self):
        return self.full_name
