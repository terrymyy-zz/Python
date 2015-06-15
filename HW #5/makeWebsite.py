import string
def read_from_file(filename):
    '''Reads a file and stores data in list'''
    #Reads a file and stores each line in a list and returns list
    fileList=[]
    fo = open(filename, 'r')
    for line in fo:
        fileList.append(line)
    fo.close()
    return fileList       

def is_file(string):
    ''' It tells whether the entered file exists or not.'''
    try:
        open(string)
        return True
    except  IOError:
        return False
    
######scrape the text file for the information#######
def detect_name(text):
    '''This function detect the name of the text file'''
    # If the first letter is not uppercase, it shows an error.
    if text[0][0] in string.ascii_uppercase:
        return text[0]
    else:
        raise ValueError("The first word is not a NAME!")

def detect_email(text):
    '''This function detect the email in correct form'''
    # Only when there is @ or .com .edu and string in between starts lowercase
    for line in text:
        if ('@' in line) and ('.com' in line or '.edu' in line):
            if len(line.split('@')[1].strip('.edu.com')) != 0:
                if line.split('@')[1].strip('.edu.com')[0] in string.ascii_lowercase:
                    return line

def detect_courses(text):
    '''detect courses and extract all the courses out'''
    courses = ''
    for line in text:
        if 'Courses' in line:
            courses = (line.strip('Courses')).lstrip(',:.- ')
    return courses

def detect_projects(text): 
    '''detect projects and make a list of each project'''
    projects = []
    flag = False
    for line in text:
        if 'Projects' in line:
            flag = True
            continue
        if flag:
            if '-'*10 not in line and line != '\r\n':
                projects.append(line.rstrip('\r\n'))
            elif '-'*10 in line:
                return projects

def detect_education(text):
    '''detect education history with words and make a list of educations'''
    education = []
    for line in text:
        if any(word in line for word in ['University','university','Institute','Bachelor','Master']):
            education.append(line)
    return education

######Write the html contents into .html file#######
def surround_block(tag, text):
    '''surround the content with tags and make it a block in a string'''
    return '<' + tag + '>\n' + text + '\n</' + tag + '>'

def create_html(name, email, courses, projects, education):
    '''This function create the HTML script by create each block and combine them
    into paragraphes and/or divisions, then combine all those together and return
    a string'''
    name_h1      = surround_block('h1', name)
    edu_h2       = surround_block('h2', 'Education')
    proj_h2      = surround_block('h2', 'Projects')
    courses_h3   = surround_block('h3', 'Courses')

    email_par    = surround_block('p', email)
    edu_ul       = create_ul(education)
    proj_ul      = create_ul(create_par(projects))
    courses_span = surround_block('span', courses)

    div1 = create_div(name_h1, email_par)
    div2 = create_div(edu_h2, edu_ul)
    div3 = create_div(proj_h2, proj_ul)
    div4 = create_div(courses_h3, courses_span)

    return '\n'.join(['<div id="page-wrap">\n',div1,div2,div3,div4,'</div>\n</body>\n</html>'])

def create_par(list1):
    '''This function helps to create a paragraph'''
    item_p  = []
    for item in list1:
        item_p.append(surround_block('p', item))
    return item_p

def create_ul(list1):
    '''This function helps to create a Unordered list'''
    item_li = []
    for item1 in list1:
        item_li.append(surround_block('li', item1))
    return surround_block('ul','\n'.join(item_li))

def create_div(header, content):
    '''This function helps to create a Division'''
    return surround_block('div', '\n'.join([header, content]))

def main():
    '''The main function mainly read the text from .txt file and 
    detect all the elements needed and then convert them into html
    format, combine with the headers then write in the .html file'''
    print is_file("resume.txt")
    print is_file("resume.html")

    f = open('resume.html', 'r+')
    lines = f.readlines()
    f.seek(0)
    f.truncate()
    del lines[-1]
    del lines[-1]

    text = read_from_file('resume.txt')

    name      = detect_name(text)
    email     = detect_email(text)
    courses   = detect_courses(text)
    projects  = detect_projects(text)
    education = detect_education(text)

    lines.append(create_html(name, email, courses, projects, education))

    f.writelines(lines)
  
if __name__=='__main__':
    main()