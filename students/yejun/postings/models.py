from django.db import models


class Posting(models.Model):
    feed_text = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)


class ImageURL(models.Model):
    image_url = models.URLField()
    postings = models.ForeignKey("Posting", on_delete=models.CASCADE)