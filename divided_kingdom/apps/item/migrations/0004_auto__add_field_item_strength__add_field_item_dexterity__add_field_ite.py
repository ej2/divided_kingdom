# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.strength'
        db.add_column(u'item_item', 'strength',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.dexterity'
        db.add_column(u'item_item', 'dexterity',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.constitution'
        db.add_column(u'item_item', 'constitution',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.intelligence'
        db.add_column(u'item_item', 'intelligence',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.will_power'
        db.add_column(u'item_item', 'will_power',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.perception'
        db.add_column(u'item_item', 'perception',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.arcane_power'
        db.add_column(u'item_item', 'arcane_power',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.presence'
        db.add_column(u'item_item', 'presence',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.manipulation'
        db.add_column(u'item_item', 'manipulation',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.attack'
        db.add_column(u'item_item', 'attack',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.defense'
        db.add_column(u'item_item', 'defense',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.speed'
        db.add_column(u'item_item', 'speed',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.min_damage'
        db.add_column(u'item_item', 'min_damage',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.max_damage'
        db.add_column(u'item_item', 'max_damage',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ItemType.strength'
        db.add_column(u'item_itemtype', 'strength',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ItemType.dexterity'
        db.add_column(u'item_itemtype', 'dexterity',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ItemType.constitution'
        db.add_column(u'item_itemtype', 'constitution',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ItemType.intelligence'
        db.add_column(u'item_itemtype', 'intelligence',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ItemType.will_power'
        db.add_column(u'item_itemtype', 'will_power',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ItemType.perception'
        db.add_column(u'item_itemtype', 'perception',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ItemType.arcane_power'
        db.add_column(u'item_itemtype', 'arcane_power',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ItemType.presence'
        db.add_column(u'item_itemtype', 'presence',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ItemType.manipulation'
        db.add_column(u'item_itemtype', 'manipulation',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ItemType.attack'
        db.add_column(u'item_itemtype', 'attack',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ItemType.defense'
        db.add_column(u'item_itemtype', 'defense',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ItemType.speed'
        db.add_column(u'item_itemtype', 'speed',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ItemType.min_damage'
        db.add_column(u'item_itemtype', 'min_damage',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ItemType.max_damage'
        db.add_column(u'item_itemtype', 'max_damage',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Item.strength'
        db.delete_column(u'item_item', 'strength')

        # Deleting field 'Item.dexterity'
        db.delete_column(u'item_item', 'dexterity')

        # Deleting field 'Item.constitution'
        db.delete_column(u'item_item', 'constitution')

        # Deleting field 'Item.intelligence'
        db.delete_column(u'item_item', 'intelligence')

        # Deleting field 'Item.will_power'
        db.delete_column(u'item_item', 'will_power')

        # Deleting field 'Item.perception'
        db.delete_column(u'item_item', 'perception')

        # Deleting field 'Item.arcane_power'
        db.delete_column(u'item_item', 'arcane_power')

        # Deleting field 'Item.presence'
        db.delete_column(u'item_item', 'presence')

        # Deleting field 'Item.manipulation'
        db.delete_column(u'item_item', 'manipulation')

        # Deleting field 'Item.attack'
        db.delete_column(u'item_item', 'attack')

        # Deleting field 'Item.defense'
        db.delete_column(u'item_item', 'defense')

        # Deleting field 'Item.speed'
        db.delete_column(u'item_item', 'speed')

        # Deleting field 'Item.min_damage'
        db.delete_column(u'item_item', 'min_damage')

        # Deleting field 'Item.max_damage'
        db.delete_column(u'item_item', 'max_damage')

        # Deleting field 'ItemType.strength'
        db.delete_column(u'item_itemtype', 'strength')

        # Deleting field 'ItemType.dexterity'
        db.delete_column(u'item_itemtype', 'dexterity')

        # Deleting field 'ItemType.constitution'
        db.delete_column(u'item_itemtype', 'constitution')

        # Deleting field 'ItemType.intelligence'
        db.delete_column(u'item_itemtype', 'intelligence')

        # Deleting field 'ItemType.will_power'
        db.delete_column(u'item_itemtype', 'will_power')

        # Deleting field 'ItemType.perception'
        db.delete_column(u'item_itemtype', 'perception')

        # Deleting field 'ItemType.arcane_power'
        db.delete_column(u'item_itemtype', 'arcane_power')

        # Deleting field 'ItemType.presence'
        db.delete_column(u'item_itemtype', 'presence')

        # Deleting field 'ItemType.manipulation'
        db.delete_column(u'item_itemtype', 'manipulation')

        # Deleting field 'ItemType.attack'
        db.delete_column(u'item_itemtype', 'attack')

        # Deleting field 'ItemType.defense'
        db.delete_column(u'item_itemtype', 'defense')

        # Deleting field 'ItemType.speed'
        db.delete_column(u'item_itemtype', 'speed')

        # Deleting field 'ItemType.min_damage'
        db.delete_column(u'item_itemtype', 'min_damage')

        # Deleting field 'ItemType.max_damage'
        db.delete_column(u'item_itemtype', 'max_damage')


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
        u'item.item': {
            'Meta': {'object_name': 'Item'},
            'arcane_power': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'attack': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'base_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'constitution': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'defense': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dexterity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'manipulation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'max_damage': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'min_damage': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'perception': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['player.Player']", 'null': 'True', 'blank': 'True'}),
            'presence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'speed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'uses': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'will_power': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'item.itemdrop': {
            'Meta': {'object_name': 'ItemDrop'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drop_rate': ('django.db.models.fields.IntegerField', [], {}),
            'drop_table': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['item.DropTable']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['item.ItemType']"}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'item.itemproperty': {
            'Meta': {'object_name': 'ItemProperty'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'properties'", 'to': u"orm['item.Item']"}),
            'modifier_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'stat_modified': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'item.itemtype': {
            'Meta': {'object_name': 'ItemType'},
            'arcane_power': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'attack': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'base_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'constitution': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'defense': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dexterity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'manipulation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'max_damage': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'min_damage': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'perception': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'presence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'speed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'uses': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'will_power': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'item.itemtypeproperty': {
            'Meta': {'object_name': 'ItemTypeProperty'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'properties'", 'to': u"orm['item.ItemType']"}),
            'modifier_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'stat_modified': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
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
        u'player.motivatingforce': {
            'Meta': {'object_name': 'MotivatingForce'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"})
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
            'distance_marker': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'gold': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['location.Location']", 'null': 'True', 'blank': 'True'}),
            'manipulation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'motivating_force': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['player.MotivatingForce']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'perception': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'presence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['location.Route']", 'null': 'True', 'blank': 'True'}),
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

    complete_apps = ['item']