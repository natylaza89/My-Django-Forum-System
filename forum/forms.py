from .models import MainTopic, Comment, Reply
from django.forms import ModelForm, HiddenInput


class NewCommentForm(ModelForm):
  
    class Meta:
        model = Comment
        fields = ['message_body']
        widgets = {
          'datetime': HiddenInput(),
          'forum': HiddenInput(),
        }

class NewPostForm(ModelForm):
  
    class Meta:
        model = MainTopic
        fields = ['title', 'announcement', 'closed', 'message_body']
        widgets = {
          'datetime': HiddenInput(),
          'forum': HiddenInput(),
        }


class NewReplyForm(ModelForm):
  
    class Meta:
        model = Reply
        fields = ['message_body']
        widgets = {
          'datetime': HiddenInput(),
          'forum': HiddenInput(),
        }