from django import forms
from placement.models import Company, Placement, JobDetails


class CompanyForm(forms.ModelForm):
    class Meta:     
        model = Company
        fields = ['company_name', 'company_logo', 'company_url']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'info-input'
            }),
            'company_url': forms.TextInput(attrs={
                'class': 'info-input'
            }),
            'company_logo': forms.FileInput(attrs={
                'class': 'info-input'
            }),
        }


class PlacementForm(forms.ModelForm):
    class Meta:
        model = Placement
        exclude = ['company']   # we will attach company manually
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'info-input'}),
            'domain': forms.TextInput(attrs={'class': 'info-input'}),
            'employment_type': forms.Select(attrs={'class': 'info-input'}),
            'work_mode': forms.Select(attrs={'class': 'info-input'}),
            'package': forms.TextInput(attrs={'class': 'info-input'}),
            'location': forms.TextInput(attrs={'class': 'info-input'}),
            'experience': forms.TextInput(attrs={'class': 'info-input'}),
            'vacancy_no': forms.NumberInput(attrs={'class': 'info-input'}),
            'min_gpa': forms.TextInput(attrs={'class': 'info-input'}),
            'passing_year': forms.TextInput(attrs={'class': 'info-input'}),
        }


class JobDetailsForm(forms.ModelForm):
    class Meta:
        model = JobDetails
        exclude = ['placement']
        widgets = {
            'job_description': forms.Textarea(attrs={
                'class': 'info-input',
                'rows': 4
            }),
            'responsibilities': forms.Textarea(attrs={
                'class': 'info-input',
                'rows': 4
            }),
            'required_skills': forms.Textarea(attrs={
                'class': 'info-input',
                'rows': 3
            }),
        }
