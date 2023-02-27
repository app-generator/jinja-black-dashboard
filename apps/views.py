# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request, redirect
from jinja2  import TemplateNotFound

# App modules
from apps import app

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/')
def index():
  try:
    return render_template( 'pages/index.html', segment='analytics', parent='dashboard')
  except TemplateNotFound:
    return render_template('pages/index.html'), 404


# Dashboard
@app.route('/')
def analytics():
  return render_template('pages/dashboards/analytics.html', segment='analytics', parent='dashboard')

@app.route('/discover/')
def discover():
  return render_template('pages/dashboards/discover.html', segment='discover', parent='dashboard')

@app.route('/sales/')
def sales():
  return render_template('pages/dashboards/sales.html', segment='sales', parent='dashboard')

@app.route('/automotive/')
def automotive():
  return render_template('pages/dashboards/automotive.html', segment='automotive', parent='dashboard')

@app.route('/smart-home/')
def smart_home():
  return render_template('pages/dashboards/smart-home.html', segment='smart_home', parent='dashboard')


# Pages -> Profile

@app.route('/profile-overview/')
def profile_overview():
  return render_template('pages/pages/profile/overview.html', parent='pages', sub_parent='profile', segment='profile_overview')

@app.route('/projects/')
def all_projects():
  return render_template('pages/pages/profile/projects.html', parent='pages', sub_parent='profile', segment='projects')

@app.route('/messages/')
def messages():
  return render_template('pages/pages/profile/messages.html', parent='pages', sub_parent='profile', segment='messages')


# Pages -> Users
@app.route('/reports/')
def reports():
  return render_template('pages/pages/users/reports.html', parent='pages', sub_parent='users', segment='reports')

@app.route('/new-user/')
def new_user():
  return render_template('pages/pages/users/new-user.html', parent='pages', sub_parent='users', segment='new_user')


# Pages -> Accounts
@app.route('/settings/')
def settings():
  return render_template('pages/pages/account/settings.html', parent='pages', sub_parent='accounts', segment='settings')

@app.route('/billing/')
def billing():
  return render_template('pages/pages/account/billing.html', parent='pages', sub_parent='accounts', segment='billing')

@app.route('/invoice/')
def invoice():
  return render_template('pages/pages/account/invoice.html', parent='pages', sub_parent='accounts', segment='invoice')

@app.route('/security/')
def security():
  return render_template('pages/pages/account/security.html', parent='pages', sub_parent='accounts', segment='security')


# Pages -> Projects
@app.route('/general/')
def general():
  return render_template('pages/pages/projects/general.html', parent='pages', sub_parent='projects', segment='general')

@app.route('/timeline/')
def timeline():
  return render_template('pages/pages/projects/timeline.html', parent='pages', sub_parent='projects', segment='timeline')

@app.route('/new-project/')
def new_project():
  return render_template('pages/pages/projects/new-project.html', parent='pages', sub_parent='projects', segment='new_project')

# Pages -> VR
@app.route('/vr-default/')
def vr_default():
  return render_template('pages/pages/vr/vr-default.html', parent='pages', sub_parent='vr', segment='vr_default')

@app.route('/vr-info/')
def vr_info():
  return render_template('pages/pages/vr/vr-info.html', parent='pages', sub_parent='vr', segment='vr_info')

# Pages
@app.route('/rtl/')
def rtl():
  return render_template('pages/pages/rtl-page.html', parent='pages', segment='rtl')

@app.route('/pricing/')
def pricing():
  return render_template('pages/pages/pricing-page.html', parent='pages', segment='pricing')

@app.route('/widgets/')
def widgets():
  return render_template('pages/pages/widgets.html', parent='pages', segment='widgets')

@app.route('/charts/')
def charts():
  return render_template('pages/pages/charts.html', parent='pages', segment='charts')

@app.route('/sweet-alerts/')
def sweet_alerts():
  return render_template('pages/pages/sweet-alerts.html', parent='pages', segment='sweet_alerts')

@app.route('/notifications/')
def notifications():
  return render_template('pages/pages/notifications.html', parent='pages', segment='notifications')


# Applications
@app.route('/crm/')
def crm():
  return render_template('pages/applications/crm.html', parent='applications', segment='crm')
  
@app.route('/kanban/')
def kanban():
  return render_template('pages/applications/kanban.html', parent='applications', segment='kanban')

@app.route('/wizard/')
def wizard():
  return render_template('pages/applications/wizard.html', parent='applications', segment='wizard')

@app.route('/datatables/')
def datatables():
  return render_template('pages/applications/datatables.html', parent='applications', segment='datatables')

@app.route('/calendar/')
def calendar():
  return render_template('pages/applications/calendar.html', parent='applications', segment='calendar')

@app.route('/stats/')
def stats():
  return render_template('pages/applications/stats.html', parent='applications', segment='stats')

# Ecommerce -> Products
@app.route('/new-product/')
def new_product():
  return render_template('pages/ecommerce/products/new-product.html', parent='ecommerce', sub_parent='products', segment='new_product')

@app.route('/edit-product/')
def edit_product():
  return render_template('pages/ecommerce/products/edit-product.html', parent='ecommerce', sub_parent='products', segment='edit_product')

@app.route('/product-page/')
def product_page():
  return render_template('pages/ecommerce/products/product-page.html', parent='ecommerce', sub_parent='products', segment='product_page')

@app.route('/products-list/')
def products_list():
  return render_template('pages/ecommerce/products/products-list.html', parent='ecommerce', sub_parent='products', segment='products_list')

# Ecommerce -> Orders
@app.route('/order-list/')
def order_list():
  return render_template('pages/ecommerce/orders/list.html', parent='ecommerce', sub_parent='orders', segment='order_list')

@app.route('/order-details/')
def order_details():
  return render_template('pages/ecommerce/orders/details.html', parent='ecommerce', sub_parent='orders', segment='order_details')

# Ecommerce -> Referral
@app.route('/referral/')
def referral():
  return render_template('pages/ecommerce/referral.html', parent='ecommerce', segment='referral')


# Authentication -> Login
@app.route('/accounts/basic-login/')
def basic_login():
  return render_template('accounts/signin/basic.html')

@app.route('/accounts/cover-login/')
def cover_login():
  return render_template('accounts/signin/cover.html')

@app.route('/accounts/illustration-login/')
def illustration_login():
  return render_template('accounts/signin/illustration.html')


# Authentication -> Register
@app.route('/accounts/basic-register/')
def basic_register():
  return render_template('accounts/signup/basic.html')

@app.route('/accounts/cover-register/')
def cover_register():
  return render_template('accounts/signup/cover.html')

@app.route('/accounts/illustration-register/')
def illustration_register():
  return render_template('accounts/signup/illustration.html')

# Authentication -> Lock
@app.route('/accounts/basic-lock/')
def basic_lock():
  return render_template('accounts/lock/basic.html')

@app.route('/accounts/cover-lock/')
def cover_lock():
  return render_template('accounts/lock/cover.html')

@app.route('/accounts/illustration-lock/')
def illustration_lock():
  return render_template('accounts/lock/illustration.html')

# Authentication -> Reset
@app.route('/accounts/basic-reset/')
def basic_reset():
  return render_template('accounts/reset/basic.html')

@app.route('/accounts/cover-reset/')
def cover_reset():
  return render_template('accounts/reset/cover.html')

@app.route('/accounts/illustration-reset/')
def illustration_reset():
  return render_template('accounts/reset/illustration.html')


# Authentication -> 
@app.route('/accounts/basic-verification/')
def basic_verification():
  return render_template('accounts/verification/basic.html')

@app.route('/accounts/cover-verification/')
def cover_verification():
  return render_template('accounts/verification/cover.html')

@app.route('/accounts/illustration-verification/')
def illustration_verification():
  return render_template('accounts/verification/illustration.html')

# Error
@app.route('/error/404/')
def error_404():
  return render_template('accounts/error/404.html')

@app.route('/error/500/')
def error_500():
  return render_template('accounts/error/500.html')

def logout_view():
  return redirect('/accounts/basic-login/')



def get_segment( request ): 
  try:
    segment = request.path.split('/')[-1]
    if segment == '':
      segment = 'index'
    return segment    
  except:
    return None  

# Custom Filter
@app.template_filter('replace_value')
def replace_value(value, arg):
  return value.replace(arg, ' ').title()