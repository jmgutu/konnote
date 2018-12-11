# forms.CharField(widget = forms.HiddenInput(), required = False)

from django import forms
from django.contrib.auth.models import User
from staff.models import Staff
from departments.models import Department
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.urlresolvers import reverse
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, MultiField, Div


class StaffRegistrationForm(forms.Form):
    '''

    Check this tutorial for more >> https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
    post = forms.CharField(widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write a post...'
            }
    ))

     forms.TextInput(attrs={'required': True})

     forms.TextInput(attrs={'size': 10, 'title': 'Your name',})



     Rendering forms manually seems the best option (More Control) >> https://docs.djangoproject.com/en/1.11/topics/forms/

    Core Field Arguments
    --------------------
    initial='Your name'
    required=True
    label='Your name'
    help_text='100 characters max.'
    error_messages={'required': 'Please enter your name'}
    diabled = True
    Field.has_changed() > Can be used to record which values have been altered by the user

    FieldTypes
    ----------
    BooleanField
    CharField
    ChoiceField
    TypedChoiceField
    DateField
        ['%Y-%m-%d',      # '2006-10-25'
         '%m/%d/%Y',      # '10/25/2006'
         '%m/%d/%y']      # '10/25/06'
     DateTimeField
     DecimalField > max_value, min_value, max_digits, decimal_places
     DurationField
     EmailField
     FileField
     FilePAthField
     FloatField
     ImageField
     Integer
     GenericIPAddressField
     MultipleChoiceField
     TypedMultipleChoiceField
     NullBooleanField
     RegexField
     SlugField
     URLField
     TimeField

     widget=forms.Textarea
     birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
     favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,)
    CHOICES = (('1', 'First',), ('2', 'Second',))
    ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    choice_field.widget.choices = ()
    choice_field.choices = (('1', 'First and only',),)

    Styling widget instances
    ------------------------
    CommentForm(auto_id=False)
    CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))

    Styling widget Classes
    ----------------------
    forms.TextInput(attrs={'size': 10, 'title': 'Your name',})
    TextInput
    NumberInput
    EmailInput
    URLInput
    PasswordInput
    HiddenInput
    DateInput
    DateTimeInput
    TimeInput
    Textarea
    CheckboxInput
    Select
    NullBooleanSelect
    SelectMultiple
    RadioSelect
    CheckboxSelectMultiple
    FileInput
    ClearableFileInput
    MultipleHiddenInput
    SelectDateWidget

     from django.shortcuts import render
    from django.http import HttpResponseRedirect

    from .forms import NameForm

    def get_name(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = NameForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = NameForm()

        return render(request, 'name.html', {'form': form})


                form = ProjectForm()
        try:
            form.fields["budget"].queryset = Budget.objects.filter(id=budget_id)
        except ObjectDoesNotExist:
            form.fields["budget"].queryset = Budget.all()
        form.fields["created_by"].initial = User.objects.get(pk=request.session['id'])
        form.fields["created_by"].widget = forms.HiddenInput()

    '''

    first_name = forms.CharField(label='First Name', max_length=100, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 error_messages={'required': 'Your First Name is required'})
    last_name = forms.CharField(label='Last Name', max_length=100, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', max_length=20, required=True, help_text='100 characters max.',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Official Email', max_length=50, required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    no = forms.CharField(label='AIR Staff Number', max_length=100, required=True,
                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.CharField(label='Position', max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    role = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control col-6'}), label='Role', max_length=250,
                           required=False)
    department = forms.ModelChoiceField(queryset=Department.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    background = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Bio', max_length=25,
                                 required=False)

    def __init__(self, *args, **kwargs):
        super(StaffRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-staff-registration-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('createstaff')
        self.helper.add_input(Submit('submit', 'Submit'))


class EditStaffForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 error_messages={'required': 'Your First Name is required'})
    last_name = forms.CharField(label='Last Name', max_length=100, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', max_length=20, required=True, help_text='100 characters max.',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Official Email', max_length=50, required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    no = forms.CharField(label='AIR Staff Number', max_length=100, required=True,
                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.CharField(label='Position', max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    role = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control col-6'}), label='Role', max_length=250,
                           required=False)
    department = forms.ModelChoiceField(queryset=Department.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    background = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Bio', max_length=25,
                                 required=False)
    staffid = forms.DecimalField(widget=forms.HiddenInput(attrs={'class': 'form-control'}), label='Description',
                                 help_text='A brief description of the department', required=True,
                                 error_messages={'required': 'The Description is required'})

    def __init__(self, *args, **kwargs):
        super(EditStaffForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-staff-edit-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('updatestaff')
        self.helper.add_input(Submit('submit', 'Submit'))



