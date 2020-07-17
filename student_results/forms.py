from django.forms import ModelForm
from django import forms, VERSION
from .models import User, Post, Profile, Comment, Friend, Staff, Std1, Std2, Std3, Std4, Std5, Std6, Std7, FormOne, FormTwo, FormThree, FormFour, FormOneTech, FormTwoTech, FormThreeTech, FormFourTech, EGM5, PCM5, PCB5, CBG5, PGM5, ECA5, HGE5, HGK5, HGL5, HKL5, EGM6, PCM6, PCB6, CBG6, PGM6, ECA6, HGE6, HGK6, HGL6, HKL6
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate    
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model



User = get_user_model()

# Create ModelForm based on the Group model.
class UserEditForm(forms.ModelForm):
    class Meta:
      model = User
      fields = ['email', 'username', 'first_name', 'last_name',]

class ProfileEditForm(forms.ModelForm):
    class Meta:
      model = Profile
      exclude = ['user',]


class PostForm(forms.ModelForm):
    class Meta:
      model = Post
      fields = "__all__"


class CommentForm(forms.ModelForm):
    content=forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Toa maoni yako ...', 'rows':'2', 'cols':'50'}))
    class Meta:
      model = Comment
      fields = ['content',]

class FriendForm(forms.ModelForm):
    class Meta:
      model = Friend
      fields = "__all__"


class UserForm(UserCreationForm):
    class Meta:
      model = User
      fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']

class SecondaryUserForm(UserCreationForm):
    class Meta:
      model = User
      fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']

class TechschoolUserForm(UserCreationForm):
    class Meta:
      model = User
      fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']

class CreateUserForm(UserCreationForm):
    class Meta:
      model = User
      fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']



class staffform(forms.ModelForm):
    class Meta:
      model = Staff
      fields = "__all__"

class Std3Form(forms.ModelForm):
    class Meta:
      model = Std3
      fields = ['user', 'candidate_NO', 'full_name', 'gender', 'grade', 'kiswahili', 'mathematics',
                 'social_studies', 'civic_and_moral', 'science_and_technology', 'english', 'total', 
                 'average', 'position', 'number_of_pupils', 'ranking', 'discriptions']
      labels = {
               "social_studies":"S.Studies",
               "civic_and_moral":"C.Moral",
               "science_and_technology":"S.Technology",
               "number_of_pupils":"No.Pupils"

               }
def __init__(self, *args, **kwargs):
      from django.forms.widgets import HiddenInput
      hide_condition = kwargs.pop('hide_condition', None)
      super(Std3Form, self).__init__(*args, **kwargs)
      if hide_condition:
          self.fields['user'].widget = HiddenInput()

      super(PostForm, self).__init__(*args, **kwargs)
      if hide_condition:
          self.fields['user'].widget = HiddenInput()
          
      super(ProfileEditForm, self).__init__(*args, **kwargs)
      if hide_condition:
          self.fields['user'].widget = HiddenInput()

class sarisfrm1tform(forms.ModelForm):
    class Meta:
      model = FormOneTech
      fields = ['candidate_NO']

class sarisfrm2tform(forms.ModelForm):
    class Meta:
      model = FormTwoTech
      fields = ['candidate_NO']

class sarisfrm3tform(forms.ModelForm):
    class Meta:
      model = FormThreeTech
      fields = ['candidate_NO']

class sarisfrm4tform(forms.ModelForm):
    class Meta:
      model = FormFourTech
      fields = ['candidate_NO']


class sarisfrm1form(forms.ModelForm):
    class Meta:
      model = FormOne
      fields = ['candidate_NO']

class sarisfrm2form(forms.ModelForm):
    class Meta:
      model = FormTwo
      fields = ['candidate_NO']

class sarisfrm3form(forms.ModelForm):
    class Meta:
      model = FormThree
      fields = ['candidate_NO']

class sarisfrm4form(forms.ModelForm):
    class Meta:
      model = FormFour
      fields = ['candidate_NO']

class sarisstd1form(forms.ModelForm):
    class Meta:
      model = Std1
      fields = ['candidate_NO']

class sarisstd2form(forms.ModelForm):
    class Meta:
      model = Std2
      fields = ['candidate_NO']

class sarisstd3form(forms.ModelForm):
    class Meta:
      model = Std3
      fields = ['candidate_NO']

class sarisstd4form(forms.ModelForm):
    class Meta:
      model = Std4
      fields = ['candidate_NO']

class sarisstd5form(forms.ModelForm):
    class Meta:
      model = Std5
      fields = ['candidate_NO']

class sarisstd6form(forms.ModelForm):
    class Meta:
      model = Std6
      fields = ['candidate_NO']

class sarisstd7form(forms.ModelForm):
    class Meta:
      model = Std7
      fields = ['candidate_NO']

class accform(forms.ModelForm):
    class Meta:
      model = User
      fields = ['email']


class Std1form(forms.ModelForm):
  class Meta:
    model = Std1
    fields = ['user', 'candidate_NO', 'full_name', 'gender', 'grade', 'kusoma', 'arithmetic',
              'kuandika', 'developing_arts', 'health_care_and_environment', 'reading', 'writing', 
                'total', 'average', 'position', 'number_of_pupils', 'ranking', 'discriptions']
    labels = {
              "health_care_and_environment":"H/Care",
              "developing_arts":"D.Arts",
              "number_of_pupils":"No.Pupils"
               }
        
class Std2form(forms.ModelForm):
  class Meta:
    model = Std2
    fields = ['user', 'candidate_NO', 'full_name', 'gender', 'grade', 'kusoma', 'arithmetic',
              'kuandika', 'developing_arts', 'health_care_and_environment', 'reading', 'writing', 
                'total', 'average', 'position', 'number_of_pupils', 'ranking', 'discriptions']
    labels = {
              "health_care_and_environment":"H/Care",
              "developing_arts":"D.Arts",
              "number_of_pupils":"No.Pupils"

               }

class Std4form(forms.ModelForm):
  class Meta:
    model = Std4
    fields = ['user', 'candidate_NO', 'full_name', 'gender', 'grade', 'kiswahili', 'mathematics',
                'social_studies', 'civic_and_moral', 'science_and_technology', 'english', 'total', 
                'average', 'position', 'number_of_pupils', 'ranking', 'discriptions']
    labels = {
              "social_studies":"S.Studies",
              "civic_and_moral":"C.Moral",
              "science_and_technology":"S.Technology",
              "number_of_pupils":"No.Pupils"

               }

class Std5form(forms.ModelForm):
  class Meta:
    model = Std5
    fields = ['user', 'candidate_NO', 'full_name', 'gender', 'grade', 'kiswahili', 'mathematics',
                'social_studies', 'civic_and_moral', 'science_and_technology', 'english', 'total', 
                'average', 'position', 'number_of_pupils', 'ranking', 'discriptions']
    labels = {
              "social_studies":"S.Studies",
              "civic_and_moral":"C.Moral",
              "science_and_technology":"S.Technology",
              "number_of_pupils":"No.Pupils"

               }

class Std6form(forms.ModelForm):
  class Meta:
    model = Std6
    fields = ['user', 'candidate_NO', 'full_name', 'gender', 'grade', 'kiswahili', 'mathematics',
                'social_studies', 'civic_and_moral', 'science_and_technology', 'english', 'total', 
                'average', 'position', 'number_of_pupils', 'ranking', 'discriptions']
    labels = {
              "social_studies":"S.Studies",
              "civic_and_moral":"C.Moral",
              "science_and_technology":"S.Technology",
              "number_of_pupils":"No.Pupils"

               }


class Std7form(forms.ModelForm):
  class Meta:
    model = Std7
    fields = ['user', 'candidate_NO', 'full_name', 'gender', 'grade', 'kiswahili', 'mathematics',
                'social_studies', 'civic_and_moral', 'science_and_technology', 'english', 'total', 
                'average', 'position', 'number_of_pupils', 'ranking', 'discriptions']
    labels = {
              "social_studies":"S.Studies",
              "civic_and_moral":"C.Moral",
              "science_and_technology":"S.Technology",
              "number_of_pupils":"No.Pupils"

               }

class FormOneform(forms.ModelForm):
  class Meta:
    model = FormOne
    fields ="__all__"
   

class FormTwoform(forms.ModelForm):
  class Meta:
    model = FormTwo
    fields = "__all__"

class FormThreeform(forms.ModelForm):
  class Meta:
    model = FormThree
    fields = "__all__"

class FormFourform(forms.ModelForm):
  class Meta:
    model = FormFour
    fields = "__all__"

class FormOneTechform(forms.ModelForm):
  class Meta:
    model = FormOneTech
    fields = "__all__"

class FormTwoTechform(forms.ModelForm):
  class Meta:
    model = FormTwoTech
    fields = "__all__"

class FormThreeTechform(forms.ModelForm):
  class Meta:
    model = FormThreeTech
    fields = "__all__"

class FormFourTechform(forms.ModelForm):
  class Meta:
    model = FormFourTech
    fields = "__all__"


class EGM5form(forms.ModelForm):
  class Meta:
    model = EGM5
    fields = "__all__"

class PCB5form(forms.ModelForm):
  class Meta:
    model = PCB5
    fields = "__all__"

class PCM5form(forms.ModelForm):
  class Meta:
    model = PCM5
    fields = "__all__"

class CBG5form(forms.ModelForm):
  class Meta:
    model = CBG5
    fields = "__all__"

class PGM5form(forms.ModelForm):
  class Meta:
    model = PGM5
    fields = "__all__"


class ECA5form(forms.ModelForm):
  class Meta:
    model = ECA5
    fields = "__all__"

class HGE5form(forms.ModelForm):
  class Meta:
    model = HGE5
    fields = "__all__"

class HGK5form(forms.ModelForm):
  class Meta:
    model = HGK5
    fields = "__all__"

class HGL5form(forms.ModelForm):
  class Meta:
    model = HGL5
    fields = "__all__"

class HKL5form(forms.ModelForm):
  class Meta:
    model = HKL5
    fields = "__all__"



class EGM6form(forms.ModelForm):
  class Meta:
    model = EGM6
    fields = "__all__"

class PCB6form(forms.ModelForm):
  class Meta:
    model = PCB6
    fields = "__all__"

class PCM6form(forms.ModelForm):
  class Meta:
    model = PCM6
    fields = "__all__"

class CBG6form(forms.ModelForm):
  class Meta:
    model = CBG6
    fields = "__all__"

class PGM6form(forms.ModelForm):
  class Meta:
    model = PGM6
    fields = "__all__"


class ECA6form(forms.ModelForm):
  class Meta:
    model = ECA6
    fields = "__all__"

class HGE6form(forms.ModelForm):
  class Meta:
    model = HGE6
    fields = "__all__"

class HGK6form(forms.ModelForm):
  class Meta:
    model = HGK6
    fields = "__all__"

class HGL6form(forms.ModelForm):
  class Meta:
    model = HGL6
    fields = "__all__"

class HKL6form(forms.ModelForm):
  class Meta:
    model = HKL6
    fields = "__all__"


