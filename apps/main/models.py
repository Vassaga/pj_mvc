# Django
from django.contrib.auth.models import User
from django.db import models
from typing import Any


# Django
from django.contrib.auth.models import User
from django.db import models
import mutagen


class Country(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=50
    )

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

    def __str__(self):
        return self.title


class Band(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=50
    )
    datetime_created = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    datetime_updated = models.DateTimeField(
        verbose_name='дата обновления',
        auto_now=True
    )
    datetime_deleted = models.DateTimeField(
        verbose_name='дата удаления',
        null=True,
        blank=True
    )
    followers = models.PositiveIntegerField(
        verbose_name='фоловеры',
        default=0
    )
    country = models.OneToOneField(
        to=Country,
        on_delete=models.PROTECT,
        verbose_name='страна'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self) -> str:
        if not self.title:
            return 'Без названия'
        return f'Группа: {self.title}'


class Artist(models.Model):
    """
    Artist model.
    """
    GENDER_OTHER = 0
    GENDER_FEMALE = 1
    GENDER_MALE = 2
    GENDERS = (
        (GENDER_OTHER, 'Остальное'),
        (GENDER_FEMALE, 'Женщина'),
        (GENDER_MALE, 'Мужчина')
    )
    band = models.ForeignKey(
        to=Band,
        on_delete=models.PROTECT,
        verbose_name='группа',
        null=True,
        blank=True
    )
    user = models.OneToOneField(
        to=User,
        on_delete=models.PROTECT,
        verbose_name='пользователь',
        null=True,
        blank=True
    )
    nickname = models.CharField(
        verbose_name='псевдоним',
        default='',
        max_length=50
    )
    gender = models.PositiveSmallIntegerField(
        choices=GENDERS,
        verbose_name='гендер',
        default=GENDER_OTHER
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'музыкант'
        verbose_name_plural = 'музыканты'

    def __str__(self) -> str:
        if not self.nickname:
            return 'Без имени'

        return f'Музыкант: {self.nickname}'


class Genre(models.Model):
    """Genre model."""

    title = models.CharField(
        max_length=50,
        verbose_name='жанр'
    )
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'
        ordering = ('-id',)


class Album(models.Model):
    """
    Album model.
    """
    REGULAR = 0
    SILVER = 1
    GOLD = 2
    PLATINUM = 3
    STATUSES = (
        (REGULAR, 'Обычный'),
        (SILVER, 'Серебряный'),
        (GOLD , 'Золотой'),
        (PLATINUM , 'Платиновый'),
    )
    band = models.ForeignKey(
        to=Band,
        on_delete=models.PROTECT,
        verbose_name='группа'
    )
    title = models.CharField(
        verbose_name='название альбома',
        max_length=150
    )
    release_date = models.DateTimeField(
        verbose_name='дата релиза',
    )
    logo = models.ImageField(
        verbose_name='логотип',
        upload_to='images/',
        null=True,
        blank=True
    )
    status = models.SmallIntegerField(
        choices=STATUSES,
        default=REGULAR,
        verbose_name='статус'
    )

    def __str__(self) -> str:
        return f'{self.band}: {self.title} ({self.status})'

    class Meta:
        ordering = ('release_date',)
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'


class Song(models.Model):
    """Song model."""

    title = models.CharField(
        verbose_name='название песни',
        max_length=50
    )
    album = models.ForeignKey(
        to=Album,
        verbose_name='альбом',
        on_delete=models.CASCADE
    )
    audio_file = models.FileField(
        verbose_name='аудио файл'
    )
    duration = models.DurationField(
        verbose_name='длительность трека'
    )
    genre = models.ManyToManyField(
        to=Genre,
        verbose_name='жанр'
    )
    times_played = models.PositiveIntegerField(
        verbose_name='количество прослушиваний',
        null=True,
        blank=True
    )
    def __str__(self) -> str:
        return f'Song: {self.title}'

    class Meta:
        verbose_name = 'песня'
        verbose_name_plural = 'песни'
        ordering = ('id',)

    def save(self, *args: Any, **kwargs: Any) -> None:

        # TODO: потом сделать через PostSave
        #
        mfile: mutagen.File = mutagen.File(
            self.audio_file
        )
        self.duration = mfile.info.length
        super().save(*args, **kwargs)


