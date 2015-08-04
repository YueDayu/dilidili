from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.html import format_html

from dilidili_dev.users import User
from dilidili_dev.models import *


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'describe', 'image')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'id', 'describe', 'money', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'username', 'name', 'email', 'is_admin', 'view_page', )
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('name', 'username', 'password')}),
        ('Personal info', {'fields': ('describe', 'email', 'money', 'image', 'cropping')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'can_comment', 'can_upload',  'can_bullet')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'name', 'describe', 'image')}
        ),
    )
    search_fields = ('username',)
    ordering = ('id', 'username',)
    filter_horizontal = ()

    def view_page(self, obj):
        return format_html('<a href={}>View</a>', obj.get_absolute_url())
    view_page.allow_tags = True


# Now register the new UserAdmin...
admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tag', 'time', 'status', 'published', 'view_link',)
    list_filter = ('status', )
    ordering = ('-time', 'id',)
    search_fields = ('name', 'describe',)
    fieldsets = [
        ('Basic info', {'fields': ['name', 'describe', 'tag', 'category_set']}),
        ('Files', {'fields': ['video', 'image']}),
        ('Status', {'fields': ['status']})
    ]

    def view_link(self, obj):
        return format_html('<a href={}>View</a>', obj.get_absolute_url())
    view_link.allow_tags = True

    def published(self, obj):
        return obj.status == 0
    published.boolean = True


admin.site.register(Video, VideoAdmin)
