from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import UserProfile, Blog, Portfolio, Testimonial, Certificate, Experience

from django.views import generic

from .forms import ContactForm


# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)
        experience = Experience.objects.all()

        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        context["experience"] = experience

        return context


class ContactView(generic.FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        received_form: ContactForm = form.save()
        print(received_form.name, received_form.message, received_form.email)
        self.__email(contact_form=received_form)
        print("EMAIL WAS SENT")
        messages.success(self.request, "Thank you. We will be in touch soon!")
        return super().form_valid(form)

    def __email(self, contact_form: ContactForm):
        send_mail(
            f"Email from: {contact_form.name}, {contact_form.email}",
            f"{contact_form.message}",
            f"{settings.EMAIL_HOST_USER}",
            [settings.EMAIL_RECEIVER],
            fail_silently=False,
        )


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "main/portfolio-detail.html"


class BlogView(generic.ListView):
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "main/blog-detail.html"
