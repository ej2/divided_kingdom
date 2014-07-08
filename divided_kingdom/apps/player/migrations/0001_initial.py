# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'player_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='players', null=True, to=orm['auth.User'])),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('xp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('gold', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('action_points', self.gf('django.db.models.fields.IntegerField')(default=50)),
            ('skill_points', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('total_health', self.gf('django.db.models.fields.IntegerField')(default=20)),
            ('current_health', self.gf('django.db.models.fields.IntegerField')(default=20)),
            ('total_stamina', self.gf('django.db.models.fields.IntegerField')(default=20)),
            ('current_stamina', self.gf('django.db.models.fields.IntegerField')(default=20)),
            ('strength', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dexterity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('constitution', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('intelligence', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('will_power', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('perception', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('arcane_power', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('presence', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('manipulation', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('attack', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('defense', self.gf('django.db.models.fields.IntegerField')(default=20)),
            ('speed', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'player', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table(u'player_player')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'player.player': {
            'Meta': {'object_name': 'Player'},
            'action_points': ('django.db.models.fields.IntegerField', [], {'default': '50'}),
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'arcane_power': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'attack': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'constitution': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'current_health': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            'current_stamina': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'defense': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            'dexterity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'gold': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'manipulation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'perception': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'presence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'skill_points': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'speed': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_health': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            'total_stamina': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'players'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'will_power': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'xp': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['player']