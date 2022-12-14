from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from .models import Card
from django.db.models import Q
from .forms import CardForm, CardGenerateForm
from .source.source import STATUS_CARD


class CardListView(TemplateView):
    template_name = 'card/card_list.html'

    def get(self, request):
        cards = Card.objects.all()
        return render(request, self.template_name, {"cards": cards})

    def post(self, request):
        card = None
        field = request.POST['fields']
        date = request.POST['date']
        if field == 'series':
            series = request.POST['field']
            if series != "":
                series = int(float(request.POST['field']))
                card = Card.objects.filter(series=series)
        elif field == 'number':
            if request.POST['field'] != "":
                number = int(float(request.POST['field']))
                card = Card.objects.filter(number=number)
        elif field == 'status':
            if request.POST['field'] != "":
                status = request.POST['field']
                card = Card.objects.filter(status=status)


        if date == 'e_date':
            if request.POST['date_field'] != "":
                e_date = request.POST['date_field']
                card = Card.objects.filter(expiration_date=e_date)
        elif date == 'r_date':
            if request.POST['date_field'] != "":
                r_date = request.POST['date_field']
                card = Card.objects.filter(release_date=r_date)

        return render(request, self.template_name, {"cards": card})

class CardDetailView(TemplateView):
    template_name = "card/card_detail.html"

    def get(self,request, pk):
        card = Card.objects.get(pk=pk)
        return render(request, self.template_name, {'card':card})

class CardDeleteView(TemplateView):
    template_name = "card/card_delete.html"

    def get(self, request, pk):
        Card.objects.get(pk = pk).delete()
        return render(request, self.template_name)

    def post(self, request):
        return redirect('card:card_list')


class CardUpdateView(TemplateView):
    template_name = 'card/card_update.html'

    def get(self, request, pk):
        card = Card.objects.get(pk=pk)
        form = CardForm(instance=card)
        return render(request, self.template_name, {'form':form})

    def post(self, request, pk):
        print("HELLO")
        card = Card.objects.get(pk=pk)
        form = CardForm(request.POST, instance=card)

        if form.is_valid():
            form.save()
            return redirect('card:card_list')
        return HttpResponse("Invalid form")

class CardGenerateView(TemplateView):
    template_name = 'card/card_generate.html'

    def get(self, request):
        form = CardGenerateForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = CardGenerateForm(request.POST)
        if form.is_valid():
            series = form.cleaned_data['series']
            quantity = int(form.cleaned_data['quantity'])
            for card in range(quantity):
                Card.objects.create(series=series, number=series,
                                    status=STATUS_CARD[1][0]).save()
            return redirect('card:card_list')
        return HttpResponse("Invalid")
