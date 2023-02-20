from .control_panel.control_items import extended_page_regions, extended_item_list, extended_item
from .control_panel.control_black_list import extended_black_list, extended_black_list_page, extended_black_list_add
from .control_panel.control_reports import extended_reports, extended_report_page
from django.shortcuts import render


def extend_access(request):
    return render(request, './advanced_admin/extended_page.html')
