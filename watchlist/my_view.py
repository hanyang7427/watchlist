# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, redirect, flash
from flask import jsonify
from watchlist import app, db

from watchlist.my_models import Stage,Topic,Problem,StageTopic,TopicProblem

@app.route('/suanf/stages', methods=['GET'])
def get_stages():
    result = Stage.query.all()
    return jsonify([x.as_dict() for x in result])

@app.route('/suanf/topics', methods=['GET'])
def get_topics():
    if request.args.get('stageID'):
        res = StageTopic.query.filter_by(stage_id=request.args.get('stageID'))
        return jsonify([x.as_dict() for x in res])
    res = StageTopic.query.all()
    return jsonify([x.as_dict() for x in res])

@app.route('/suanf/problems', methods=['GET'])
def get_problems():
    if request.args.get('topicID'):
        res = TopicProblem.query.filter_by(topic_id=request.args.get('topicID'))
        return jsonify([x.as_dict() for x in res])
    result = TopicProblem.query.all()
    return jsonify([x.as_dict() for x in result])