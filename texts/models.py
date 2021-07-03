from django.db import models

import uuid
from decimal import Decimal
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = models.CharField(max_length=128, unique=True)

    class Meta:
        db_table = 'texts_tag'
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.tag

    def save(self, *args, **kwargs):
        super(Tag, self).save(*args, **kwargs)
        self.tag = self.tag.lower()


class TextSnippet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    creator = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(db_index=True, auto_now_add=True)
    tag = models.ForeignKey('texts.Tag', on_delete=models.CASCADE)

    class Meta:
        db_table = 'texts_text_snippet'
        verbose_name = _('text snippet')
        verbose_name_plural = _('text snippets')
        ordering = ('-timestamp',)

    def __str__(self):
        return self.title
