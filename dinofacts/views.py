from django.shortcuts import render
from datetime import datetime

def dinofacts(request):
    return render(request, 'show_dino.html', {})


def show_dino(request, name):
    data = {
    "dinosaurs": [
            "Tyrannosaurus",
            "Stegosaurus",
            "Raptor",
            "Triceratops",
        ],
    "now": datetime.now(),
    }

    return render(request, name + ".html", data)
