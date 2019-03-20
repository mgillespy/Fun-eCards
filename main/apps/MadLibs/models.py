from __future__ import unicode_literals
from django.db import models

from django.core.exceptions import ValidationError


class CardManager(models.Manager):
    def card_validator(self, postData):
        errors = {}
        if not postData['sender']:
            errors["sender"] = "Please enter your name."
        if not postData['recipient']:
            errors["recipient"] = "Please enter the recipient's name."
        if not postData['event']:
            errors["event"] = "Please enter an event."
        if not postData['adj1']:
            errors["adj1"] = "Please enter all required words."
        elif not postData['adj2']:
            errors["adj2"] = "Please enter all required words.."
        elif not postData['noun1']:
            errors["noun1"] = "Please enter all required words."
        elif not postData['adj3']:
            errors["adj3"] = "Please enter all required words."
        elif not postData['noun2']:
            errors["noun2"] = "Please enter all required words."
        elif not postData['adj4']:
            errors["adj4"] = "Please enter all required words."
        elif not postData['adj5']:
            errors["adj5"] = "Please enter all required words."
        elif not postData['noun3']:
            errors["noun3"] = "Please enter all required words."
        elif not postData['adj6']:
            errors["adj6"] = "Please enter all required words."
        elif not postData['noun4']:
            errors["noun4"] = "Please enter all required words."
        elif not postData['noun5']:
            errors["noun5"] = "Please enter all required words."
        elif not postData['noun6']:
            errors["noun6"] = "Please enter all required words."
        elif not postData['noun7']:
            errors["noun7"] = "Please enter all required words."
        elif not postData['noun8']:
            errors["noun8"] = "Please enter all required words."
        elif not postData['adj7']:
            errors["adj7"] = "Please enter all required words."
        elif not postData['noun9']:
            errors["noun9"] = "Please enter all required words."
        print(errors)
        return errors


class Card(models.Model):
    sender = models.TextField(max_length=30, blank=True)
    recipient = models.TextField(max_length=30, blank=True)
    event = models.TextField(max_length=30, blank=True)
    noun1 = models.TextField(max_length=30, blank=True)
    noun2 = models.TextField(max_length=30, blank=True)
    noun3 = models.TextField(max_length=30, blank=True)
    noun4 = models.TextField(max_length=30, blank=True)
    noun5 = models.TextField(max_length=30, blank=True)
    noun6 = models.TextField(max_length=30, blank=True)
    noun7 = models.TextField(max_length=30, blank=True)
    noun8 = models.TextField(max_length=30, blank=True)
    noun9 = models.TextField(max_length=30, blank=True)
    adj1 = models.TextField(max_length=30, blank=True)
    adj2 = models.TextField(max_length=30, blank=True)
    adj3 = models.TextField(max_length=30, blank=True)
    adj4 = models.TextField(max_length=30, blank=True)
    adj5 = models.TextField(max_length=30, blank=True)
    adj6 = models.TextField(max_length=30, blank=True)
    adj7 = models.TextField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CardManager()

    def __repr__(self):
        return "Card.object.{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(self.sender, self.recipient, self.event, self.noun1, self.noun2, self.noun3, self.noun4, self.noun5, self.noun6, self.noun7, self.noun8, self.noun9, self.adj1, self.adj2, self.adj3, self.adj4, self.adj5, self.adj6, self.adj7)
