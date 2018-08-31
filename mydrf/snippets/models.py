from django.db import models
from django.contrib.auth.models import User

from pygments.lexers import get_all_lexers

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])


class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='snippets', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title