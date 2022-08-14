from flask import Blueprint, render_template, request, flash

views = Blueprint('views',__name__)

@views.route('/pump')
def pump():
    
    
    return render_template('pump.html')

@views.route('/water')
def water():
    
    
    return render_template('water.html')

@views.route('/solar')
def solar():
    
    
    return render_template('solar.html')