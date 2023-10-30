from django.db import models

# Create your models here.
class Diary(models.Model):

<<<<<<< HEAD
    # user = models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル',max_length=40)
    content = models.CharField(verbose_name='本文',blank=True,null=True)
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    # updateed_at = models.DateTimeField(verbose_name='更新日時',auto_now=True)

    # photo1 = models.ImageField(verbose_name='写真1',blank=True,null=True)
    # photo2 = models.ImageField(verbose_name='写真2',blank=True,null=True)
    # photo3 = models.ImageField(verbose_name='写真3',blank=True,null=True)

=======
    title = models.CharField(verbose_name='タイトル',max_length=40)
>>>>>>> ce8f1603a7b4955e9d1ec2996b6376a5e5e36052
    class Meta:
        verbose_name_plural = 'Diary'

    def __str__(self):
<<<<<<< HEAD
        return self.title

=======
        return self.title
>>>>>>> ce8f1603a7b4955e9d1ec2996b6376a5e5e36052
