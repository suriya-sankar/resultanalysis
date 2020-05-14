from django.contrib import admin
from .models import batches,excel_raw_data,arrears_excel_data,came,reevalutation_data,arrear_reevaluation_data,arrears_count_data
admin.site.register(batches)
admin.site.register(excel_raw_data)
admin.site.register(arrears_excel_data)
admin.site.register(reevalutation_data)
admin.site.register(arrear_reevaluation_data)
admin.site.register(came)
admin.site.register(arrears_count_data)
admin.site.site_header="RESULT ANALYSIS"
