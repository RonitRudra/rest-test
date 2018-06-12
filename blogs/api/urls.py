from django.conf.urls import url
from blogs.api.views import BlogPostRUDView

urlpatterns = [
	url(r'^(?P<pk>\d+)$',BlogPostRUDView.as_view(),name='post-rud')
	]
