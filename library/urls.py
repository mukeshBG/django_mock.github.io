from django.urls import path
from library.views import borrowing_details
urlpatterns = [
    path('borrowing/<int:Borrowing_id>',borrowing_details)
]
