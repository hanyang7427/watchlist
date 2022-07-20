# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, redirect, flash

from watchlist import app, db

from watchlist.my_models import Stage,Topic,Problem,StageTopic,TopicProblem

@app.route('/suanf/text', methods=['GET', 'POST'])
def suanfa():
    if request.method == 'GET':
        Problem.query.filter_by(id='010101').firts()
        return 1
    return 1
