from django.db import models


class Classes(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

class Lessons(models.Model):
    name = models.CharField(verbose_name='Название предмета', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Teacher(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=50)
    teacher_class = models.ForeignKey(Classes, on_delete=models.SET_NULL,
            null=True, blank=True) # Может ли учитель вести одновременно 9 и 11 класс?
    lesson = models.ManyToManyField(Lessons)

    def __str__(self):
        return f"{self.fio}, учитель {self.teacher_class.name} класса по предметам {', '.join(lesson.name for lesson in self.lesson.all())}"


    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Tariff(models.Model):
    name = models.CharField(verbose_name='Название тарифа', max_length=100)
    tariff_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    products_price = models.JSONField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'


class Cart(models.Model):
    count = models.PositiveIntegerField(verbose_name='Кол-во продуктов')
    amount = models.PositiveIntegerField(verbose_name='Текущая цена')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

class Products(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    class_product = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name='Класс продукта')
    lesson_product = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name='Урок продукта')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Учитель продукта')
    tariffs = models.ManyToManyField(Tariff, verbose_name='Тарифы')
    custom_price = models.PositiveIntegerField(verbose_name='Специальная цена', null=True, blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.lesson_product.name}. {self.teacher.fio}"
        super(Products, self).save(*args, **kwargs)
