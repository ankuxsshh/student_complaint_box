from django.contrib import admin
from .models import complaint_box_register
from .models import complaint_box_complaint
from .models import complaint_box_faculty
from .models import complaint_box_acknowledgement
from .models import complaint_box_faculty_acknowledgement

# Register your models here.

admin.site.register(complaint_box_register)
admin.site.register(complaint_box_complaint)
admin.site.register(complaint_box_faculty)
admin.site.register(complaint_box_acknowledgement)
admin.site.register(complaint_box_faculty_acknowledgement)


