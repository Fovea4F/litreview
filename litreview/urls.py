"""
URL configuration for litreview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path

import authentication.views
import review.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", authentication.views.login_page, name='login'),
    path("logout", authentication.views.logout_page, name='logout'),
    path("signup/", authentication.views.signup_page, name='signup'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'), name='password_change'),
    path('change-password-done', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'), name='password_change_done'),

    path("home/", review.views.home, name='home'),
    path('ticket/create', review.views.ticket_create, name='ticket_create'),
    path('ticket/<int:ticket_id>/', review.views.ticket_edit, name='ticket_edit'),
    path('review/create', review.views.review_and_ticket_create, name='review_ticket_create'),
    path('ticket/<int:ticket_id>/', review.views.review_and_ticket_edit, name='ticket_review_edit'),
    path('review/<int:review_id>/', review.views.review_edit, name='review_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
