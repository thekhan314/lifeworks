from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import EntryForm



@app.route('/', methods = ['GET','POST'])
def index():

    form = EntryForm()

    if form.validate_on_submit():
        flash('New Entry: {}'.format(
            form.entry.data))
        return redirect(url_for('index'))

    return render_template('entry.html', form=form)

    