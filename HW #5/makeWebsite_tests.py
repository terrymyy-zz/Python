from makeWebsite import *
import unittest

class TestmakeWebsite(unittest.TestCase):

    def setUp(self):
        self.text = ''
        self.tag  = ''
        self.list1 = []
        self.filename = ''

    def testread_from_file(self):
        '''test whether it can read from the file'''
        self.filename = 'resume.txt'
        self.assertTrue(len(read_from_file(self.filename)) == 37)

    def testis_file(self):
        '''test whether it can find the file'''
        self.filename = 'resume.txt'
        self.assertTrue(is_file(self.filename))
        self.filename1 = 'asdf.txt'
        self.assertFalse(is_file(self.filename1))

    def testdetect_name(self):
        '''test whether it can detect name'''
        self.text = ['Yaoyu Ma','mayaoyu@.edu','terrymyy@gmail.com']
        self.assertEqual(detect_name(self.text), 'Yaoyu Ma')
        self.text1 = ['aYaoyu Ma','mayaoyu@.edu','terrymyy@gmail.com']
        self.assertRaises(ValueError)

    def testdetect_email(self):
        '''test whether it can detect email'''
        self.text = ['terrymyy@','mayaoyu@.edu','terrymyy@gmail.com']
        self.assertEqual(detect_email(self.text), 'terrymyy@gmail.com')
        self.text1 = ['te.com','mayaoyu.edu','teru@A.edu','terrymyy@gmail.edu']
        self.assertEqual(detect_email(self.text1), 'terrymyy@gmail.edu')

    def testdetect_courses(self):
        '''test whether it can detect courses'''
        self.text = ['Courses :- CIT590,MEAM513, MEAM521']
        self.assertEqual(detect_courses(self.text), 'CIT590,MEAM513, MEAM521')

    def testdetect_projects(self):
        '''test whether it can detect projects'''
        self.text = ['Projects','project1','project2','-------------------']
        self.assertEqual(detect_projects(self.text), ['project1','project2'])

    def testdetect_education(self):
        '''test whether it can detect education'''
        self.text = ['asdf','Bachelor degree','University of Pennsylvania in Master','university of beijing']
        self.assertEqual(detect_education(self.text), ['Bachelor degree','University of Pennsylvania in Master','university of beijing'])

    def testsurround_block(self):
        '''test whether it can surround the content to create a block'''
        self.tag  = 'p'
        self.text = 'asdf'
        self.assertEqual(surround_block(self.tag, self.text), '<p>\nasdf\n</p>')
        self.tag  = 'ul'
        self.text = 'qwewerasdfag'
        self.assertEqual(surround_block(self.tag, self.text), '<ul>\nqwewerasdfag\n</ul>')

    def testcreate_html(self):
        '''test whether it can create a html format string'''
        self.name      = 'Yaoyu Ma'
        self.email     = 'mayaoyu@seas.upenn.edu'
        self.courses   = 'CIT590, MEAM513, MEAM521'
        self.projects  = ['asdfasdf','zxczxc']
        self.education = ['qwe','ert']
        self.assertEqual(create_html(self.name,self.email, self.courses, self.projects, self.education), '<div id="page-wrap">\n\n<div>\n<h1>\nYaoyu Ma\n</h1>\n<p>\nmayaoyu@seas.upenn.edu\n</p>\n</div>\n<div>\n<h2>\nEducation\n</h2>\n<ul>\n<li>\nqwe\n</li>\n<li>\nert\n</li>\n</ul>\n</div>\n<div>\n<h2>\nProjects\n</h2>\n<ul>\n<li>\n<p>\nasdfasdf\n</p>\n</li>\n<li>\n<p>\nzxczxc\n</p>\n</li>\n</ul>\n</div>\n<div>\n<h3>\nCourses\n</h3>\n<span>\nCIT590, MEAM513, MEAM521\n</span>\n</div>\n</div>\n</body>\n</html>')

    def testcreate_par(self):
        '''test whether it can create a html paragraph'''
        self.list1 = ['asdf','zxcv','qwer']
        self.assertEqual(create_par(self.list1), ['<p>\nasdf\n</p>','<p>\nzxcv\n</p>','<p>\nqwer\n</p>'])

    def testcreate_ul(self):
        '''test whether it can create a html unordered list'''
        self.list1 = ['asdf','zxcv','qwer']
        self.assertEqual(create_ul(self.list1), '<ul>\n<li>\nasdf\n</li>\n<li>\nzxcv\n</li>\n<li>\nqwer\n</li>\n</ul>')

    def testcreate_div(self):
        '''test whether it can create a html division'''
        self.list1 = ['<h1>h1</h1>','<ul><li>asdf</li><li>zxcv</li></ul>']
        self.assertEqual(create_div(self.list1[0],self.list1[1]), '<div>\n<h1>h1</h1>\n<ul><li>asdf</li><li>zxcv</li></ul>\n</div>')
      
unittest.main()
