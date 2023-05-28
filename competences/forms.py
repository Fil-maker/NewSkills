from django import forms


class Form(forms.Form):
    CHOICES = [
        ('C', 'Компетенция'),
        ('P', 'Профессия'),
        ('S', 'Стандарты'),
        ('J', 'Конкретика'),
        ('I', 'Общепрофессиональные компетенции'),
    ]
    request = forms.CharField(label="job name", max_length=200)
    in_type = forms.CharField(label="Ввод", widget=forms.RadioSelect(choices=CHOICES))
    out_type = forms.CharField(label="Вывод", widget=forms.RadioSelect(choices=CHOICES))
