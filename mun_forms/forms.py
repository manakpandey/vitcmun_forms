from django import forms


class ApplicationForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    phone = forms.IntegerField(widget=forms.NumberInput)
    dob = forms.DateField()
    institution = forms.CharField()
    mun_exp = forms.CharField()
    council_p1 = forms.CharField()
    council_p2 = forms.CharField()
    imp_p1 = forms.CharField(max_length=1500, widget=forms.Textarea)
    q1 = forms.CharField(widget=forms.Textarea, max_length=5000)
    q2 = forms.CharField(widget=forms.Textarea, max_length=5000)
    accommodation = forms.CharField()
