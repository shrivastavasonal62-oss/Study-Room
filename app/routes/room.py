from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import StudyRoom, RoomMember, StudySession, RoomMessage, RoomActivityLog, db
from datetime import datetime

room = Blueprint('room', __name__)

@room.route('/room/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        subject = request.form.get('subject')
        visibility = request.form.get('visibility', 'public')

        new_room = StudyRoom(name=name, description=description, 
                             subject=subject, visibility=visibility, 
                             created_by=current_user.id)
        db.session.add(new_room)
        db.session.flush() # Get the ID before commit

        # Add creator as admin member
        member = RoomMember(room_id=new_room.id, user_id=current_user.id, role='admin')
        db.session.add(member)

        # Log activity
        log = RoomActivityLog(room_id=new_room.id, user_id=current_user.id, 
                              activity_type='room_created', details=f"Room '{name}' created")
        db.session.add(log)
        
        db.session.commit()
        flash('Study room created successfully!', 'success')
        return redirect(url_for('room.detail', room_id=new_room.id))

    return render_template('room/create.html')

@room.route('/room/join', methods=['GET', 'POST'])
@login_required
def join():
    if request.method == 'POST':
        invite_code = request.form.get('invite_code')
        target_room = StudyRoom.query.filter_by(invite_code=invite_code).first()

        if not target_room:
            flash('Invalid invite code.', 'danger')
            return redirect(url_for('room.join'))

        # Check if already a member
        existing_member = RoomMember.query.filter_by(room_id=target_room.id, user_id=current_user.id).first()
        if existing_member:
            flash('You are already a member of this room.', 'info')
            return redirect(url_for('room.detail', room_id=target_room.id))

        # Join room
        new_member = RoomMember(room_id=target_room.id, user_id=current_user.id)
        db.session.add(new_member)

        # Log activity
        log = RoomActivityLog(room_id=target_room.id, user_id=current_user.id, 
                              activity_type='user_joined', details=f"{current_user.name} joined the room")
        db.session.add(log)

        db.session.commit()
        flash(f'Joined room: {target_room.name}', 'success')
        return redirect(url_for('room.detail', room_id=target_room.id))

    return render_template('room/join.html')

@room.route('/room/<int:room_id>')
@login_required
def detail(room_id):
    target_room = StudyRoom.query.get_or_404(room_id)
    
    # Check if user is a member
    member = RoomMember.query.filter_by(room_id=room_id, user_id=current_user.id).first()
    if not member and target_room.visibility == 'private':
        flash('This is a private room. You need an invite to join.', 'warning')
        return redirect(url_for('main.dashboard'))

    # If public and not a member, auto-join or show preview? Let's auto-join for simplicity
    if not member:
        member = RoomMember(room_id=room_id, user_id=current_user.id)
        db.session.add(member)
        log = RoomActivityLog(room_id=room_id, user_id=current_user.id, 
                              activity_type='user_joined', details=f"{current_user.name} joined the room")
        db.session.add(log)
        db.session.commit()

    messages = RoomMessage.query.filter_by(room_id=room_id).order_by(RoomMessage.created_at.asc()).all()
    members = RoomMember.query.filter_by(room_id=room_id).all()
    active_session = StudySession.query.filter_by(room_id=room_id, status='active').first()
    history = RoomActivityLog.query.filter_by(room_id=room_id).order_by(RoomActivityLog.created_at.desc()).limit(20).all()

    return render_template('room/detail.html', 
                           room=target_room, 
                           messages=messages, 
                           members=members, 
                           active_session=active_session,
                           history=history)

@room.route('/room/<int:room_id>/session/start', methods=['POST'])
@login_required
def start_session(room_id):
    # Check if there's already an active session
    active = StudySession.query.filter_by(room_id=room_id, status='active').first()
    if active:
        flash('A session is already active in this room.', 'info')
    else:
        new_session = StudySession(room_id=room_id, started_by=current_user.id)
        db.session.add(new_session)
        
        log = RoomActivityLog(room_id=room_id, user_id=current_user.id, 
                              activity_type='session_started', details=f"Study session started by {current_user.name}")
        db.session.add(log)
        db.session.commit()
        flash('Study session started!', 'success')
    
    return redirect(url_for('room.detail', room_id=room_id))

@room.route('/room/<int:room_id>/session/end', methods=['POST'])
@login_required
def end_session(room_id):
    active = StudySession.query.filter_by(room_id=room_id, status='active').first()
    if active:
        active.end_time = datetime.utcnow()
        active.status = 'completed'
        
        # Calculate duration
        duration = active.end_time - active.start_time
        active.duration_minutes = int(duration.total_seconds() / 60)
        
        log = RoomActivityLog(room_id=room_id, user_id=current_user.id, 
                              activity_type='session_ended', 
                              details=f"Study session ended. Duration: {active.duration_minutes} mins")
        db.session.add(log)
        db.session.commit()
        flash(f'Session ended. You studied for {active.duration_minutes} minutes.', 'success')
    else:
        flash('No active session found.', 'warning')
    
    return redirect(url_for('room.detail', room_id=room_id))
