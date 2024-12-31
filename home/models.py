# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Articles(models.Model):

    #__Articles_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    family = models.ForeignKey(family, on_delete=models.CASCADE)
    sub-family = models.ForeignKey(sub-family, on_delete=models.CASCADE)

    #__Articles_FIELDS__END

    class Meta:
        verbose_name        = _("Articles")
        verbose_name_plural = _("Articles")


class Family(models.Model):

    #__Family_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)

    #__Family_FIELDS__END

    class Meta:
        verbose_name        = _("Family")
        verbose_name_plural = _("Family")


class Sub-Family(models.Model):

    #__Sub-Family_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)

    #__Sub-Family_FIELDS__END

    class Meta:
        verbose_name        = _("Sub-Family")
        verbose_name_plural = _("Sub-Family")



#__MODELS__END
