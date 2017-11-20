from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Location(models.Model):
    address = models.CharField(max_length=200)
    building_name = models.CharField(max_length=30)
    room_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.room_name} {self.building_name}'


class Practice(models.Model):
    title = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.title} at {self.location} on {self.date}'


class Attendance(models.Model):
    RSVP_CHOICES = [
        ('y', 'Yes'),
        ('n', 'No'),
        ('m', 'Maybe'),
        ('u', 'Unknown'),
    ]
    rsvp = models.CharField(max_length=1, choices=RSVP_CHOICES)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.get_full_name()} rsvp'd {self.rsvp} for " \
               f"{self.practice.title} on {self.practice.date}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=18)
    DANCE_ROLES = [
        ('l', 'Lead'),
        ('f', 'Follow'),
        ('b', 'Both')
    ]
    lead_follow = models.CharField(max_length=1, choices=DANCE_ROLES)

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.phone} - ' \
               f'{self.lead_follow}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
