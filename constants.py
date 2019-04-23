__all__ = ['RADIUS', 'TAG', 'QUERY_TEMPLATE']

RADIUS = 2000
TAG = 'fuel'
QUERY_TEMPLATE = '(node["amenity"="{tag}"](around:{radius},{lat},{lon}););out body;'
NTH_POINT = 500
