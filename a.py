# coding: utf-8
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Fact(Base):
    __tablename__ = 'facts'

    start_time = Column(String(1), primary_key=True, nullable=False)
    end_time = Column(String(1), primary_key=True, nullable=False)
    problem_id = Column(INTEGER(11))


class Movie(Base):
    __tablename__ = 'movie'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(60))
    year = Column(String(4))


class Problem(Base):
    __tablename__ = 'problem'
    __table_args__ = {'comment': '问题'}

    id = Column(String(10), primary_key=True)
    name = Column(String(100), unique=True)


class Stage(Base):
    __tablename__ = 'stage'
    __table_args__ = {'comment': '阶段'}

    id = Column(String(10), primary_key=True)
    name = Column(String(50), nullable=False)


class StageTopic(Base):
    __tablename__ = 'stage_topic'
    __table_args__ = {'comment': '阶段和话题'}

    topic_id = Column(INTEGER(11), primary_key=True, nullable=False)


class Topic(Base):
    __tablename__ = 'topic'
    __table_args__ = {'comment': '主题'}

    id = Column(String(10), primary_key=True)
    name = Column(String(50), unique=True)


class TopicProblem(Base):
    __tablename__ = 'topic_problem'
    __table_args__ = {'comment': '话题和问题对应'}

    topic_id = Column(INTEGER(11), primary_key=True, nullable=False)
    problem_id = Column(INTEGER(11), primary_key=True, nullable=False)


class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(20))
    username = Column(String(20))
    password_hash = Column(String(128))
