from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.http import HttpResponse
from home.models import Photo, Person, PersonGallery
import re

import string
import random

# ReGEx required for getting photo name
post_type = re.compile(r"static/images/(.*)")

# Required for image processing
import face_recognition
import cv2
from sklearn.cluster import DBSCAN
import numpy as np
import re

# Required for downloading
import os
import zipfile
import tempfile, zipfile
from django.http import HttpResponse
from wsgiref.util import FileWrapper

# for checking face simmilarity
import scipy.spatial.distance as dist

