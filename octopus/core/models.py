from django.db import models


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseSeason(BaseModel):
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.start_year}-{self.end_year}'

    class Meta:
        abstract = True
        verbose_name_plural = 'Seasons'


class BaseTeam(BaseModel):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        verbose_name_plural = 'Teams'


class BaseMatch(BaseModel):
    match_date = models.DateTimeField()
    home_score = models.PositiveIntegerField()
    away_score = models.PositiveIntegerField()

    class Meta:
        abstract = True
        verbose_name_plural = 'Matches'
