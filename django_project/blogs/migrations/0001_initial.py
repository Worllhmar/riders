# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImageModel'
        db.create_table(u'blogs_imagemodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'blogs', ['ImageModel'])

        # Adding model 'Blog'
        db.create_table(u'blogs_blog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('intro', self.gf('tinymce.models.HTMLField')()),
            ('content', self.gf('tinymce.models.HTMLField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'blogs', ['Blog'])

        # Adding M2M table for field images on 'Blog'
        db.create_table(u'blogs_blog_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blog', models.ForeignKey(orm[u'blogs.blog'], null=False)),
            ('imagemodel', models.ForeignKey(orm[u'blogs.imagemodel'], null=False))
        ))
        db.create_unique(u'blogs_blog_images', ['blog_id', 'imagemodel_id'])


    def backwards(self, orm):
        # Deleting model 'ImageModel'
        db.delete_table(u'blogs_imagemodel')

        # Deleting model 'Blog'
        db.delete_table(u'blogs_blog')

        # Removing M2M table for field images on 'Blog'
        db.delete_table('blogs_blog_images')


    models = {
        u'blogs.blog': {
            'Meta': {'object_name': 'Blog'},
            'content': ('tinymce.models.HTMLField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['blogs.ImageModel']", 'null': 'True', 'blank': 'True'}),
            'intro': ('tinymce.models.HTMLField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'blogs.imagemodel': {
            'Meta': {'object_name': 'ImageModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blogs']