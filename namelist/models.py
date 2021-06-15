from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.urls import reverse

class DevilName(models.Model):

    # Fields
    id = models.AutoField(
        primary_key=True,
        verbose_name="ID",
        help_text="Código do nome do capeta",
    )

    name = CharField(
        verbose_name="Nome",
        help_text="Nome do capeta",
        max_length=255,
        unique=True,
    )

    creation_date = DateTimeField(
        verbose_name="Data de criação",
        help_text="Data de criação do nome do capeta",
        auto_now_add=True,
    )

    # Metadata
    class Meta:
        ordering = ['name']
        verbose_name = 'Nome'

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('devil_name_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name