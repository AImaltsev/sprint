from django.urls import path
from .views import SubmitDataView, GetPerevalByIdView, EditPerevalView, GetUserPerevalsView

urlpatterns = [
    path('submitData/', SubmitDataView.as_view(), name='submit_data'),
    path('submitData/<int:id>/', GetPerevalByIdView.as_view(), name='get_pereval_by_id'),
    path('submitData/<int:id>/edit/', EditPerevalView.as_view(), name='edit_pereval'),
    path('submitData/user/', GetUserPerevalsView.as_view(), name='get_user_perevals'),
]