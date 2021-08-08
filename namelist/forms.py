
from django import forms

class NewDevilNameForm(forms.Form):

    # TODO: Validar se o nome é único (não pode cadastrar um nome que já existe)
    name = forms.CharField (
        help_text="Informe o novo nome do Capeta",
        label="Nome do Capeta",
        max_length=255,
        error_messages={'required': 'é necessário informar um Nome do Capeta'}
    )

class ImportDevilNameForm(forms.Form):

    # TODO: Validar se o nome é único (não pode cadastrar um nome que já existe)
    csv_file = forms.FileField (
        help_text="Envie apenas arquivos CSV",
        label="Selecione um arquivo de Nomes do Capeta",
        error_messages={'required': 'é necessário informar um arquivo'}
    )