from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import StudyRoom, RoomMember, StudySession, RoomActivityLog, db
from sqlalchemy import func

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    # Rooms created by user
    created_rooms = StudyRoom.query.filter_by(created_by=current_user.id).all()
    
    # Rooms joined by user (including those they created if they are members)
    memberships = RoomMember.query.filter_by(user_id=current_user.id).all()
    joined_room_ids = [m.room_id for m in memberships]
    joined_rooms = StudyRoom.query.filter(StudyRoom.id.in_(joined_room_ids)).all() if joined_room_ids else []

    # Statistics
    total_sessions = StudySession.query.filter_by(started_by=current_user.id, status='completed').count()
    total_time = db.session.query(func.sum(StudySession.duration_minutes)).filter_by(started_by=current_user.id, status='completed').scalar() or 0
    
    # Recent activity
    recent_activities = RoomActivityLog.query.filter(
        (RoomActivityLog.user_id == current_user.id) | 
        (RoomActivityLog.room_id.in_(joined_room_ids))
    ).order_by(RoomActivityLog.created_at.desc()).limit(10).all()

    return render_template('dashboard.html', 
                           created_rooms=created_rooms, 
                           joined_rooms=joined_rooms,
                           total_sessions=total_sessions,
                           total_time=total_time,
                           recent_activities=recent_activities)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)
