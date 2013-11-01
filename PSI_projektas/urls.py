from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from PSI_projektas import stock_info
from django.contrib.sites.models import Site

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()
admin.site.unregister(Site)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PSI_projektas.views.home', name='home'),
    # url(r'^PSI_projektas/', include('PSI_projektas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/', include(stock_info.urls)),
)
