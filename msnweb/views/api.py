from flask import Blueprint, render_template, session, jsonify
from msnweb.forms import RegisterForm
from msnweb.MSN import MSN
from msnweb.mongo import db
from msnweb.models import Message
from msnweb.helpers import login_required
from flask import request
import json
from bson.objectid import ObjectId


bp = Blueprint(
        __name__,
        __name__,
        template_folder='templates',
        url_prefix='/api'
        )

@bp.route('/conversation/<conversation_id>', methods=['POST', 'GET'])
@bp.route('/conversation', defaults={'conversation_id': None})
@login_required
def show(conversation_id):
    messages = []
    _messages = []

    if conversation_id is not None:
        _messages = list(db.collections.find({
                'structure': '#Message',
                'conversation_id': conversation_id
            }))

    for msg in _messages:
        user = db.collections.find_one({
            'structure': '#User',
            '_id': ObjectId(msg['sender_id'])
            })
        msg['user'] = user
        messages.append(msg)

    return render_template('render_conversation.html', messages=messages)

@bp.route('/conversation/<conversation_id>/version', methods=['POST', 'GET'])
@login_required
def show_version(conversation_id):
    
    existing_conversation = db.collections.find_one({
           'structure': '#Conversation',
           '_id': ObjectId(conversation_id)
        })

    return jsonify({'version': existing_conversation['ver']})


@bp.route('/conversation/<conversation_id>/send', methods=['POST', 'GET'])
@login_required
def send(conversation_id):
    body = request.form.get('body')
    sender_id = session['user_id']

    message = Message(
                body=body,
                sender_id=sender_id,
                conversation_id=conversation_id
            )

    existing_conversation = db.collections.find_one({
           'structure': '#Conversation',
           '_id': ObjectId(conversation_id)
        })

    db.collections.update_one({
            'structure': '#Conversation',
            '_id': ObjectId(conversation_id)
            }, {'$set': {'ver' : int(existing_conversation['ver'])+1}})

    db.collections.insert_one(message.export())

    return 'OK', 200
