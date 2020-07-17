from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from .models import Staff, User
from django.contrib.auth.models import Group, Permission



def staff_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='primary')
		instance.groups.add(group)
		Staff.objects.create(
			user=instance,
			name=instance.email,
			)
post_save.connect(staff_profile, sender=Staff)

def secondary_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='secondary')
		instance.groups.add(group)
		Staff.objects.create(
			user=instance,
			name=instance.email,
			)
post_save.connect(secondary_profile, sender=Staff)

def techschool_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='techschool')
		instance.groups.add(group)
		Staff.objects.create(
			user=instance,
			name=instance.email,
			)
post_save.connect(techschool_profile, sender=Staff)

