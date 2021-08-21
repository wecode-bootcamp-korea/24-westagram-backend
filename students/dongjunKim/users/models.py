from django.db import models

class User(models.Model):
    name     = models.CharField(max_length=30)
    email    = models.CharField(max_length=100)
    password = models.CharField(max_length=25)
    phone    = models.CharField(max_length=15)
    class Meta:
        db_table = 'users'

    #다음과 같은 필드들이 추가될 수 있음.
    #주민번호, 성별, 주소, ..
    
    #향후 프론트 파트와의 협업을 진행할 때 달라질 수 있음.
    #현재 진행하고 있는 프로젝트는 '위스타그램 - 벡앤드' 이므로
    #기본 필드만 추가하였음.
