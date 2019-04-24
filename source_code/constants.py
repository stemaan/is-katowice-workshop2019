
__all__ = ['RADIUS', 'TAG', 'QUERY_TEMPLATE', 'NTH_POINT']

RADIUS = 10000
TAG = 'fuel'
QUERY_TEMPLATE = '(node["amenity"="{tag}"](around:{radius},{lat},{lon}););out body;'
NTH_POINT = 500
