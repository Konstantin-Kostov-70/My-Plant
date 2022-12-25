from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from My_exam.my_plant.forms import PlantForm
from My_exam.my_plant.models import Profile, Plant


class IndexView(views.ListView):
    model = Profile
    template_name = 'home-page.html'

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        return context


class CreateProfileView(views.CreateView):
    context_object_name = 'profile'
    model = Profile
    template_name = 'create-profile.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('catalogue')


class CatalogueView(views.ListView):
    context_object_name = 'plants'
    model = Plant
    template_name = 'catalogue.html'


class CreatePlantView(views.CreateView):
    context_object_name = 'plant'
    model = Plant
    template_name = 'create-plant.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('catalogue')


class PlantDetailsView(views.DetailView):
    context_object_name = 'plant'
    model = Plant
    template_name = 'plant-details.html'


class PlantEditView(views.UpdateView):
    context_object_name = 'plant'
    model = Plant
    template_name = 'edit-plant.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('catalogue')


class PlantDeleteView(views.DeleteView):
    model = Plant
    template_name = 'delete-plant.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            form = PlantForm(instance=self.object)
        else:
            form = PlantForm(self.request.POST)
            if form.is_valid():
                form.save()

        context['form'] = form
        return context

    def get_success_url(self):
        return reverse_lazy('catalogue')


def plant_delete(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PlantForm(instance=plant)

    else:
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'delete-plant.html', context)


class ProfileDetailsView(views.TemplateView):
    model = Profile
    template_name = 'profile-details.html'

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get()
        plant_count = Plant.objects.count()
        plants = Plant.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        context['plant_count'] = plant_count
        context['plants'] = plants
        return context


class ProfileEditView(views.UpdateView):
    context_object_name = 'profile'
    model = Profile
    template_name = 'edit-profile.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('profile details')


class ProfileDeleteView(views.DeleteView):
    model = Profile
    template_name = 'delete-profile.html'

    def get_success_url(self):
        return reverse_lazy('index')








