from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

app = Flask(__name__)

# Configure PostgreSQL connection
DATABASE_URL = "postgresql://postgres:Jblingzify007!@database-3.cncfqwwnagxs.eu-west-2.rds.amazonaws.com:5432/postgres"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Mirror(Base):
    __tablename__ = 'mirrors'
    id = Column(String, primary_key=True)
    word = Column(String)
    mirrored_word = Column(String)

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

@app.route('/api/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/api/mirror')
def mirror():
    word = request.args.get('word', '')
    mirrored_word = word.swapcase()[::-1]

    # Save (word, mirroredWord) pair to database
    session = Session()
    new_mirror = Mirror(id=str(uuid.uuid4()), word=word, mirrored_word=mirrored_word)
    session.add(new_mirror)
    session.commit()
    session.close()

    return jsonify({"transformed": mirrored_word})

if __name__ == '__main__':
    app.run(port=4004)

