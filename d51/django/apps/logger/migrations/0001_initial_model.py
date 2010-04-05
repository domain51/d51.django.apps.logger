
from south.db import db
from django.db import models
from d51.django.apps.logger.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Hit'
        db.create_table('logger_hit', (
            ('id', models.AutoField(primary_key=True)),
            ('url', models.URLField()),
            ('created_on', models.DateTimeField(auto_now_add=True)),
        ))
        db.send_create_signal('logger', ['Hit'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Hit'
        db.delete_table('logger_hit')
        
    
    
    models = {
        'logger.hit': {
            'created_on': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'url': ('models.URLField', [], {})
        }
    }
    
    complete_apps = ['logger']
