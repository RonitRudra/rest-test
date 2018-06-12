from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class BlogPost(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	title = models.CharField(max_length=120, null=True, blank=True)
	content = models.CharField(max_length=120, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = _('blog post')
		verbose_name_plural = _('blog posts')

	def __str__(self):
		return self.user