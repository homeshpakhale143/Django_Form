from django import forms
g={'M':'Male', 'F':'Female'}
c={'SQL':'SQL','Python':'Python','Java':'Java'}

class CollegeForm(forms.Form):
    Sname=forms.CharField(max_length=100)
    Sage=forms.IntegerField(min_value=18)
    Semail=forms.EmailField()
    Surl=forms.URLField()
    Saddress=forms.CharField(widget=forms.Textarea())
    Spassword=forms.CharField(widget=forms.PasswordInput(attrs={'column':5, 'rows':10}))
    Sgender=forms.ChoiceField(choices=g)
    Scourse=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    Scourse=forms.MultipleChoiceField(choices=c)




