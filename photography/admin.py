from django.contrib import admin

from .models import RyersonEvent, RyersonEventImage, TCEModel, TCEImage, Creative, ProjectImage

# Register Ryerson Events
class RyersonEventImageAdmin(admin.StackedInline):
    model = RyersonEventImage

@admin.register(RyersonEvent)
class RyersonEventAdmin(admin.ModelAdmin):
    inlines = [RyersonEventImageAdmin]

    class Meta:
        model = RyersonEvent

@admin.register(RyersonEventImage)
class RyersonEventImageAdmin(admin.ModelAdmin):
    def get_model_perms(self,request):
        return {}

# Register TCE
class TCEImageAdmin(admin.StackedInline):
    model = TCEImage

@admin.register(TCEModel)
class TCEAdmin(admin.ModelAdmin):
    inlines = [TCEImageAdmin]

    class Meta:
        model = TCEModel

@admin.register(TCEImage)
class TCEImageAdmin(admin.ModelAdmin):
    def get_model_perms(self,request):
        return {}

# Register Creative
class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage

@admin.register(Creative)
class CreativeAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]
    prepopulated_fields = {'slug': ('project_title',)}
    
    class Meta:
        model = Creative

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    def get_model_perms(self,request):
        return {}