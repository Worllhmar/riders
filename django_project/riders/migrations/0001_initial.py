# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImageModel'
        db.create_table(u'riders_imagemodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'riders', ['ImageModel'])

        # Adding model 'Rider'
        db.create_table(u'riders_rider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('birth', self.gf('django.db.models.fields.DateField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ride', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'riders', ['Rider'])

        # Adding M2M table for field images on 'Rider'
        db.create_table(u'riders_rider_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('rider', models.ForeignKey(orm[u'riders.rider'], null=False)),
            ('imagemodel', models.ForeignKey(orm[u'riders.imagemodel'], null=False))
        ))
        db.create_unique(u'riders_rider_images', ['rider_id', 'imagemodel_id'])


    def backwards(self, orm):
        # Deleting model 'ImageModel'
        db.delete_table(u'riders_imagemodel')

        # Deleting model 'Rider'
        db.delete_table(u'riders_rider')

        # Removing M2M table for field images on 'Rider'
        db.delete_table('riders_rider_images')


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
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['riders']