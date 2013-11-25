from django.forms.widgets import Widget
from django.utils.html import format_html
from django.forms.util import flatatt
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text
from itertools import chain

class ListWidget(Widget): 
    allow_multiple_selected = False

    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        output = [format_html('<ul{0}>', flatatt(final_attrs))]
        options = self.render_options(choices, [value], name)
        if options:
            output.append(options)
        output.append('</ul>')
        return mark_safe('\n'.join(output))
    
    def render_option(self, selected_choices, option_value, name, option_label):
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''
        return format_html(u'<li class="changelist_actions" value="{0}"{1}><a href="/admin/handleAction?Action={3}">{2}</a></li>',
                           option_value,
                           selected_html,
                           force_text(option_label),
                           name)

    def render_options(self, choices, selected_choices,name):
        # Normalize to strings.
        selected_choices = set(force_text(v) for v in selected_choices)
        output = []
        for option_value, option_label in chain(self.choices, choices):
            if isinstance(option_label, (list, tuple)):
                if option_value:
                    output.append(format_html('<optgroup label="{0}">', force_text(option_value)))
                    for option in option_label:
                        output.append(self.render_option(selected_choices, name, *option))
                    output.append('</optgroup>')
            elif option_value:
                output.append(self.render_option(selected_choices, option_value, name, option_label))
        return '\n'.join(output)

        