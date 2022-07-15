# -*- coding: utf-8 -*-
import click

from watchlist import app, db
from watchlist.models import User, Movie
from watchlist.my_models import Stage,Topic,Problem,StageTopic,TopicProblem

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    name = 'Grey Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user."""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)
    else:
        click.echo('Creating user...')
        user = User(username=username, name='Admin')
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('Done.')


@app.cli.command()
def gen():
    """Generate fake data."""
    db.drop_all()
    db.create_all()
    import os
    def x(d):
        for id1,x in enumerate([name for name in os.listdir(d) if os.path.isdir(os.path.join(d,name)) & (not name.startswith('__')) & (not name.startswith('.'))]):
            id11 = str((id1+1)).zfill(2)
            stage = Stage(name=x,id=id11)
            db.session.add(stage)
            for y in [n for n in os.listdir(os.path.join(d,x)) if os.path.isdir(os.path.join(d,x,n)) & (not n.startswith('__')) & (not n.startswith('.'))]:
                for id2,z in enumerate([a for a in os.listdir(os.path.join(d,x,y)) if os.path.isdir(os.path.join(d,x,y,a)) & (not a.startswith('__')) & (not a.startswith('.'))]):
                    id22 = id11+str((id2+1)).zfill(2)
                    topic = Topic(name=z,id=id22)
                    db.session.add(topic)
                    stage_topic = StageTopic(stage_id=id11,topic_id=id22)
                    db.session.add(stage_topic)
                    for id3,l in enumerate([b for b in os.listdir(os.path.join(d,x,y,z)) if os.path.isfile(os.path.join(d,x,y,z,b)) & (b.endswith('.ipynb'))]):
                        id33 = id22+str((id3+1)).zfill(2)
                        problem = Problem(name=l,id=id33)
                        db.session.add(problem)
                        topic_problem = TopicProblem(topic_id=id22,problem_id=id33)
                        db.session.add(topic_problem)
                    
    x(os.path.join(os.getcwd(),'suanfa'))
    # print(os.path.join(os.getcwd(),'suanfa'))
    db.session.commit()
    click.echo('Done.')

print('commands.py executed')
