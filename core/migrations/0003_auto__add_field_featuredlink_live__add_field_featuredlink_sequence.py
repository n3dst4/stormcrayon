# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'FeaturedLink.live'
        db.add_column('core_featuredlink', 'live', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'FeaturedLink.sequence'
        db.add_column('core_featuredlink', 'sequence', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'FeaturedLink.live'
        db.delete_column('core_featuredlink', 'live')

        # Deleting field 'FeaturedLink.sequence'
        db.delete_column('core_featuredlink', 'sequence')


    models = {
        'core.featuredlink': {
            'Meta': {'object_name': 'FeaturedLink'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_markdown': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'image_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['core']
