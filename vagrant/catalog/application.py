from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Campground, SiteReview, Base

app = Flask(__name__)

engine = create_engine('sqlite:///campgroundreview.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Show All Campgrounds
@app.route('/')
@app.route('/campground/')
def showCampgrounds():
    campgrounds = session.query(Campground).all()
    items = session.query(SiteReview).all()
    return render_template('campgrounds.html', campgrounds=campgrounds, items=items)

#Create A New Campground
@app.route('/campground/new/',methods=['GET', 'POST'])
def createCampground():
       if request.method == 'POST':
              createCampground = Campground(name=request.form['name'])
              session.add(createCampground)
              session.commit()
              return redirect(url_for('showCampgrounds'))
       else:
              return  render_template('newCampground.html')

#Edit A Campground
@app.route('/campground/<int:campground_id>/edit/', methods=['GET', 'POST'])
def editCampground(campground_id):
    editedCampground = session.query(
        Campground).filter_by(id=campground_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCampground.name = request.form['name']
            return redirect(url_for('showCampgrounds'))
    else:
        return render_template(
            'editCampground.html', campground=editedCampground)






#Delete A Campground
@app.route('/campground/<int:campground_id>/delete/', methods=['GET', 'POST'])
def deleteCampground(campground_id):
       campgroundToBeDeleted = session.query(Campground).filter_by(id=campground_id).one()
       if request.method == 'POST':
              session.delete(campgroundToBeDeleted)
              session.commit()
              return redirect(url_for('showCampgrounds', campground_id=campground_id))
       else:
              return render_template('deleteCampground.html', campground=campgroundToBeDeleted)              

             
#Show A Site Review
@app.route('/campground/<int:campground_id>/')
@app.route('/campground/<int:campground_id>/review/')
def showSiteReview(campground_id):
       campground = session.query(Campground).filter_by(id=campground_id).one()
       items = session.query(SiteReview).filter_by(campground_id=campground_id).all()
       return render_template('siteReview.html', campground=campground, items=items)

# Edit A Site Review
@app.route('/campground/<int:campground_id>/review/<int:site_id>/edit/', methods=['GET', 'POST'])
def editSiteReview(campground_id, site_id):
       editedSiteReview = session.query(SiteReview).filter_by(id=site_id).one()
       return render_template('editSiteReview.html', campground_id=campground_id, site_id=site_id, item=editedSiteReview)    

     



if __name__ == '__main__':
       #app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=5000)    