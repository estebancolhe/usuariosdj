from tkinter.tix import Form
from django import forms
from django.contrib.auth import authenticate

from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        min_length=6 , label='Contraseña', required=True, widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        min_length=6, label='Contraseña', required=True, widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )

    class Meta:

        model = User
        fields = ('username','email','nombres','apellidos','genero')

    #para hacer la validacion del campo que quiero validar debo utilizar...
    #el metodo clean_campo_a_validar
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            #se quiere que sí password1 y password2 no son iguales, entonces...
            #se pinte el error en el conjunto de errores que muestra el formulario de Django
            #para agregar el error se utiliza el metodo "add_error()", es necesario que el...
            #primer argumento del metodo sea el nombre del campo al cual yo quiero asignarle...
            #el error, es decir, al lado de que campo yo quiero que me muestre ese error

            #el segundo argumento del metodo es el texto del error que va a mostrar
            self.add_error('password2', 'Las contraseñas no son iguales')

class LoginForm(forms.Form):
    username = forms.CharField(label='username',required=True, widget=forms.TextInput(attrs=
    {
        'placeholder':'username',
        'style': '{ margin: 10px }',
    }))
    password = forms.CharField(label='contraseña', required=True, widget=forms.PasswordInput(
        attrs={
            'placeholder':'contraseña'
        }
    ))

    def clean(self):
        #se quiere realizar desde el form la validacion del usuario...
        #como la validacion no implica un solo campo, sino que son dos...
        #(username, password) se pone el metodo clean y Django ya sabe...
        #que esta es una de las primeras validaciones que debe realizar
        cleaned_data = super(LoginForm, self).clean()
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')

        return self.cleaned_data
        #anteriormente se ponia un return para un campo en especifico, 
        #return cleaned_data["username"] o return cleaned_data["password"], pero en este caso...
        #no hay como hacerlo, para eso se crea la variable "cleaned_data"...
        #que quiere decir  retorne todos los datos


class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'contraseña actual'
            }
        )
    )
    password2 = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'contraseña nueva'
            }
        )
    )


class VerificationForm(forms.Form):
    codregistro = forms.CharField(required=True)

    def __init__(self, pk, *args, **kwargs):
        self.id_user= pk
        super(VerificationForm, self).__init__(*args, **kwargs)

    def clean_codregistro(self):
        codigo = self.cleaned_data['codregistro']

        if len(codigo) == 6:
            #se verifica si el codigo y el id el usuario son validos:
            activo = User.objects.cod_validation(self.id_user, codigo)
            if not codigo:
                raise forms.ValidationError('Codigo incorrecto')
        else:
            raise forms.ValidationError('Codigo incorrecto')