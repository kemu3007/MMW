from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '{} ¥{}'.format(self.name, self.calc_sum()['money__sum'])

    def calc_sum(self):
        return self.order_set.aggregate(models.Sum('money'))


class Order(models.Model):
    money = models.IntegerField()
    date = models.DateField(null=True)
    contents = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    active = models.BooleanField(default=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{}-¥{}({})'.format(self.date, self.money, self.tag.name)

    @staticmethod
    def calc_sum():
        return Order.objects.all().aggregate(models.Sum('money'))


