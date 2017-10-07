from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    prof_name = models.CharField('Professor Name', max_length=250)
    qualification = models.CharField('Qualification(such as Phd. )', max_length=250, blank=True)
    qualification_institute = models.CharField('Institution Qualified From (such as IIT Delhi )', max_length=250, blank=True)
    area_of_interest=models.CharField('Areas Of Interest (, separated)', max_length=1250)
    contact_info=models.CharField('Email id:', max_length=250)
    image_file = models.FileField(blank=True)


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_name=models.CharField('Event Name', max_length=250)
    about=models.CharField('About Event', max_length=250)
    event_image = models.FileField(blank=True)


class SubEvent(models.Model):
    id = models.AutoField(primary_key=True)
    sub_event_name = models.CharField('Sub Event Name', max_length=250)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    about_sub_event=models.CharField('About Event', max_length=250, blank=True)
    sub_event_image = models.FileField(blank=True)


class EventCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField('category Name', max_length=250)
    sub_event = models.ForeignKey(SubEvent, on_delete=models.CASCADE)
    winners= models.CharField('Winners name (, separated)', max_length=250)
    runner_ups=models.CharField('Winners name (, separated)', max_length=250)


class Organizers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('member Name', max_length=250)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class LibrarySection(models.Model):
    id = models.AutoField(primary_key=True)
    section = models.CharField('section Name', max_length=250)


class LibrarySectionCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField('category Name', max_length=250)
    section = models.ForeignKey(LibrarySection, on_delete=models.CASCADE)


class GuestLecturers:
    id = models.AutoField(primary_key=True)
    prof_name = models.CharField('Professor Name', max_length=250)
    qualification = models.CharField('Qualification(such as Phd. )', max_length=250, blank=True)
    qualification_institute = models.CharField('Institution Qualified From (such as IIT Delhi )', max_length=250,
                                               blank=True)
    area_of_interest = models.CharField('Areas Of Interest (, separated)', max_length=1250,blank=True)
    contact_info = models.CharField('Email id:', max_length=250)
    title = models.CharField('Title of Talk', max_length=500)
    abstract = models.CharField('Abstract', max_length=1250)
    image_file = models.FileField(blank=True)