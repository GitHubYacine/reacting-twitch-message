from database.db_config import db, app

reaction_messages = [
        {"message_id": "1", "emoji": "", "count": 0},
    ]

reaction_emojis = {
    "1": "🧨",
    "2": "🤝🏽",
    "3": "🧡"
}

class Reaction_message(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False)
    emoji = db.Column(db.Integer, db.ForeignKey("emojis.id"), nullable=False)

class Emojis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emoji = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()
    for reaction_message in reaction_messages:
        messages = Reaction_message(message_id=reaction_message["message_id"],count=reaction_message["count"], emoji=reaction_message["emoji"])
        db.session.add(messages)
    for key, value in reaction_emojis.items():
        emojis = Emojis(id=key, emoji=value)
        db.session.add(emojis)
    db.session.commit()