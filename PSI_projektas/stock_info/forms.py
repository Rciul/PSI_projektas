from django.forms.forms import Form
from django.forms.fields import FileField, DateField
from django.utils.translation import ugettext_lazy

class FileForm(Form):
    file_name = FileField(label=ugettext_lazy('File name'))

class QualityForm(Form):
    date_from = DateField(label=ugettext_lazy('Date from'))
    date_to = DateField(label=ugettext_lazy('Date from'))