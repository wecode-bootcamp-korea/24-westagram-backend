from django.db import models

class Post(models.Model):
    caption      = models.TextField(default="", blank=True)
    posting_time = models.DateTimeField(auto_now_add=True)
    user         = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="post")
    location     = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "posts"

    def __str__(self):
        return self.caption

class Image(models.Model):
    url  = models.URLField()
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="image")

    class Meta:
        db_table = "images"

class Comment(models.Model):
    comment         = models.CharField(max_length=200)
    commenting_time = models.DateTimeField(auto_now_add=True)
    user            = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="comment")
    post            = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comment")
    parent_comment  = models.ForeignKey("self", on_delete=models.CASCADE, related_name="child_comment", null=True)

    class Meta:
        db_table = "comments"

class Like(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="like")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="like")

    class Meta:
        db_table = "likes"

class Follow(models.Model):
    following = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="following")
    follower = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="follower")

    class Meta:
        db_table = "follows"

    def __str__(self):
        return self.follower.name + " following " + self.following.name