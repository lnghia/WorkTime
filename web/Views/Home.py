from api.models.TimeSheet import TimeSheet
from api.models.Worker import Worker
from django.shortcuts import redirect, render
from datetime import date
import datetime as dt
from django.contrib.auth.decorators import login_required
from ..constants import RowClasses


@login_required(login_url='/login/')
def index(request):
    worker = Worker.objects.filter(user=request.user)
    
    if len(worker):
        worker = worker[0]
        worker.update_start_of_month(date.today())
        start_day = worker.start_of_month
        days_in_month = []
        row_classes = []
        for i in range(28):
            tmp = start_day + dt.timedelta(days=i)
            i_th_next_day = TimeSheet.objects.filter(date=tmp)
            if len(i_th_next_day):
                if i_th_next_day[0].work_in is None or i_th_next_day[0].work_out is None:
                    row_classes.append(RowClasses.warning)
                else:
                    row_classes.append(RowClasses.primary)
                days_in_month.append({'date': tmp, 'work_in': i_th_next_day[0].work_in, 'work_out': i_th_next_day[0].work_out}) 
            else:
                row_classes.append(RowClasses.default)
                days_in_month.append({'date': tmp, 'work_in': '', 'work_out': ''})
        # print(days_in_month)
        return render(request, 'html/home.html', {'days_in_month': days_in_month, 'row_classes': row_classes})
    return redirect('web:logout')
