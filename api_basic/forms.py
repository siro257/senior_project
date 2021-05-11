from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
Hour_Choices = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ("13", "13"),
    ("14", "14"),
    ("15", "15"),
    ("16", "16"),
    ("17", "17"),
    ("18", "18"),
    ("19", "19"),
    ("20", "20"),
    ("21", "21"),
    ("22", "22"),
    ("23", "23"),
    ("24", "24"),
)

Minute_Choices = (
    ("00", "00"),
    ("05", "05"),
    ("10", "10"),
    ("15", "15"),
    ("20", "20"),
    ("25", "25"),
    ("30", "30"),
    ("35", "35"),
    ("40", "40"),
    ("45", "45"),
    ("50", "50"),
    ("55", "55")
)

Weekday_Choices = (
    ("1", "Monday"),
    ("2", "Tuesday"),
    ("3", "Wednesday"),
    ("4", "Thursday"),
    ("5", "Friday"),
)

class addTimeForm(forms.Form):
    start_break_hour = forms.ChoiceField(choices=Hour_Choices, label=mark_safe('Start time'))
    start_break_minute = forms.ChoiceField(choices=Minute_Choices, label=mark_safe(':'))

    end_break_hour = forms.ChoiceField(choices=Hour_Choices, label=mark_safe('End time'))
    end_break_minute = forms.ChoiceField(choices=Minute_Choices, label=mark_safe(':'))

    def clean_end_break_minute(self):
        start_hr = int(self.cleaned_data['start_break_hour'])
        print(start_hr)
        start_min = int(self.cleaned_data['start_break_minute'])
        end_hr = int(self.cleaned_data['end_break_hour'])
        print(end_hr)
        end_min = int(self.cleaned_data['end_break_minute'])

        if start_hr > end_hr:
            raise ValidationError(_('Invalid end time - end time must be later than start time'))
        if start_hr == end_hr and start_min >= end_min:
            raise ValidationError(_('Invalid end time - end time must be later than start time'))

class addWeekdays(forms.Form):
    weekday = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Weekday_Choices, required=False)