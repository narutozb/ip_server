import json

from django.http import JsonResponse
from django.shortcuts import render


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 获取真实IP
    else:
        ip = request.META.get('REMOTE_ADDR')  # 获取代理IP

    return JsonResponse({'ip': ip})


def get_client_meta_data(request):
    result = {}
    proxy_indicators = [
        'HTTP_VIA',
        'HTTP_X_FORWARDED_FOR',
        'HTTP_FORWARDED',
        'HTTP_X_FORWARDED',
        'HTTP_X_CLUSTER_CLIENT_IP',
        'HTTP_FORWARDED_FOR',
        'HTTP_FORWARDED_FOR_IP',
        'REMOTE_ADDR',
    ]
    meta = request.META
    for i in proxy_indicators:
        data = meta.get(i)
        if data:
            result[i] = data

    return JsonResponse({'meta': result})
