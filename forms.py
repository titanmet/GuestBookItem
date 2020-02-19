from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm

from models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        include = [
            'user_id',
        ]

