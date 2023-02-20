from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from handlers.models import Report
# Create your views here.


@permission_required('handlers.control_reports', login_url='login')
def extended_reports(request):
    reports = Report.objects.all()
    return render(request, './advanced_admin/extend_reports/extended_reports.html', {'reports': reports})


@permission_required('handlers.control_reports', login_url='login')
def extended_report_page(request, report_id):
    report = Report.objects.get(id=report_id)
    if request.method == 'POST':
        report.delete()
        messages.success(request, 'Жалоба успешно удалена')
        return redirect('extended_reports')

    return render(request, './advanced_admin/extend_reports/extended_report_page.html', {'report': report})
