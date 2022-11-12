from flask import Flask, render_template, render_template, redirect, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pets_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)
db.create_all()


# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)




@app.route("/")
def homepage():
    """Show homepage of pets."""

    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()
    """if form is valid add pet to homepage - otherwisse return back to add pet form"""
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} has been added!")
        return redirect(url_for('homepage'))

    else:
        return render_template("pet_add_form.html", form=form)

@app.route("/<int:pet_id>", methods=['GET', 'POST'])
def edit_pet(pet_id):
    """to edit pet and add update the pets information on homepage"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} updated!")
        return redirect(url_for('homepage'))

    else:
        return render_template('pet_edit_form.html', form=form, pet=pet)
