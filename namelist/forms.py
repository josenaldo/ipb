
from django import forms

ORDER_BY_VALUES = [
    ('id', 'ID ASC'),
    ('-id', 'ID DESC'),
    ('name', 'Nome ASC'),
    ('-name', 'Nome DESC'),
    ('creation_date', 'Criação ASC'),
    ('-creation_date', 'Criação DESC'),
]

class DevilNameSearchForm(forms.Form):

    search = forms.CharField (
        help_text="Pesquise",
        label="Pesquisa",
        max_length=255,
        required=False,
    )

    ordering = forms.ChoiceField(
        label="Ordenação",
        required=False,
        choices=ORDER_BY_VALUES,
        initial=ORDER_BY_VALUES[2],
    )

class ImportDevilNameForm(forms.Form):

    csv_file = forms.FileField (
        help_text="Envie apenas arquivos CSV",
        label="Selecione um arquivo",
        error_messages={'required': 'é necessário informar um arquivo'}
    )

