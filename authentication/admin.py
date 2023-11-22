from django.contrib import admin
from authentication.models import User
from review.models import Ticket
from review.models import Review
from review.models import UserFollows


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'is_active', 'date_joined', 'is_superuser', 'last_login')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user', 'image', 'time_created')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('rating', 'user', 'headline', 'body', 'time_created')


class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ('user', 'followed_user')


admin.site.register(User, UserAdmin)       # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserFollows, UserFollowsAdmin)
