from django.contrib import admin
from django.db import models

# Models
from .models import Question, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Question admin"""
    list_display = (
        'pk',
        'profile',
        'title', 
        'detail_question',
        'photo',
        'created', 
        'modified'
    )
    
    list_display_links = (
        'pk',
        'profile'
    )
    
    list_editable = (
        'title',
        'detail_question',
    )
    
    list_filter = (
        'created', 
        'modified',
        'profile__user__is_active',
        'profile__user__is_staff',
    )

    fieldsets = (
        ('Profile', {
            'fields':(
                ('profile'),
                ('title', 'detail_question'),
                ('photo',)
            )
        }),
        ('Metadata', {
            'fields':(
                ('created', 'modified')
            )
        })
    )
    readonly_fields= ('profile','created', 'modified')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """answer admin"""
    list_display = (
        'pk',
        'question_id', 
        'profile',
        'detail_answer',
        'likes',
        'dislikes',
        'is_correct',
        'created', 
        'modified',
    ) 
    
    list_display_links = (
        'pk',
        'profile'
    )
    
    list_editable = (
        'detail_answer',
    )
    
    list_filter = (
        'created', 
        'modified',
        'profile__user__is_active',
        'profile__user__is_staff',
    )

    fieldsets = (
        ('Profile', {
            'fields':(
                ('profile', 'detail_answer'),
            )
        }),
        ('Metadata', {
            'fields':(
                ('created', 'modified')
            )
        })
    )
    readonly_fields= ('profile','created', 'modified')
