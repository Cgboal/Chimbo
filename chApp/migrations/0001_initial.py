# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'chApp_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userName', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('pHash', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('perms', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('fName', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('lName', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'chApp', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'chApp_user')


    models = {
        u'chApp.user': {
            'Meta': {'object_name': 'User'},
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fName': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lName': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pHash': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'perms': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'userName': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['chApp']