class Instance:
    # 3 dev / 5 - stage / 7 - alpha / 10 - prod
    _INSTANCE_PORTAL = 'dev'
    _INSTANCE_ADMIN_PANEL = '3'
    BASE_PORTAL_URL = 'https://portal-' + _INSTANCE_PORTAL + 'interlir.ninja'
    BASE_ADMIN_PANEL_URL = 'http://10.10.206.' + _INSTANCE_ADMIN_PANEL + ':8081/admin/login/'




class URL:
    LOGIN_URL = Instance.BASE_PORTAL_URL + '/login'
    ADD_BUSINESS_ACCOUNT_URL = Instance.BASE_PORTAL_URL + '/organization/add'
