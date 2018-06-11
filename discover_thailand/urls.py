"""discover_thailand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import views as home_views
from about import views as about_views
from contact import views as contact_views
from accounts import views as accounts_views
from blog import views as blog_views
from .settings import MEDIA_ROOT
from django.views.static import serve
from threads import views as forum_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.get_home, name='home'),

    # about url
    url(r'^about/$', about_views.about, name='about'),

    # contact url
    url(r'^contact/$', contact_views.contact, name='contact'),

    # authentication url
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url('^', include('django.contrib.auth.urls')),

    # blog url
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^blog/$', blog_views.post_list),
    url(r'^blog/(?P<id>\d+)/$', blog_views.post_detail),
    url(r'^blog/top', blog_views.top_posts),
    url(r'^post/new/$', blog_views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$', blog_views.edit_post),

    # forum
    url(r'^forum/$', forum_views.forum),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', forum_views.new_thread, name='new_thread'),

]
