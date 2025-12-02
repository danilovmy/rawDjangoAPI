from django.http import HttpResponse, JsonResponse
from django.views.generic import DetailView, ListView, CreateView
from .models import Pet
from django.core.serializers.json import Serializer

# Create your views here.

class PetListView(ListView):
    model = Pet

    def render_to_response(self, context, *args, **kwargs):
        if 'application/json' in self.request.headers.get('Content-Type', '') or 'application/json' in self.request.headers.get('Accept', ''):
            data = self.list_pets(context)
            return HttpResponse(data, content_type='application/json')
        return super().render_to_response(context, *args, **kwargs)


    def create_pets(body):  # noqa: E501
        validator = modelformfactory(self.model)(self.request.json())
        if validator.is_valid():
            instance = validator.save()
        """Create a pet
        # noqa: E501

        :param pet:
        :type pet: dict | bytes

        :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
        """
        pet = body
        if connexion.request.is_json:
            pet = Pet.from_dict(connexion.request.get_json())  # noqa: E501
        return 'do some magic!'


    def list_pets(cotext):  # noqa: E501
        objects = context.get('object_list')
        """List all pets

        # noqa: E501

        :param limit: How many items to return at one time (max 100)
        :type limit: int

        :rtype: Union[List[Pet], Tuple[List[Pet], int], Tuple[List[Pet], int, Dict[str, str]]
        """
        return Serializer().serialize('json', objects)


class PetDetailView(DetailView):
    model = Pet

    def show_pet_by_id(pet_id):  # noqa: E501
        """Info for a specific pet

        # noqa: E501

        :param pet_id: The id of the pet to retrieve
        :type pet_id: str

        :rtype: Union[Pet, Tuple[Pet, int], Tuple[Pet, int, Dict[str, str]]
        """
        return 'do some magic!'
