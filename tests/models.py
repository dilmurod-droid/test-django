from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return f'{self.name}'
class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    variants=models.CharField(max_length=255,default='a)3,b)5,c)2,d)6')
    def __str__(self):
        return f'{self.text}'

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question}'
