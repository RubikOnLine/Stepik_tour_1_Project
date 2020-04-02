from django.shortcuts import render
from django.views import View

from .data import tours

# Create your views here.



class MainView(View):
    def get(self, request, *args, **kwargs):

        context ={}
        context['tours'] = tours

        return render(request, 'tours/index.html', context)

class DepartureView(View):
    def get(self, request, city_id:str):
        context = {}
        data = {}
        i = 0

        for num_tour, decrip_tour in tours.items():
            if decrip_tour["departure"] == city_id:
                data[i] = decrip_tour
                i +=1
                context['city'] = decrip_tour['dep']

        context['min_nights'] = min((data[i]["nights"]) for i in range(len(data)))
        context['max_nights'] = max((data[i]["nights"]) for i in range(len(data)))
        context['min_price'] = min((data[i]["price"]) for i in range(len(data)))
        context['max_price'] = max((data[i]["price"]) for i in range(len(data)))
        context['count'] = i
        context['data'] = data


        return render(request, 'tours/departure.html', context)

class TourView(View):
    def get(self, request, id):
        context = {}

        context['data'] = list(tours[id].values())

        return render(request, 'tours/tour.html', context)
