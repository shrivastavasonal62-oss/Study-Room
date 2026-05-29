from datetime import datetime
from flask_login import UserMixin
from app import db, login_manager
import uuid

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    created_rooms = db.relationship('StudyRoom', backref='creator', lazy=True)
    memberships = db.relationship('RoomMember', backref='user', lazy=True)
    sessions = db.relationship('StudySession', backref='user', lazy=True)
    messages = db.relationship('RoomMessage', backref='user', lazy=True)
    activities = db.relationship('RoomActivityLog', backref='user', lazy=True)

class StudyRoom(db.Model):
    __tablename__ = 'study_rooms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    subject = db.Column(db.String(100))
    visibility = db.Column(db.String(20), default='public') # public, private
    invite_code = db.Column(db.String(10), unique=True, default=lambda: str(uuid.uuid4())[:8])
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    members = db.relationship('RoomMember', backref='room', lazy=True, cascade="all, delete-orphan")
    sessions = db.relationship('StudySession', backref='room', lazy=True, cascade="all, delete-orphan")
    messages = db.relationship('RoomMessage', backref='room', lazy=True, cascade="all, delete-orphan")
    activities = db.relationship('RoomActivityLog', backref='room', lazy=True, cascade="all, delete-orphan")

class RoomMember(db.Model):
    __tablename__ = 'room_members'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('study_rooms.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role = db.Column(db.String(20), default='member') # admin, member
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

class StudySession(db.Model):
    __tablename__ = 'study_sessions'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('study_rooms.id'), nullable=False)
    started_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    duration_minutes = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), default='active') # active, completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class RoomMessage(db.Model):
    __tablename__ = 'room_messages'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('study_rooms.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class RoomActivityLog(db.Model):
    __tablename__ = 'room_activity_logs'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('study_rooms.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    activity_type = db.Column(db.String(50), nullable=False) # room_created, user_joined, session_started, session_ended
    details = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
