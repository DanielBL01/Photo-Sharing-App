import django_filters

from .models import Post

class PostFilter(django_filters.FilterSet):
    # field_name searches for specifed field/attritube
    # icontains ignores case sensitivity
    # iexact requires all characters to match which is NOT what we want here
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Post

        # We just want to filter by title
        exclude = ['users', 'description', 'date_posted', 'image']


       