from django import forms


class CreateNewTask(forms.Form):
    title= forms.CharField(label="Titulo de la tarea",max_length=200)
    description=forms.CharField(label="descripcion", widget=forms.Textarea)
    
class CreteNewProject(forms.Form):
    name=forms.CharField(label="Nombre proyecto",max_length=200)