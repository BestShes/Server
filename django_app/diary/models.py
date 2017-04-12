from django.conf import settings
from django.db import models


class Diary(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    cover_image = models.ImageField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return '작성자 : {author} - 제목 : {title}'.format(
            author=self.author,
            title=self.title,
        )


class Post(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    cover_image = models.ImageField()

    class Meta:
        order_with_respect_to = 'diary'

    def __str__(self):
        return '{diary} - 내용 : {content}'.format(
            diary=self.diary,
            content=self.content,
        )


class PostPhoto(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post')
    gpsLatitude = models.FloatField("Latitude", blank=True, null=True)
    gpsLongitude = models.FloatField("Longitude", blank=True, null=True)

    class Meta:
        order_with_respect_to = 'post'

    def __str__(self):
        return '{post} / {photo}'.format(
            post=self.post,
            photo=self.photo,
        )
