from django.shortcuts import render_to_response
import random
import datetime
import time
from django.template.context import RequestContext
from django.contrib import messages
from django.http import HttpResponseRedirect
from PSI_projektas.stock_info.models import Orderfailure

def draw_chart(request):
    
    def validate_and_get_date(request):
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        date_from = datetime.datetime.strptime(date_from, '%Y-%m-%d').date()
        date_to = datetime.datetime.strptime(date_to, '%Y-%m-%d').date()
        if date_to < date_from:
            messages.error(request, _('Invalid period entered'))
            return HttpResponseRedirect(request.META['HTTP_REFERER']), date_to, date_from
        return None, date_to, date_from
    
    group = None
    if request.GET.get('group'):
        group = request.GET.get('group')
    response, date_to, date_from = validate_and_get_date(request)
    if response:
        return response
    quality = Orderfailure.calculate_service_level(date_from, date_to, group)
    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_series = {"tooltip": {"y_start": "", "y_end": " calls"},
                    "date_format": tooltip_date}
    chartdata = {
        'x': quality.keys(),
        'name1': _('Quality cofficient'), 'y1': quality.values(), 'extra1': extra_series
    }
    charttype = "cumulativeLineChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    rc = RequestContext(request, {})
    rc.autoescape = False
    res = render_to_response('graph.html', data, rc)
    return res
