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
    return render_template( 'pages/dashboard.html', segment='analytics', parent='dashboard')
  except TemplateNotFound:
    return render_template('pages/dashboard.html'), 404


# Pages 
@app.route('/pages/icons')
def pages_icons():
  return render_template('pages/icons.html', segment='icons', parent='pages')

@app.route('/pages/map')
def pages_map():
  return render_template('pages/map.html', segment='map', parent='pages')

@app.route('/pages/notifications/')
def pages_notifications():
  return render_template('pages/notifications.html', segment='notifications', parent='pages')

@app.route('/pages/rtl/')
def pages_rtl():
  return render_template('pages/rtl.html', segment='rtl', parent='pages')

@app.route('/pages/tables/')
def pages_tables():
  return render_template('pages/tables.html', segment='tables', parent='pages')

@app.route('/pages/typography/')
def pages_typography():
  return render_template('pages/typography.html', segment='typography', parent='pages')

@app.route('/pages/upgrade/')
def pages_upgrade():
  return render_template('pages/upgrade.html', segment='upgrade', parent='pages')

@app.route('/pages/user/')
def pages_user():
  return render_template('pages/user.html', segment='user', parent='pages')

# Registration 

@app.route('/registration/logged_out/')
def registration_logged_out():
  return render_template('registration/logged_out.html', segment='logged_out', parent='registration')

@app.route('/registration/password_change_done/')
def registration_password_change_done():
  return render_template('registration/password_change_done.html', segment='password_change_done', parent='registration')

@app.route('/registration/password_change_form/')
def registration_password_change_form():
  return render_template('registration/password_change_form.html', segment='password_change_form', parent='registration')

# Accounts 

@app.route('/accounts/auth-signin/')
def accounts_signin():
  return render_template('accounts/auth-signin.html', segment='signin', parent='accounts')

@app.route('/accounts/auth-signup/')
def accounts_signup():
  return render_template('accounts/auth-signup.html', segment='signup', parent='accounts')

@app.route('/accounts/forgot-password/')
def accounts_forgot_password():
  return render_template('accounts/forgot-password.html', segment='forgot-password', parent='accounts')

@app.route('/accounts/password-change/')
def accounts_password_change():
  return render_template('accounts/password_change.html', segment='password-change-done', parent='accounts')

@app.route('/accounts/password-change-done/')
def accounts_password_change_done():
  return render_template('accounts/password_change_done.html', segment='password-change-done', parent='accounts')

@app.route('/accounts/password-reset-complete/')
def accounts_password_reset_complete():
  return render_template('accounts/password_reset_complete.html', segment='password-reset-complete', parent='accounts')

@app.route('/accounts/password-reset-done/')
def accounts_password_reset_done():
  return render_template('accounts/password_reset_done.html', segment='password-reset-done', parent='accounts')

@app.route('/accounts/recover-password/')
def accounts_recover_password():
  return render_template('accounts/recover-password.html', segment='recover-password', parent='accounts')


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