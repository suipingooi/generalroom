def trolley_items(request):
    trolley = request.session.get('basket', {})
    return {
        'basket': trolley,
        'num_items': len(trolley)
    }
