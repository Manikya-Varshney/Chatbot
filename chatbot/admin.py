from django.contrib import admin

from .models import Note
from .models import Query
from .models import Unanswered_Query
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.forms import ValidationError

class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ['timestamp']

class QueryResource(resources.ModelResource):
    class Meta:
        '''
            attributes -
            model : Which model to use
            skip_unchanged : skip import of unchnaged records
            report_skipped : Report what columns are skipped
            exclude : What fields to exclude
            import_id_fields : What fields to include in import
            fields : What fields to include in import export resource.
        '''
        model = Query
        skip_unchanged = True
        report_skipped = False
        exclude = ('id')
        import_id_fields = ('question', 'response',)
        fields = ('question', 'response',)
    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        for row in dataset:
            print(row)
            if row[0] is None and row[1] is None:
                raise ValidationError('Row cannot be empty\n')
            elif row[1] is None:
                raise ValidationError(' Response cannot be null for question = %s\n' % row[0])
            elif row[0] is None:
                raise ValidationError(' Question cannot be null for response = %s\n' % row[1])
        return

class QueryAdmin(ImportExportModelAdmin):
    '''
        Admin integration is achieved by subclassing ImportExportModelAdmin or one
        of the available mixins. It registers our QueryResource in Admin panel.
    '''
    resource_class = QueryResource

admin.site.register(Note, NoteAdmin)
admin.site.register(Query, QueryAdmin)
admin.site.register(Unanswered_Query, QueryAdmin)
