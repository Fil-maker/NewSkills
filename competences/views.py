from django.shortcuts import render
from .forms import Form
from .models import Direction, Professions, Competence, Standards, Jobs, International
from django.shortcuts import get_object_or_404, Http404
from django.core.exceptions import ObjectDoesNotExist

def create_response(name, response_set):
    return f"{name}:\n" + "*" + "\n\n*".join([i.name for i in response_set])


# Create your views here.
def index(request):
    output = "Что-то пошло не так.\nПопробуйте Позже!"
    if request.method == "POST":
        form = Form(request.POST)
        if not form.is_valid():
            return render(request, "base.html", context={"form": form})
        name = form.data.get("request", None)
        name = name.strip()
        in_type = form.data.get("in_type", None)
        out_type = form.data.get("out_type", None)
        try:
            if in_type == "P":
                obj = Professions.objects.get(name=name)
                if out_type == "P":
                    output = create_response("Профессии", obj.direction.professions_set.all())
                elif out_type == "C":
                    output = create_response("Компетенции", obj.competence_set.all())
                elif out_type == "S":
                    output = create_response("Должности", obj.standards_set.all())
                elif out_type == "J":
                    output = create_response("Конкретика", obj.jobs_set.all())
                elif out_type == "I":
                    output = create_response(
                        "Общепрофессиональные компетенции", obj.international_set.all())
            elif in_type == "C":
                obj = Competence.objects.get(name=name)
                if out_type == "P":
                    output = create_response("Профессии", obj.profession.all())
                if out_type == "C":
                    output = create_response("Компетенции", obj.profession.all()[0].competence_set.all())
                elif out_type == "S":
                    output = create_response("Должности", obj.standards_set.all())
                if out_type == "J":
                    output = create_response("Конкретика", obj.jobs_set.all())
                if out_type == "I":
                    output = create_response("Общепрофессиональные компетенции", obj.international_set.all())
            elif in_type == "S":
                obj = Standards.objects.get(name=name)
                if out_type == "P":
                    output = create_response("Профессии", obj.profession.all())
                if out_type == "C":
                    output = create_response("Компетенции", obj.competences.all())
                elif out_type == "S":
                    output = create_response("Должности", obj.profession.first().standards_set.all())
                if out_type == "J":
                    output = create_response("Конкретика", obj.jobs_set.all())
                if out_type == "I":
                    output = create_response("Общепрофессиональные компетенции", obj.international_set.all())
            elif in_type == "J":
                obj = Jobs.objects.get(name=name)
                if out_type == "P":
                    output = create_response("Профессии", obj.profession.all())
                if out_type == "C":
                    output = create_response("Компетенции", obj.competences.all())
                elif out_type == "S":
                    output = create_response("Должности", obj.standards.all())
                if out_type == "J":
                    output = create_response("Конкретика", obj.profession.first().jobs_set.all())
                if out_type == "I":
                    output = create_response("Общепрофессиональные компетенции", obj.international_set.all())
            elif in_type == "I":
                obj = International.objects.get(name=name)
                if out_type == "P":
                    output = create_response("Профессии", obj.profession.all())
                if out_type == "C":
                    output = create_response("Компетенции", obj.competences.all())
                elif out_type == "S":
                    output = create_response("Должности", obj.standards.all())
                if out_type == "J":
                    output = create_response("Конкретика", obj.jobs.all())
                if out_type == "I":
                    output = create_response(
                        "Общепрофессиональные компетенции", obj.profession.first().international_set.all())
        except Http404 as e:
            print(e)
            output = "Не найдено!"
        except ObjectDoesNotExist as e:
            print(e)
            output = "Не найдено!"
        except Exception as e:
            print(e)
    else:
        form = Form()
    return render(request, "base.html", context={"form": form, "output": output})
