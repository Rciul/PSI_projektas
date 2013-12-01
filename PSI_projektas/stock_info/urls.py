from django.conf.urls import patterns, url
urlpatterns = patterns("",
                       url(r"^stock_info/file_form", "stock_info.views.File_form"),
                       url(r"^stock_info/quality$", "stock_info.views.quality_redirect"),
                       url(r"^stock_info/quality_form$", 'stock_info.views.render_quality'))
