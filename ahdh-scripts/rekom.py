#!/usr/bin/python
# recommendation engine experiment

from math import (
    pow
)

data = {
    "Jack Matthews": {
        "Lady in the Water": 3.0,
        "Snakes on a Plane": 4.0,
        "You, Me and Dupree": 3.5,
        "Superman Returns": 5.0,
        "The Night Listener": 3.0},
    "Mick LaSalle": {
        "Lady in the Water": 3.0,
        "Snakes on a Plane": 4.0,
        "Just My Luck": 2.0,
        "Superman Returns": 3.0,
        "You, Me and Dupree": 2.0,
        "The Night Listener": 3.0},
    "Claudia Puig": {
        "Snakes on a Plane": 3.5,
        "Just My Luck": 3.0,
        "You, Me and Dupree": 2.5,
        "Superman Returns": 4.0,
        "The Night Listener": 4.5},
    "Lisa Rose": {
        "Lady in the Water": 2.5,
        "Snakes on a Plane": 3.5,
        "Just My Luck": 3.0,
        "Superman Returns": 3.5,
        "The Night Listener": 3.0,
        "You, Me and Dupree": 2.5},
    "Toby": {
        "Snakes on a Plane": 4.5,
        "Superman Returns": 4.0,
        "You, Me and Dupree": 1.0},
    "Gene Seymour": {
        "Lady in the Water": 3.0,
        "Snakes on a Plane": 3.5,
        "Just My Luck": 1.5,
        "Superman Returns": 5.0,
        "You, Me and Dupree": 3.5,
        "The Night Listener": 3.0},
    "Michael Phillips": {
        "Lady in the Water": 2.5,
        "Snakes on a Plane": 3.0,
        "Superman Returns": 3.5,
        "The Night Listener": 4.0}}

for user in data.keys():
    for users in data.keys():
        if users is not user:
            score = 1/(1+sum([pow(data[user][item] - data[users][item], 2) for item in data[user] if item in data[users]]))
            print user, users, "skors: ", score
