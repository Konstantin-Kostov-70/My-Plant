from django.urls import path

from My_exam.my_plant.views import IndexView, CreateProfileView, CatalogueView, CreatePlantView, PlantDetailsView, \
    PlantEditView, ProfileDetailsView, ProfileEditView, ProfileDeleteView, plant_delete, PlantDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profile/create/', CreateProfileView.as_view(), name='create profile'),
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path('create/', CreatePlantView.as_view(), name='create plant'),
    path('details/<int:pk>', PlantDetailsView.as_view(),name='plant details'),
    path('edit/<int:pk>/', PlantEditView.as_view(), name='edit plant'),
    path('delete/<int:pk>/', PlantDeleteView.as_view(), name='delete plant'),
    path('profile/details/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile edit'),
    path('profile/delete<int:pk>/', ProfileDeleteView.as_view(), name='profile delete'),

]