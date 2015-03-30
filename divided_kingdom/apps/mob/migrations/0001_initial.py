# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MobType'
        db.create_table(u'mob_mobtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('is_named', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('total_health', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total_stamina', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('strength', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dexterity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('constitution', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('intelligence', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('will_power', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('perception', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('arcane_power', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('presence', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('manipulation', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('attack', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('defense', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('speed', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'mob', ['MobType'])

        # Adding model 'Mob'
        db.create_table(u'mob_mob', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('mob_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mob.MobType'])),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total_health', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total_stamina', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('current_health', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('current_stamina', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('strength', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dexterity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('constitution', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('intelligence', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('will_power', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('perception', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('arcane_power', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('presence', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('manipulation', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('attack', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('defense', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('speed', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('route', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['location.Route'])),
            ('drop_table', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['item.DropTable'])),
        ))
        db.send_create_signal(u'mob', ['Mob'])

        # Adding model 'Encounter'
        db.create_table(u'mob_encounter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('route', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['location.Route'], unique=True)),
            ('max_rate', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mob', ['Encounter'])

        # Adding model 'MobEncounter'
        db.create_table(u'mob_mobencounter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('mob_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mob.MobType'])),
            ('encounter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mobs', to=orm['mob.Encounter'])),
            ('encounter_rate', self.gf('django.db.models.fields.IntegerField')()),
            ('drop_table', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['item.DropTable'])),
        ))
        db.send_create_signal(u'mob', ['MobEncounter'])


    def backwards(self, orm):
        # Deleting model 'MobType'
        db.delete_table(u'mob_mobtype')

        # Deleting model 'Mob'
        db.delete_table(u'mob_mob')

        # Deleting model 'Encounter'
        db.delete_table(u'mob_encounter')

        # Deleting model 'MobEncounter'
        db.delete_table(u'mob_mobencounter')


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
        u'item.droptable': {
            'Meta': {'object_name': 'DropTable'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_rate': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'location.location': {
            'Meta': {'object_name': 'Location'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'location.route': {
            'Meta': {'object_name': 'Route'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'distance': ('django.db.models.fields.IntegerField', [], {}),
            'end_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ending_routes'", 'to': u"orm['location.Location']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'starting_routes'", 'to': u"orm['location.Location']"}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'mob.encounter': {
            'Meta': {'object_name': 'Encounter'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_rate': ('django.db.models.fields.IntegerField', [], {}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['location.Route']", 'unique': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'mob.mob': {
            'Meta': {'object_name': 'Mob'},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'arcane_power': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'attack': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'constitution': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'current_health': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'current_stamina': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'defense': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dexterity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'drop_table': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['item.DropTable']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'manipulation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mob_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mob.MobType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'perception': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'presence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['location.Route']"}),
            'speed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_health': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_stamina': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'will_power': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'mob.mobencounter': {
            'Meta': {'object_name': 'MobEncounter'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drop_table': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['item.DropTable']"}),
            'encounter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mobs'", 'to': u"orm['mob.Encounter']"}),
            'encounter_rate': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mob_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mob.MobType']"}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'mob.mobtype': {
            'Meta': {'object_name': 'MobType'},
            'arcane_power': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'attack': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'constitution': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'defense': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dexterity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'is_named': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manipulation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'perception': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'presence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'speed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_health': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_stamina': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'will_power': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['mob']