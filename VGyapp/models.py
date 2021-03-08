from django.db import models

# Create your models here.
class UserModel(models.Model):
    GENDER_CHOICES = (
        (1, '男性'),
        (2, '女性'),
        (3, 'その他'),
    )
    AGE_CHOICES = (
        (1, '10代'),
        (2, '20~60代'),
        (3, '70代以上'),
    )
    gender = models.IntegerField(verbose_name='性別', choices=GENDER_CHOICES, blank=True)
    age = models.IntegerField(verbose_name='年齢', choices=AGE_CHOICES, blank=True)

class VgModel(models.Model):
    Vg_name = models.CharField(verbose_name='野菜の名前', max_length=100)
    Vg_energie = models.CharField(verbose_name='エネルギー', max_length=100, null=True)
    Vg_protein = models.CharField(verbose_name='プロテイン', max_length=100, null=True)
    Vg_lipids = models.CharField(verbose_name='脂質', max_length=100, null=True)

    def __str__(self):
        return self.title