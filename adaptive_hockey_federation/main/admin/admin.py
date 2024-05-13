from django.contrib import admin
from main.admin.inlines import (
    DocumentInline,
    PlayerInline,
    PlayerTeamInline,
    StaffTeamMemberTeamInline,
)
from main.forms import PlayerForm, TeamForm


class CityAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")
    search_fields = ("name",)
    ordering = ["name"]


class NosologyAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")
    search_fields = ("name",)
    ordering = ["name"]


class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "nosology")
    search_fields = (
        "pk",
        "name",
        "nosology__name",
    )
    ordering = ["name"]


class DisciplineNameAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")
    search_fields = ("name",)
    ordering = ["name"]


class DisciplineLevelAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")
    search_fields = ("name",)
    ordering = ["name"]


class DocumentAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "file")
    search_fields = (
        "name",
        "file",
    )
    ordering = ["name"]


class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ("pk", "surname", "name", "patronymic", "phone")
    search_fields = (
        "pk",
        "surname",
        "name",
        "patronymic",
        "phone",
    )


class StaffTeamMemberAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "staff_member",
        "staff_position",
        "qualification",
        "notes",
    )
    search_fields = (
        "pk",
        "staff_member__name",
        "staff_member__surname",
        "staff_member__patronymic",
        "staff_position",
        "qualification",
        "notes",
    )


class PlayerAdmin(admin.ModelAdmin):
    change_form_template = "admin/custom_change_form.html"
    form = PlayerForm
    list_display = (
        "pk",
        "surname",
        "name",
        "patronymic",
        "birthday",
        "gender",
        "get_nosology",
        "diagnosis",
        "discipline_name",
        "discipline_level",
        "level_revision",
        "position",
        "number",
        "is_captain",
        "is_assistent",
        "identity_document",
    )
    search_fields = (
        "pk",
        "surname",
        "name",
        "patronymic",
        "birthday",
        "gender",
        "diagnosis__nosology__name",
        "discipline_name__name",
        "discipline_level__name",
        "level_revision",
        "position",
        "number",
        "identity_document",
    )
    ordering = ["surname", "name", "patronymic", "birthday"]
    inlines = (
        PlayerInline,
        DocumentInline,
    )
    fieldsets = (
        (
            "Персональные данные",
            {
                "classes": ("collapse",),
                "fields": (
                    (
                        "surname",
                        "name",
                    ),
                    "patronymic",
                    (
                        "gender",
                        "birthday",
                    ),
                    "identity_document",
                    "discipline_name",
                    "discipline_level",
                    "nosology",
                    "diagnosis",
                    "level_revision",
                    "addition_date",
                ),
            },
        ),
        (
            "Игровые данные",
            {
                "classes": ("collapse",),
                "fields": (
                    "position",
                    (
                        "number",
                        "is_captain",
                        "is_assistent",
                    ),
                ),
            },
        ),
    )
    readonly_fields = ("addition_date",)
    list_filter = ("addition_date",)

    @admin.display(
        description="Нозология", ordering="diagnosis__nosology__name"
    )
    def get_nosology(self, obj):
        return obj.diagnosis.nosology.name


class TeamAdmin(admin.ModelAdmin):
    form = TeamForm
    change_form_template = "admin/custom_change_form.html"
    list_display = (
        "pk",
        "name",
        "city",
        "discipline_name",
    )
    search_fields = (
        "pk",
        "name",
        "city__name",
        "discipline_name__name",
    )
    ordering = ["name"]
    inlines = (
        StaffTeamMemberTeamInline,
        PlayerTeamInline,
    )
