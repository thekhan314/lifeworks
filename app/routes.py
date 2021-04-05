from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import EntryForm
from app.models import Entry


@app.route('/', methods = ['GET','POST'])
def index():

    form = EntryForm()

    if form.validate_on_submit():
        flash('New Entry: {}'.format(
            form.entry.data))

        entry = Entry(
            entry=form.entry.data,
            project=form.project.data,
            notes= form.notes.data
        )

        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('index'))
    
    entries = Entry.query.all()


    return render_template('entry.html', form=form, data = entries)

    