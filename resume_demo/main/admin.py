from django.contrib import admin
from .models import (
    UserProfile,
    ContactProfile,
    Testimonial,
    Media,
    Portfolio,
    Blog,
    Certificate,
    Skill,
    Experience,
)


# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "cv")


@admin.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "timestamp", "message")
    list_filter = ("name", "email", "message", "timestamp")
    readonly_fields = ("timestamp",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "role", "is_active")
    list_filter = ("id", "name", "role", "is_active")


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    readonly_fields = ("slug",)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    readonly_fields = ("slug",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("name", "issue_date", "issuing_org", "is_active")
    list_filter = ("issue_date", "issuing_org", "is_active")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "skill_type", "score", "is_key_skill", "id")
    list_filter = ["name", "score", "skill_type", "is_key_skill"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "name_of_company",
        "name_of_position",
        "start_date",
        "is_current_company",
    )
    list_filter = (
        "name_of_company",
        "name_of_position",
        "start_date",
        "is_current_company",
    )
    date_hierarchy = "start_date"
