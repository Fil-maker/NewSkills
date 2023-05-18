from django.shortcuts import render
from .forms import Form
# from .models import Competence, Professions
from django.shortcuts import get_object_or_404, Http404


# Create your views here.
def index(request):
    output = ""
    if request.method == "POST":
        form = Form(request.POST)
        # print(form.data)
        if not form.is_valid():
            return render(request, "base.html", context={"form": form})
        req = form.data.get("request", None)
        try:
            in_type = form.data.get("in_type", None)
            out_type = form.data.get("out_type", None)
            # if in_type == "P":
            #     p = get_object_or_404(Professions, name=req.lower())
            #     print(p.competence_set())
            #     if out_type == "C":
            #         for c in p.required_competences.all():
            #             output += c.name + "\n"
            #     elif out_type == "P":
            #         for p in p.similar.all():
            #             output += p.name + "\n"
            # elif in_type == "C":
            #     c = get_object_or_404(Competence, name=req.lower())
            #     if out_type == "P":
            #         for p in c.suiting_jobs.all():
            #             output += p.name + "\n"
            #     elif out_type == "C":
            #         for cs in c.similar.all():
            #             output += cs.name + "\n"
        except Http404:
            output = "Что-то пошло не так.\nПопробуйте Позже!"
    else:
        form = Form()
    return render(request, "base.html", context={"form": form, "output": output})
