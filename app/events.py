from flask import request
from flask_socketio import emit, join_room, leave_room
from flask_login import current_user
from app import socketio, db
from app.models import RoomMessage, RoomActivityLog, User
from datetime import datetime

@socketio.on('join')
def on_join(data):
    room_id = data.get('room_id')
    if room_id:
        join_room(str(room_id))
        # We don't necessarily need to broadcast join here as we log it in the route
        # but for instant feedback we can:
        emit('status', {'msg': f'{current_user.name} has entered the room.'}, room=str(room_id))

@socketio.on('leave')
def on_leave(data):
    room_id = data.get('room_id')
    if room_id:
        leave_room(str(room_id))
        emit('status', {'msg': f'{current_user.name} has left the room.'}, room=str(room_id))

@socketio.on('send_message')
def handle_send_message(data):
    room_id = data.get('room_id')
    message_text = data.get('message')
    
    if room_id and message_text and current_user.is_authenticated:
        # Save to DB
        msg = RoomMessage(room_id=room_id, user_id=current_user.id, message=message_text)
        db.session.add(msg)
        db.session.commit()
        
        # Broadcast to room
        emit('new_message', {
            'user': current_user.name,
            'message': message_text,
            'timestamp': datetime.utcnow().strftime('%H:%M')
        }, room=str(room_id))

@socketio.on('session_update')
def handle_session_update(data):
    # This can be used to notify others when a session starts/ends via socket
    # instead of just relying on page refreshes
    room_id = data.get('room_id')
    action = data.get('action') # 'started' or 'ended'
    
    if room_id:
        emit('session_changed', {
            'user': current_user.name,
            'action': action
        }, room=str(room_id))
