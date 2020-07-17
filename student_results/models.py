from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import Q
import uuid
from django.conf import settings
 


class MyUserManager(UserManager):
	def create_user(self, email, username, first_name, last_name, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			first_name=first_name,
			last_name=last_name,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, first_name, last_name, password=None):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
			first_name=first_name,
			last_name=last_name,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class User(AbstractUser):
	id 						= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	first_name 				= models.CharField(max_length=100, blank=True)
	last_name 				= models.CharField(max_length=100, blank=True)	
	is_admin				   = models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				   = models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

	objects = MyUserManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True


class Profile(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', null=True, blank=True, on_delete=models.SET_NULL)
   profile_pic = models.ImageField(default="icon.png", null=True, blank=True)


class Post(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)   
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
   post = models.TextField(max_length=5000, null=True)
   likes = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', null=True, blank=True, on_delete=models.CASCADE)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)



class Comment(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)  
   post = models.ForeignKey(Post, blank=True, on_delete=models.CASCADE)
   content = models.TextField(max_length=200, null=True)  
   created = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
      return '{}-{}' .format(self.post, str(self.user.username))


   
  
class Friend(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)   
   user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner', null=True, on_delete=models.SET_NULL)
   friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

   @classmethod
   def make_friend(cls, user, new_friend):
      friend, created = cls.objects.get_or_create(user=user)
      friend.friends.add(new_friend)

   @classmethod
   def lose_friend(cls, user, new_friend):
      friend, created = cls.objects.get_or_create(user=user)
      friend.friends.remove(new_friend)

   def __str__(self):
      return str(self.user)


class Staff(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   name = models.CharField(max_length=200, null=True)
   email = models.CharField(max_length=200, null=True)
   phone = models.CharField(max_length=200, null=True)
   
   def __str__(self):
       return self.name 

class Std1(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)      
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)   
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True, default=3)
   kuandika = models.CharField(max_length=3, blank=True)
   arithmetic = models.CharField(max_length=3, blank=True)
   reading = models.CharField(max_length=3, blank=True)
   kusoma = models.CharField(max_length=3, blank=True)
   health_care_and_environment = models.CharField(max_length=3, blank=True)
   writing = models.CharField(max_length=3, blank=True)
   developing_arts = models.CharField(max_length=3, blank=True)
   total = models.CharField(max_length=3, blank=True)
   average = models.CharField(max_length=3, blank=True)
   ranking = models.CharField(max_length=5, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_pupils = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)

   def __str__(self):
       return self.full_name 


class Std2(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)      
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)   
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True, default=3)
   kuandika = models.CharField(max_length=3, blank=True)
   arithmetic = models.CharField(max_length=3, blank=True)
   reading = models.CharField(max_length=3, blank=True)
   kusoma = models.CharField(max_length=3, blank=True)
   health_care_and_environment = models.CharField(max_length=3, blank=True)
   writing = models.CharField(max_length=3, blank=True)
   developing_arts = models.CharField(max_length=3, blank=True)
   total = models.CharField(max_length=3, blank=True)
   average = models.CharField(max_length=3, blank=True)
   ranking = models.CharField(max_length=5, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_pupils = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)

   def __str__(self):
       return self.full_name 

class Std3(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)      
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)   
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True, default=3)
   kiswahili = models.CharField(max_length=3, blank=True)
   mathematics = models.CharField(max_length=3, blank=True)
   social_studies = models.CharField(max_length=3, blank=True)
   civic_and_moral = models.CharField(max_length=3, blank=True)
   science_and_technology = models.CharField(max_length=3, blank=True)
   english = models.CharField(max_length=3, blank=True)
   vocational_skills = models.CharField(max_length=3, blank=True)
   total = models.CharField(max_length=3, blank=True)
   average = models.CharField(max_length=3, blank=True)
   ranking = models.CharField(max_length=5, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_pupils = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)

   def __str__(self):
       return self.full_name 

class Std4(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)      
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)  
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True, default=4)
   kiswahili = models.CharField(max_length=3, blank=True)
   mathematics = models.CharField(max_length=3, blank=True)
   social_studies = models.CharField(max_length=3, blank=True)
   civic_and_moral = models.CharField(max_length=3, blank=True)
   science_and_technology = models.CharField(max_length=3, blank=True)
   english = models.CharField(max_length=3, blank=True)
   vocational_skills = models.CharField(max_length=3, blank=True)
   total = models.CharField(max_length=3, blank=True)
   average = models.CharField(max_length=3, blank=True)
   ranking = models.CharField(max_length=5, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_pupils = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)

   def __str__(self):
       return self.full_name 

class Std5(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)      
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)   
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True, default=5)
   kiswahili = models.CharField(max_length=3, blank=True)
   mathematics = models.CharField(max_length=3, blank=True)
   social_studies = models.CharField(max_length=3, blank=True)
   civic_and_moral = models.CharField(max_length=3, blank=True)
   science_and_technology = models.CharField(max_length=3, blank=True)
   english = models.CharField(max_length=3, blank=True)
   vocational_skills = models.CharField(max_length=3, blank=True)
   total = models.CharField(max_length=3, blank=True)
   average = models.CharField(max_length=3, blank=True)
   ranking = models.CharField(max_length=5, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_pupils = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)

   def __str__(self):
       return self.full_name 

class Std6(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)      
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)   
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True, default=6)
   kiswahili = models.CharField(max_length=3, blank=True)
   mathematics = models.CharField(max_length=3, blank=True)
   social_studies = models.CharField(max_length=3, blank=True)
   civic_and_moral = models.CharField(max_length=3, blank=True)
   science_and_technology = models.CharField(max_length=3, blank=True)
   english = models.CharField(max_length=3, blank=True)
   vocational_skills = models.CharField(max_length=3, blank=True)
   total = models.CharField(max_length=3, blank=True)
   average = models.CharField(max_length=3, blank=True)
   ranking = models.CharField(max_length=5, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_pupils = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)

   def __str__(self):
       return self.full_name 

class Std7(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)      
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)   
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True, default=7)
   kiswahili = models.CharField(max_length=3, blank=True)
   mathematics = models.CharField(max_length=3, blank=True)
   social_studies = models.CharField(max_length=3, blank=True)
   civic_and_moral = models.CharField(max_length=3, blank=True)
   science_and_technology = models.CharField(max_length=3, blank=True)
   english = models.CharField(max_length=3, blank=True)
   vocational_skills = models.CharField(max_length=3, blank=True)
   total = models.CharField(max_length=3, blank=True)
   average = models.CharField(max_length=3, blank=True)
   ranking = models.CharField(max_length=5, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_pupils = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)

   def __str__(self):
       return self.full_name 

    

class FormOneTech(models.Model):
   DISCRIPTIONS = (
               ('Passed', 'Passed'),
               ('Failed', 'Failed'),
               )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   form = models.CharField(max_length=10, blank=True)
   mathematics = models.CharField(max_length=3, blank=True)
   english_languge = models.CharField(max_length=3, blank=True)
   biology = models.CharField(max_length=3, blank=True)
   civics = models.CharField(max_length=3, blank=True)
   kiswahili = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)
   chemistry = models.CharField(max_length=3, blank=True)
   bookkeeping = models.CharField(max_length=3, blank=True)
   commerce = models.CharField(max_length=3, blank=True)
   additional_mathematics = models.CharField(max_length=3, blank=True)
   engineering_science = models.CharField(max_length=3, blank=True)
   welding = models.CharField(max_length=3, blank=True)
   civil_engineering = models.CharField(max_length=3, blank=True)
   electrical_engineering = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name 

class FormTwoTech(models.Model):
   DISCRIPTIONS = (
               ('Passed', 'Passed'),
               ('Failed', 'Failed'),
               )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   form = models.CharField(max_length=10, blank=True)
   mathematics = models.CharField(max_length=3, blank=True)
   english_languge = models.CharField(max_length=3, blank=True)
   biology = models.CharField(max_length=3, blank=True)
   civics = models.CharField(max_length=3, blank=True)
   kiswahili = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)
   chemistry = models.CharField(max_length=3, blank=True)
   bookkeeping = models.CharField(max_length=3, blank=True)
   commerce = models.CharField(max_length=3, blank=True)
   additional_mathematics = models.CharField(max_length=3, blank=True)
   engineering_science = models.CharField(max_length=3, blank=True)
   welding = models.CharField(max_length=3, blank=True)
   civil_engineering = models.CharField(max_length=3, blank=True)
   electrical_engineering = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name 

class FormThreeTech(models.Model):
   DISCRIPTIONS = (
               ('Passed', 'Passed'),
               ('Failed', 'Failed'),
               )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   form = models.CharField(max_length=10, blank=True)
   mathematics = models.CharField(max_length=3, blank=True)
   english_languge = models.CharField(max_length=3, blank=True)
   biology = models.CharField(max_length=3, blank=True)
   civics = models.CharField(max_length=3, blank=True)
   kiswahili = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)
   chemistry = models.CharField(max_length=3, blank=True)
   bookkeeping = models.CharField(max_length=3, blank=True)
   commerce = models.CharField(max_length=3, blank=True)
   additional_mathematics = models.CharField(max_length=3, blank=True)
   engineering_science = models.CharField(max_length=3, blank=True)
   welding = models.CharField(max_length=3, blank=True)
   civil_engineering = models.CharField(max_length=3, blank=True)
   electrical_engineering = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name 

class FormFourTech(models.Model):
   DISCRIPTIONS = (
               ('Passed', 'Passed'),
               ('Failed', 'Failed'),
               )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   form = models.CharField(max_length=10, blank=True)
   mathematics = models.CharField(max_length=3, blank=True)
   english_languge = models.CharField(max_length=3, blank=True)
   biology = models.CharField(max_length=3, blank=True)
   civics = models.CharField(max_length=3, blank=True)
   kiswahili = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)
   chemistry = models.CharField(max_length=3, blank=True)
   bookkeeping = models.CharField(max_length=3, blank=True)
   commerce = models.CharField(max_length=3, blank=True)
   additional_mathematics = models.CharField(max_length=3, blank=True)
   engineering_science = models.CharField(max_length=3, blank=True)
   welding = models.CharField(max_length=3, blank=True)
   civil_engineering = models.CharField(max_length=3, blank=True)
   electrical_engineering = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name 

class FormOne(models.Model):
   DISCRIPTIONS = (
               ('Passed', 'Passed'),
               ('Failed', 'Failed'),
               )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   form = models.CharField(max_length=10, blank=True)
   mathematics = models.CharField(max_length=3, blank=True)
   english_languge = models.CharField(max_length=3, blank=True)
   biology = models.CharField(max_length=3, blank=True)
   civics = models.CharField(max_length=3, blank=True)
   kiswahili = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)  
   history = models.CharField(max_length=3, blank=True)
   chemistry = models.CharField(max_length=3, blank=True)  
   physics = models.CharField(max_length=3, blank=True)
   bookkeeping = models.CharField(max_length=3, blank=True)
   commerce = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name 

class FormTwo(models.Model):
   DISCRIPTIONS = (
               ('Passed', 'Passed'),
               ('Failed', 'Failed'),
               )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   form = models.CharField(max_length=10, blank=True)
   mathematics = models.CharField(max_length=3, blank=True)
   english_languge = models.CharField(max_length=3, blank=True)
   biology = models.CharField(max_length=3, blank=True)
   civics = models.CharField(max_length=3, blank=True)
   kiswahili = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)  
   history = models.CharField(max_length=3, blank=True)
   chemistry = models.CharField(max_length=3, blank=True)  
   physics = models.CharField(max_length=3, blank=True)
   bookkeeping = models.CharField(max_length=3, blank=True)
   commerce = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name 

class FormThree(models.Model):
   DISCRIPTIONS = (
               ('Passed', 'Passed'),
               ('Failed', 'Failed'),
               )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   form = models.CharField(max_length=10, blank=True)
   mathematics = models.CharField(max_length=3, blank=True)
   english_languge = models.CharField(max_length=3, blank=True)
   biology = models.CharField(max_length=3, blank=True)
   civics = models.CharField(max_length=3, blank=True)
   kiswahili = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)  
   history = models.CharField(max_length=3, blank=True)
   chemistry = models.CharField(max_length=3, blank=True)  
   physics = models.CharField(max_length=3, blank=True)
   bookkeeping = models.CharField(max_length=3, blank=True)
   commerce = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name 

class FormFour(models.Model):
   DISCRIPTIONS = (
               ('Passed', 'Passed'),
               ('Failed', 'Failed'),
               )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   form = models.CharField(max_length=10, blank=True)
   mathematics = models.CharField(max_length=3, blank=True)
   english_languge = models.CharField(max_length=3, blank=True)
   biology = models.CharField(max_length=3, blank=True)
   civics = models.CharField(max_length=3, blank=True)
   kiswahili = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)  
   history = models.CharField(max_length=3, blank=True)
   chemistry = models.CharField(max_length=3, blank=True)  
   physics = models.CharField(max_length=3, blank=True)
   bookkeeping = models.CharField(max_length=3, blank=True)
   commerce = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name 

   
class EGM5(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   economics = models.CharField(max_length=3, blank=True)  
   geography = models.CharField(max_length=3, blank=True)
   advanced_mathematics = models.CharField(max_length=3, blank=True)   
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class PGM5(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   physics = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)
   advanced_mathematics = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name
 
class PCM5(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   physics = models.CharField(max_length=3, blank=True)
   chemistry = models.CharField(max_length=3, blank=True)
   advanced_mathematics = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class CBG5(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   chemistry = models.CharField(max_length=3, blank=True)
   biology = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)
   bam = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class PCB5(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   physics = models.CharField(max_length=3, blank=True)
   chemistry = models.CharField(max_length=3, blank=True)
   biology = models.CharField(max_length=3, blank=True)
   bam = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class ECA5(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   economics = models.CharField(max_length=3, blank=True)
   commerce = models.CharField(max_length=3, blank=True)
   accounts = models.CharField(max_length=3, blank=True)
   bam = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class HGE5(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   history = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)
   economics = models.CharField(max_length=3, blank=True)
   bam = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class HGK5(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   history = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)
   kiswahili = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class HGL5(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   history = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)
   language = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class HKL5(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   history = models.CharField(max_length=3, blank=True)
   kiswahili = models.CharField(max_length=3, blank=True)
   language = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name




class EGM6(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   economics = models.CharField(max_length=3, blank=True)  
   geography = models.CharField(max_length=3, blank=True)
   advanced_mathematics = models.CharField(max_length=3, blank=True)   
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class PGM6(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   physics = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)
   advanced_mathematics = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name
 
class PCM6(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   physics = models.CharField(max_length=3, blank=True)
   chemistry = models.CharField(max_length=3, blank=True)
   advanced_mathematics = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class CBG6(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   chemistry = models.CharField(max_length=3, blank=True)
   biology = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class PCB6(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   physics = models.CharField(max_length=3, blank=True)
   chemistry = models.CharField(max_length=3, blank=True)
   biology = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class ECA6(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   economics = models.CharField(max_length=3, blank=True)
   commerce = models.CharField(max_length=3, blank=True)
   accounts = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class HGE6(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   history = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)
   economics = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class HGK6(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   history = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)
   kiswahili = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class HGL6(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   history = models.CharField(max_length=3, blank=True)
   geography = models.CharField(max_length=3, blank=True)
   language = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name

class HKL6(models.Model):
   DISCRIPTIONS = (
                  ('Passed', 'Passed'),
                  ('Failed', 'Failed'),
                  )

   GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )  
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
   candidate_NO = models.CharField(max_length=100, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   full_name = models.CharField(max_length=100, blank=True)
   gender = models.CharField(max_length=10, blank=True, choices=GENDER)
   grade = models.CharField(max_length=10, blank=True)
   history = models.CharField(max_length=3, blank=True)
   kiswahili = models.CharField(max_length=3, blank=True)
   language = models.CharField(max_length=3, blank=True)
   general_studies = models.CharField(max_length=3, blank=True)
   division = models.CharField(max_length=10, blank=True)
   points = models.CharField(max_length=3, blank=True)
   position = models.CharField(max_length=3, blank=True)
   number_of_students = models.CharField(max_length=3, blank=True)
   discriptions = models.CharField(max_length=500, blank=True, choices=DISCRIPTIONS)
   def __str__(self):
       return self.full_name
