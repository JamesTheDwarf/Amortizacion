from django.conf.urls import url
import views as T_views

urlpatterns = [
    url(r'^$', T_views.Index.as_view(), name='Index'),
]