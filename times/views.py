from django.shortcuts import render
from datetime import datetime

def index(request):
	now = datetime.now()
	t_date = now.strftime('%b %d, %Y')
	t_time = now.strftime('%I:%M %p')
	context = {
		'date': t_date,
		'time': t_time,
	}
	return render(request, 'times/index.html', context)
