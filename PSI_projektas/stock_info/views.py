from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.
def metodas(request):
    kintamasis = 52
    kintamasis2 = [14,25,"iidfidj"]
    return render_to_response("admin/failas.html",{"raktas1":kintamasis,
                                            "raktas2":kintamasis2},
                       RequestContext(request, {}),)
    