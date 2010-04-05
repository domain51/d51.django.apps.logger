
from south.db import db
from django.db import models
from d51.django.apps.logger.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Hit.content_type'
        db.add_column('logger_hit', 'content_type', models.ForeignKey(orm['contenttypes.ContentType'], null=True, blank=True))
        
        # Adding field 'Hit.object_id'
        db.add_column('logger_hit', 'object_id', models.PositiveIntegerField(null=True, blank=True))
        
        # Changing field 'Hit.url'
        db.alter_column('logger_hit', 'url', models.URLField(verify_exists=False))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Hit.content_type'
        db.delete_column('logger_hit', 'content_type_id')
        
        # Deleting field 'Hit.object_id'
        db.delete_column('logger_hit', 'object_id')
        
        # Changing field 'Hit.url'
        db.alter_column('logger_hit', 'url', models.URLField())
        
    
    
    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label','model'),)", 'db_table': "'django_content_type'"},
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'logger.hit': {
            'content_type': ('models.ForeignKey', ["orm['contenttypes.ContentType']"], {'null': 'True', 'blank': 'True'}),
            'created_on': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('models.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('models.URLField', [], {'verify_exists': 'False'})
        }
    }
    
    complete_apps = ['logger']
