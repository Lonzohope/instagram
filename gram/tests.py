# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Image

class ImageTestClass(TestCase):
    def setUp(self):
        self.image= Image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))


    def test_save_method(self):
        self.image.save_images()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
