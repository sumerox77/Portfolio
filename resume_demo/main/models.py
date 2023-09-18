from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


class Skill(models.Model):
    class Meta:
        verbose_name_plural = "Skills"
        verbose_name = "Skill"

    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)

    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)

    class SkillDomain(models.TextChoices):
        PROGRAMMING_LANGUAGE = "PL", _("Programming Language")
        FRAMEWORK = "FW", _("Framework")
        DATABASE = "DB", _("Database")
        OTHER_TECHNOLOGY = "OT", _("Other...")

    skill_type = models.CharField(
        max_length=2,
        choices=SkillDomain.choices,
        default=SkillDomain.PROGRAMMING_LANGUAGE,
    )

    def __str__(self):
        return self.name


class Experience(models.Model):
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experience"

    name_of_company = models.CharField(max_length=50, blank=True, null=True)
    name_of_position = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    exit_date = models.DateField(blank=True, null=True)
    company_image = models.ImageField(blank=True, null=True, upload_to="company")
    is_current_company = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name_of_position} at {self.name_of_company}"


class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = "User Profiles"
        verbose_name = "User Profile"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")
    experience = models.ManyToManyField(Experience, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = "Contact Profiles"
        verbose_name = "Contact Profile"
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f"{self.name}"


class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = "Testimonials"
        verbose_name = "Testimonial"
        ordering = ["name"]

    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Media(models.Model):
    class Meta:
        verbose_name_plural = "Media Files"
        verbose_name = "Media"
        ordering = ["name"]

    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = "Portfolio Profiles"
        verbose_name = "Portfolio"
        ordering = ["name"]

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class Blog(models.Model):
    class Meta:
        verbose_name_plural = "Blog Profiles"
        verbose_name = "Blog"
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class Certificate(models.Model):
    class Meta:
        verbose_name_plural = "Certificates"
        verbose_name = "Certificate"

    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    issuing_org = models.CharField(max_length=200, blank=True, null=True)
    credential_id = models.CharField(max_length=200, blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
