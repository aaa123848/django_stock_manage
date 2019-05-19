from django.db import models

# Create your models here.


class User(models.Model):
    
    gender = (
        ('male','boy'),
        ('female','girl'),
    )


    name123 = models.CharField(max_length=256, unique=True, verbose_name='username')
    password = models.CharField( max_length=256, verbose_name='password')
    email = models.EmailField(unique = True, verbose_name='email')
    sex = models.CharField(choices=gender, max_length=256, verbose_name='sex')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='create time')

    def __str__(self):
        return self.email


    class Meta:
        ordering = ['-create_time']
        verbose_name = 'user'
        verbose_name_plural = 'users' 

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)