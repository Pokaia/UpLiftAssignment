from django.contrib import admin

from providers.models import Provider, Skill, ProviderSkill

admin.site.register(Provider)
admin.site.register(Skill)
admin.site.register(ProviderSkill)
