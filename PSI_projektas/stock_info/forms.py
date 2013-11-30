from django.forms.forms import Form
from django.forms.fields import FileField, DateField, CharField, IntegerField
from django.utils.translation import ugettext_lazy
from django.forms.widgets import DateInput
from django.forms.models import ModelForm
from PSI_projektas.stock_info.models import Orderfailure, Operation
from django.core.exceptions import ValidationError

class FileForm(Form):
    file_name = FileField(label=ugettext_lazy('File name'))

class QualityForm(Form):
    date_from = DateField(label=ugettext_lazy('Date from'))
    date_to = DateField(label=ugettext_lazy('Date to'))
    group = CharField(label=ugettext_lazy('Group'))

class OrderFailureForm(ModelForm):
    operation = IntegerField(label=ugettext_lazy('Operation ID'))
    
    class Meta:
        model = Orderfailure
        
    def clean_operation(self, *args, **kwargs):
        operation_id = self.cleaned_data['operation']
        operations = Operation.objects.filter(operation_id=operation_id)
        if operations.count() == 0:
            raise ValidationError(ugettext_lazy('Operation provided not found'))
        return operations[0]