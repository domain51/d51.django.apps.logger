
from south.db import db
from django.db import models
from d51.django.apps.logger.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'UserAction'
        db.create_table('logger_useraction', (
            ('id', models.AutoField(primary_key=True)),
            ('action', models.CharField(max_length=200, db_index=True)),
            ('user', models.ForeignKey(orm['auth.User'])),
            ('created_on', models.DateTimeField(auto_now_add=True)),
            ('content_type', models.ForeignKey(orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', models.PositiveIntegerField(null=True, blank=True)),
        ))
        db.send_create_signal('logger', ['UserAction'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'UserAction'
        db.delete_table('logger_useraction')
        
    
    
    models = {
        'logger.useraction': {
            'action': ('models.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'content_type': ('models.ForeignKey', ["orm['contenttypes.ContentType']"], {'null': 'True', 'blank': 'True'}),
            'created_on': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('models.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('models.ForeignKey', ["orm['auth.User']"], {})
        },
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
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
