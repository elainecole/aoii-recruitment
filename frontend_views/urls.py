from django.conf.urls import url
import views as v

urlpatterns = [
    url(r'^$', v.base_view, name='base'),
    url(r'^outfit$', v.outfit_view, name='outfit')
]
