from django import forms
from django.forms import model_to_dict
from divided_kingdom.apps.core.game_settings import BASE_HEALTH, BASE_STAMINA
from divided_kingdom.apps.player.models import GENDER, Player


class PlayerForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "span3"}))
    gender = forms.ChoiceField(required=False, choices=GENDER)
    age = forms.IntegerField(min_value=17, max_value=75)

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop("instance", None)

        super(PlayerForm, self).__init__(*args, **kwargs)

        if self.instance:
            self.initial = model_to_dict(self.instance)

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if not self.is_edit and Player.objects.filter(name=name).exists():
            raise forms.ValidationError(
                "A player with this name already exists")

        return name

    @property
    def is_edit(self):
        return self.instance is not None

    def save(self):

        data = self.cleaned_data
        player = self.instance or Player()

        player.name = data.get("name")
        player.gender = data.get("gender")
        player.age = data.get("age")

        player.xp = 0

        player.save()

        return player