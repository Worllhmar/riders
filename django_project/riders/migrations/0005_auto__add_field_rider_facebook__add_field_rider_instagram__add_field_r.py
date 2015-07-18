# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Rider.facebook'
        db.add_column(u'riders_rider', 'facebook',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Rider.instagram'
        db.add_column(u'riders_rider', 'instagram',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Rider.twitter'
        db.add_column(u'riders_rider', 'twitter',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Rider.facebook'
        db.delete_column(u'riders_rider', 'facebook')

        # Deleting field 'Rider.instagram'
        db.delete_column(u'riders_rider', 'instagram')

        # Deleting field 'Rider.twitter'
        db.delete_column(u'riders_rider', 'twitter')


    models = {
        u'riders.imagemodel': {
            'Meta': {'object_name': 'ImageModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'riders.rider': {
            'Meta': {'object_name': 'Rider'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birth': ('django.db.models.fields.DateField', [], {}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['riders.ImageModel']", 'symmetrical': 'False', 'blank': 'True'}),
            'instagram': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ride': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['riders']