
from django import forms

class NewDevilNameForm(forms.Form):

    # TODO: Validar se o nome é único (não pode cadastrar um nome que já existe)
    name = forms.CharField (
        help_text="Informe o novo nome do Capeta",
        label="Nome do Capeta",
        max_length=255,
        error_messages={'required': 'é necessário informar um Nome do Capeta'}
    )


ORDER_BY_VALUES = [
    ('id', 'ID ASC'),
    ('-id', 'ID DESC'),
    ('name', 'Nome ASC'),
    ('-name', 'Nome DESC'),
    ('creation_date', 'Criação ASC'),
    ('-creation_date', 'Criação DESC'),
]

class DevilNameSearchForm(forms.Form):

    # TODO: Validar se o nome é único (não pode cadastrar um nome que já existe)
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

    # TODO: Validar se o nome é único (não pode cadastrar um nome que já existe)
    csv_file = forms.FileField (
        help_text="Envie apenas arquivos CSV",
        label="Selecione um arquivo",
        error_messages={'required': 'é necessário informar um arquivo'}
    )

