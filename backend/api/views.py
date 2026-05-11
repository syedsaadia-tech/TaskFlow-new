from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

tasks = []

@csrf_exempt
def create_task(request):
    if request.method == "POST":
        data = json.loads(request.body)

        task = {
            "title": data.get("title"),
            "description": data.get("description"),
            "due_date": data.get("due_date"),
            "member_email": data.get("member_email"),
            "assigned_date": data.get("assigned_date"),
            "status": data.get("status", "Pending"),
            "progress": data.get("progress", 0)
        }

        tasks.append(task)
        return JsonResponse({"message": "created"})


def get_tasks(request):
    return JsonResponse(tasks, safe=False)


@csrf_exempt
def update_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        index = data.get("index")

        if index is not None and index < len(tasks):

            if "progress" in data:
                tasks[index]["progress"] = int(data["progress"])

            if "status" in data:
                tasks[index]["status"] = data["status"]

            return JsonResponse({"message": "updated"})

        return JsonResponse({"error": "invalid"})