from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Provider(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    birth_date = models.DateField()
    rating = models.DecimalField(max_digits=4, decimal_places=1)

    company = models.CharField(max_length=100)
    active = models.BooleanField()
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    count = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def incrementCount(self):
        self.count = self.count + 1
        self.save()


class ProviderSkill(models.Model):
    PRIMARY = 0
    SECONDARY = 1
    SKILL_TYPES = {
                PRIMARY: 'primary',
                SECONDARY: 'secondary',
            }
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    type = models.IntegerField(choices=list(SKILL_TYPES.items()), default=0)

    def __str__(self):
        return self.provider.first_name + ' ' + self.provider.last_name + '->' + self.skill.name + ':' + self.SKILL_TYPES[self.type]

    class Meta:
        unique_together = [['provider', 'skill', 'type']]
