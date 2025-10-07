from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import uuid
import cv2
import numpy as np
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///deepfake.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    videos = db.relationship('Video', backref='user', lazy=True)

# Video model
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    result = db.Column(db.String(50))
    confidence = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('home'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password1')
        password2 = request.form.get('password2')

        if password != password2:
            flash('Passwords do not match')
            return redirect(url_for('signup'))

        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('signup'))

        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return redirect(url_for('signup'))

        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@app.route('/validate', methods=['GET', 'POST'])
@login_required
def validate():
    if request.method == 'POST':
        if 'video_file' not in request.files:
            flash('No video file uploaded')
            return redirect(request.url)
            
        video_file = request.files['video_file']
        if video_file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if video_file:
            # Generate unique filename
            filename = str(uuid.uuid4()) + os.path.splitext(video_file.filename)[1]
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            video_file.save(filepath)

            # Here you would normally call your deepfake detection model
            # For demonstration, using random result
            import random
            is_deepfake = random.choice([True, False])
            confidence = random.uniform(60, 99)

            # Save video analysis to database
            video = Video(
                filename=filename,
                result='Deepfake' if is_deepfake else 'Authentic',
                confidence=confidence,
                user_id=current_user.id
            )
            db.session.add(video)
            db.session.commit()

            return render_template('predict.html', 
                                prediction='Deepfake' if is_deepfake else 'Authentic',
                                confidence=confidence,
                                unique_hash_id=filename)

    return render_template('validate.html')

# API routes for statistics
@app.route('/api/stats')
def get_stats():
    total_videos = Video.query.count()
    deepfake_count = Video.query.filter_by(result='Deepfake').count()
    authentic_count = Video.query.filter_by(result='Authentic').count()
    
    return jsonify({
        'total_videos': total_videos,
        'deepfake_count': deepfake_count,
        'authentic_count': authentic_count
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 