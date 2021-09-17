from django.contrib import admin
from django.db import models

# Models
from .models import Question, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Question admin"""
    list_display = (
        'pk', 
        'user', 
        'profile',
        'title', 
        'detail_question',
        'photo',
        'created', 
        'modified'
    )
    
    list_display_links = (
        'pk',
        'user'
    )
    
    list_editable = (
        'title',
        'detail_question',
    )
    
    list_filter = (
        'created', 
        'modified',
        'user__is_active',
        'user__is_staff',
    )

    fieldsets = (
        ('Profile', {
            'fields':(
                ('user'),
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
    readonly_fields= ('user','created', 'modified')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """answer admin"""
    list_display = (
        'pk',
        'question_id', 
        'user', 
        'profile',
        'detail_answer',
        'likes',
        'dislikes',
        'correct',
        'created', 
        'modified',
    ) 
    
    list_display_links = (
        'pk',
        'user'
    )
    
    list_editable = (
        'detail_answer',
    )
    
    list_filter = (
        'created', 
        'modified',
        'user__is_active',
        'user__is_staff',
    )

    fieldsets = (
        ('Profile', {
            'fields':(
                ('user', 'detail_answer'),
            )
        }),
        ('Metadata', {
            'fields':(
                ('created', 'modified')
            )
        })
    )
    readonly_fields= ('user','created', 'modified')