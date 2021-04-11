from django import template
from django.http import HttpResponseRedirect
from django.urls import reverse
from ..models import Category
from ..forms import PostForm


register = template.Library()

@register.simple_tag
def categories():
    return Category.objects.all()

@register.inclusion_tag('post/post_modal.html', takes_context=True)
def post_modal(context):
    form = PostForm()
    return {'modal_form': form}
        
