from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    # author : 작성자 추가
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')

    # modify_date : 수정일시 추가
    modify_date = models.DateTimeField(null=True, blank=True)

    # voter : 추천인 추가
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    # author : 작성자 추가 (null값 허용)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author_answer')

    # modify_date : 수정일시 추가
    modify_date = models.DateTimeField(null=True, blank=True)

    # voter : 추천인 추가
    voter = models.ManyToManyField(User, related_name='voter_answer')

    def __str__(self):
        return self.content