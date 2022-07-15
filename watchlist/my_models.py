# coding: utf-8
from sqlalchemy import Column, Index, String, Table
from sqlalchemy.dialects.mysql import INTEGER
from watchlist import db


from watchlist import db




class Fact(db.Model):
    __tablename__ = 'facts'

    start_time = Column(String(1), primary_key=True, nullable=False)
    end_time = Column(String(1), primary_key=True, nullable=False)
    problem_id = Column(INTEGER(11))



class Problem(db.Model):
    __tablename__ = 'problem'
    __table_args__ = {'comment': '问题'}

    id = Column(String(10), primary_key=True)
    name = Column(String(100), unique=True)


class Stage(db.Model):
    __tablename__ = 'stage'
    __table_args__ = {'comment': '阶段'}

    id = Column(String(10), primary_key=True)
    name = Column(String(50), nullable=False)


class StageTopic(db.Model):
    __tablename__ = 'stage_topic'
    __table_args__ = {'comment': '阶段和话题'}

    stage_id = Column(String(10), primary_key=True, nullable=False)
    topic_id = Column(String(10), primary_key=True, nullable=False)


class Topic(db.Model):
    __tablename__ = 'topic'
    __table_args__ = {'comment': '主题'}

    id = Column(String(10), primary_key=True)
    name = Column(String(50), unique=True)


class TopicProblem(db.Model):
    __tablename__ = 'topic_problem'
    __table_args__ = {'comment': '话题和问题对应'}

    topic_id = Column(String(10), primary_key=True, nullable=False)
    problem_id = Column(String(10), primary_key=True, nullable=False)



print('my_models.py executed')