# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        db.delete_primary_key("core_featuredlink")
        db.delete_column("core_featuredlink", "id")
        db.rename_column("core_featuredlink", "temp_id", "id")
        db.create_primary_key("core_featuredlink", ["id"])
        


    def backwards(self, orm):
        "Write your backwards methods here."


    models = {
        'core.featuredlink': {
            'Meta': {'ordering': "('sequence', 'name')", 'object_name': 'FeaturedLink'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_markdown': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'image_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'temp_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']
