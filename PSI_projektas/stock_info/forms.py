from django.forms.forms import Form
from django.forms.fields import FileField
from django.utils.translation import ugettext_lazy

class FileForm(Form):
    file_name = FileField(label=ugettext_lazy('File name'))
    