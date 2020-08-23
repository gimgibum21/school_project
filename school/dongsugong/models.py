from django.db import models


class DSG(models.Model):
    class Meta:
        ordering = ['-created_at']
    grade = models.CharField(max_length=20, default="1학년", verbose_name="학년")
    subject = models.CharField(max_length=20, default="", verbose_name="과목")
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    image = models.ImageField(upload_to="dongsugong/img", blank=True, verbose_name="사진")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="게시일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")



