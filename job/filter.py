import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('owner','salary','published_at','vacancy','experience','image','slug')