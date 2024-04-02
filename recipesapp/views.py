from django.shortcuts import render, get_object_or_404
from .models import Recipe

# List view for recipes
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {"recipes":recipes})

# Detail view for each recipe
def recipe_detail(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    return render(request, 'recipe_detail.html', {'recipe': recipe})