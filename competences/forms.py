from django import forms


class Form(forms.Form):
    CHOICES = [
        ('C', 'Компетенция'),
        ('P', 'Профессия'),
        ('S', 'Стандарты'),
        ('J', 'Конкретика'),
    ]
    request = forms.CharField(label="job name", max_length=100)
    in_type = forms.CharField(label="Ввод", widget=forms.RadioSelect(choices=CHOICES))
    out_type = forms.CharField(label="Вывод", widget=forms.RadioSelect(choices=CHOICES))
