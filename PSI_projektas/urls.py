from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from PSI_projektas.stock_info import urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()
#admin.site.unregister(Site)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PSI_projektas.views.home', name='home'),
    # url(r'^PSI_projektas/', include('PSI_projektas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(urls)),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),    
)
