from email.policy import default
from django import forms
from .models import Fabrics, Makers, Fabnames, Partycodes

makers= Makers.objects.all()
fabnames= Fabnames.objects.all()
partycodes= Partycodes.objects.all()
ml=[]
fl=[]
pcl=[]
for m in makers:
    b=(m.maker,m.maker)
    ml.append(b)
for m in fabnames:
    b=(m.fabname,m.fabname)
    fl.append(b)
for m in partycodes:
    b=(m.partycode,m.partycode)
    pcl.append(b)

# partycodelist=[
#     ('green','GREEN'),
#     ('blue', 'BLUE'),
#     ('red','RED'),
#     ('orange','ORANGE'),
#     ('black','BLACK'),
# ]

# fabriclist=[
#     ('lycra','Lycra'),
#     ('cotton','Cotton'),
#     ('rib','Rib'),
# ]

# makerlist=[
#     ('adil','Adil'),
#     ('baba','Baba'),
#     ('feroz','Feroz'),
#     ('guddu','Guddu'),
# ]

class AddFabrics(forms.ModelForm):
    
    partycode = forms.ChoiceField(choices=pcl, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    fabric = forms.ChoiceField(choices=fl, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    maker = forms.ChoiceField(choices=ml, widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    
    class Meta:
        model = Fabrics
        fields = ['partycode','color','meter','fabric','maker']
        labels = {'partycode':'Party_Code','color':'Color','meter':'Meter','fabric':'Fabric','maker':'Maker'}
        widgets={
            # 'partycode': forms.Select(attrs={'class':'form-select'}),
            'color': forms.NumberInput(attrs={'class':'form-control'}),
            'meter': forms.NumberInput(attrs={'class':'form-control'}),
            # 'fabric': forms.Select(attrs={'class':'form-select'})
            # 'maker': forms.Select(attrs={'class':'form-select'})
        }



# maker edit form
# class editfab(forms.forms.ModelForm):