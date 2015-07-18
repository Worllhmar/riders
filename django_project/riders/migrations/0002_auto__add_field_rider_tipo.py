# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Rider.tipo'
        db.add_column(u'riders_rider', 'tipo',
                      self.gf('django.db.models.fields.CharField')(default='fmx', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Rider.tipo'
        db.delete_column(u'riders_rider', 'tipo')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['riders.ImageModel']", 'symmetrical': 'False', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ride': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['riders']