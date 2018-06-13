# ACCOUNTS FOLDER
from django.conf.urls import url
from accounts.views import do_login, register, do_logout, profile  
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

    
urlpatterns = [
    url(r'^login', do_login, name='login'),    
    url(r'^register$', register, name='register'), 
    url(r'^logout$', do_logout, name='logout'),
    url(r'^profile$', profile, name='profile'),
    url(r'^password-reset/$', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    url(r'^password-reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^password-reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
        url(r'^password-reset/complete/$', password_reset_complete, name='password_reset_complete'),
]