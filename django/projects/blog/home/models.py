from django.db import models
from django.utils.html import format_html


class Category(models.Model):

    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/category/")
    add_date = models.DateTimeField(auto_now_add=False, null=True)
    
    def image_tag(self):
        return format_html('  <image src="/media/{}"  style="width:40px;hight:40px;border-radious:50%;" />'.format(self.image))

    def __str__(self):
        return self.title

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    content=models.TextField()
    url=models.CharField(max_length=150)
    image = models.ImageField(upload_to="media/post/")

    # def image_tag(self):
    #     return format_html('<image scrc="/media/{}" style "width:40px;height:40px;border-radious:50%"/>'.format(self.image))
    

    def __str__(self):
        return self.title
    

    
    



# Create your models here.
