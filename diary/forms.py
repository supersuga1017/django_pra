import os

from django import forms
from django.core.mail import EmailMessage
<<<<<<< HEAD
from .models import Diary
=======
>>>>>>> ce8f1603a7b4955e9d1ec2996b6376a5e5e36052

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前',max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル',max_length=30)
    message = forms.CharField(label='メッセージ',widget=forms.Textarea)
    dream = forms.CharField(label='夢っす', widget=forms.Textarea)


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してくださいね。'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'

        self.fields['dream'].widget.attrs['class'] = 'form-control'
        self.fields['dream'].widget.attrs['placeholder'] = 'あなたの夢をここに入力してください。'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問合わせ{}'.format(title)
        message = 'お問合わせよ:{0}\nメールアドレスだよ：{1}\nメッセージだよ：{2}'.format(name,email,message)

        from_email = os.environ.get('FROM_EMAIL')
        to_list = [
            os.environ.get('FROM_EMAIL')
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject= subject,body=message,from_email=from_email,to=to_list,cc=cc_list)
<<<<<<< HEAD
        message.send()


class SugaForm(forms.Form):
    name = forms.CharField(label='やる気',max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='棒読み感',max_length=30)
    message = forms.CharField(label='不思議さ',widget=forms.Textarea)
    dream = forms.CharField(label='度胸', widget=forms.Textarea)


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してくださいね。'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'

        self.fields['dream'].widget.attrs['class'] = 'form-control'
        self.fields['dream'].widget.attrs['placeholder'] = 'あなたの夢をここに入力してください。'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問合わせ{}'.format(title)
        message = 'お問合わせよ:{0}\nメールアドレスだよ：{1}\nメッセージだよ：{2}'.format(name,email,message)

        from_email = os.environ.get('FROM_EMAIL')
        to_list = [
            os.environ.get('FROM_EMAIL')
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject= subject,body=message,from_email=from_email,to=to_list,cc=cc_list)
        message.send()



class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Diary
        # fields = ('title','content','photo1','photo2','photo3')
        fields = ('title','content')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'



=======
        message.send()
>>>>>>> ce8f1603a7b4955e9d1ec2996b6376a5e5e36052
