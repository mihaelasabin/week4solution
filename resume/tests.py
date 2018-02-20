"""
week4solution/resumt/tests.py
Feb 19, 2018
"""

import datetime

from django.test import TestCase
from .models import Resume, Education, Experience

class ResumeTestCases(TestCase):

    def setUp(self):
        today = datetime.datetime.today()
        resume1 = Resume.objects.create(
            first_name='jon', last_name='shallow'
        )
        experience1 = Experience.objects.create(
            resume=resume1,
            title='Instructor Pilot',
            location='US Army',
            start_date=today,
            end_date=today,
            description='Murica!'
        )
        education1 = Education.objects.create(
            resume=resume1,
            institution_name='H60A/L/M IPC',
            degree='Certification',
            major='Instructor',
            gpa=4.0
        )

    def test_instances(self):
        """
        Check if objects are saved in test database and 
        of the correct type
        """
        resume1 = Resume.objects.first()
        self.assertIsInstance(resume1, Resume)
        education1 = Education.objects.first()
        self.assertIsInstance(education1, Education)
        experience1 = Experience.objects.first()
        self.assertIsInstance(experience1, Experience)

    def test_get_full_name(self):
        resume1 = Resume.objects.first()
        actual = resume1.get_full_name()
        expected = "jon shallow"
        self.assertEqual(actual, expected)

    def test_get_last_name_first_name(self):
        resume1 = Resume.objects.first()
        actual = resume1.get_last_name_first_name()
        expected = "shallow jon"
        self.assertEqual(actual, expected)

    def test_get_experience(self):
        """
        get_experience is a wrapper function to make it a bit easier
        to get the experience_set of a given resume. Test that
        resume_object.get_experience === resume_object.experience_set.all()
        """
        resume1 = Resume.objects.first()
        actual = list(resume1.get_experience())
        expected = list(resume1.experience_set.all())
        self.assertEqual(actual, expected)

    def test_get_education(self):
        """
        get_education is a wrapper function to make it a bit easier
        to get the education_set of a given resume. Test that
        resume_object.get_education === resume_object.education_set.all()
        """
        resume1 = Resume.objects.first()
        actual = list(resume1.get_education())
        expected = list(resume1.education_set.all())
        self.assertEqual(actual, expected)
