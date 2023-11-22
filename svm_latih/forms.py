from django import forms

class InputForm(forms.Form):
    CHOICES = ( 
        (0, '--Pilih--'),
        (1, 'Tidak'),
        (2, 'Ya')
    )

    nama_pasien = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    umur_pasien = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    nyeri_dada = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    sulit_menelan = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    rasa_terbakar = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    regurgitasi = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    batuk_kronis = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    sakit_tenggorokan = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    peningkatan_airliur = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    gangguan_tidur = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    gangguan_pernapasan = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    perubahan_beratbadan = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    kelelahan = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    gangguan_pencernaan = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
