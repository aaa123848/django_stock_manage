from django.db import models

# Create your models here.


class stock(models.Model):
    itemname = models.CharField(verbose_name=u'商品名稱', max_length=512)
    itemspec = models.CharField(verbose_name=u'商品規格', max_length=512)
    safty_stock= models.IntegerField(verbose_name=u'庫存安全量', max_length=512 )
    sell_platform = models.CharField(verbose_name=u'販售平台', max_length=512 )
    sum_import= models.IntegerField(verbose_name=u'總入庫數量', max_length=512 )
    sum_output= models.IntegerField(verbose_name=u'總出庫數量', max_length=512 )
    stock = models.IntegerField(verbose_name=u'現存數量', max_length=512 )

    #interfirld 找一下
    
    

    def __str__(self):
        return self.itemname

    class Meta:
            ordering = ('itemname', 'itemspec' )
            verbose_name = 'itemname'
            verbose_name_plural = 'itemnames' 



class ImportFile(models.Model):
    file = models.FileField(upload_to='File')
    name = models.CharField(max_length=50, verbose_name=u'檔名')
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name