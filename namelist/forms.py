
from django import forms

class NewDevilNameForm(forms.Form):

    # TODO: Validar se o nome é único (não pode cadastrar um nome que já existe)
    name = forms.CharField (
        help_text="Informe o novo nome do Capeta",
        label="Nome do Capeta",
        max_length=255,
        error_messages={'required': 'é necessário informar um Nome do Capeta'}
    )