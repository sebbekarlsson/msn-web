from flask import Blueprint, render_template, redirect, session
from msnweb.MSN import MSN
from msnweb.forms import LoginForm
from msnweb.helpers import login_required
from msnweb.mongo import db
from bson.objectid import ObjectId
from msnweb.models import Conversation


bp = Blueprint(
        __name__,
        __name__,
        template_folder='templates',
        url_prefix='/conversation'
        )


@bp.route('/new/<id>')
@bp.route('/',  defaults={'id': None})
@login_required
def new(id):
    chat_user = db.collections.find({
            'structure': '#User',
            '_id': ObjectId(id)
        })

    if  chat_user is None:
        return redirect('/')

    existing_convo = db.collections.find_one({
            'structure': '#Conversation',
            'user_ids' : [session['user_id'], id]
            }
                    )

    if existing_convo is not None:
        return redirect ('/conversation/{}'.format(str(existing_convo['_id'])))

    new_conversation = Conversation(
                title='New Conversation',
                user_ids=[session['user_id'], id],
                ver=0
            )
    convo = db.collections.insert_one(new_conversation.export())

    return redirect('/conversation/{}'.format(str(convo.inserted_id)))

@bp.route('/<id>')
@bp.route('/',  defaults={'id': None})
@login_required
def show(id):
    chat_user = None
    chat_user_id = None

    conversation = db.collections.find_one({
            'structure': '#Conversation',
            '_id': ObjectId(id)
        })

    if conversation is None:
        return redirect('/')

    messages = db.collections.find({
            'structure': '#Message',
            'conversation_id': ObjectId(conversation['_id'])
        })
    conversation['messages'] = messages

    for uid in conversation['user_ids']:
        if uid == session['user_id']:
            continue
        else:
            chat_user_id = uid

    if chat_user_id is None:
        chat_user_id = session['user_id']

    chat_user = db.collections.find_one({
            'structure': '#User',
            '_id': ObjectId(chat_user_id)
        })

    return render_template('chat.html',
            chat_user=chat_user,
            conversation=conversation
            )
