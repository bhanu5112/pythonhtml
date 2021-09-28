
f=open("data.csv",'r')
header=f.readline()
l=f.readline()
course,student={},{}

while (l):
 lcomp=l.strip().split(',')
 if int(lcomp[0]) in student:
   student[int(lcomp[0])].append([int(lcomp[1]),int(lcomp[2])])
 else:
   student[int(lcomp[0])]=[[int(lcomp[1]),int(lcomp[2])]]
 
 if int(lcomp[1]) in course:
   course[int(lcomp[1])].append(int(lcomp[2]))
 else:
   course[int(lcomp[1])]=[int(lcomp[2])]
 l=f.readline()
f.close()



from jinja2 import Template
TEMPLATE1='''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title> Student Details </title>
        
    </head>
    <body>
        <div id="intro">
            <h1>Student Details</h1>
           
        </div>
        <div id="main">
            <table border="1">
                <thead>
                    <tr>
                      <th>Student id</th>
                      <th>Course id</th>
                      <th>Marks</th>
                  </tr>
                </thead>
                <tbody>
                    {% for i in student[sid] %}
                    <tr>
                        <td>{{sid}}</td>
                        <td>{{i[0]}}</td>
                        <td>{{i[1]}}</td>
                    </tr>
                    {% endfor %}
                    <tr>
                      <td colspan="2">Total</td>
                      <td>{{total}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </body>
</html>

'''
TEMPLATE2='''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title> Course Details </title>
        
    </head>
    <body>
        <div id="intro">
            <h1>Course Details</h1>
           
        </div>
        <div id="main">
            <table border="1">
                <thead>
                    <tr>
                      <th>Average Marks</th>
                      <th>Maximum Marks</th>
                  </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{{Average}}</td>
                        <td>{{Maximum}}</td>
                    </tr>
                </tbody>
            </table>
            <img src="hist.png" alt="sorry could not display image" >
        </div>
    </body>
</html>

'''
TEMPLATE3='''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title>Something Went Wrong</title>
        
    </head>
    <body>
        <div id="intro">
           <h1>Wrong Inputs</h1>
        </div>
        <div id="main">
          Something went wrong
        </div>
    </body>
</html>

'''

import sys

import matplotlib.pyplot as plt

f=open("output.html",'w')
try:
 if sys.argv[1]=='-s':
   if int(sys.argv[2]) in student:
     total= sum( i[1] for i in student[int(sys.argv[2])]) 
     template=Template(TEMPLATE1)
     f.write(template.render(student=student, sid=int(sys.argv[2]),total=total))
   else:
     template=Template(TEMPLATE3)
     f.write(template.render())
 elif sys.argv[1]=='-c':
   if int(sys.argv[2]) in course:
     print(course)
     print(course[int(sys.argv[2])])
     print(sum(course[int(sys.argv[2])]))
     print(len(course[int(sys.argv[2])]))
     Average=sum(course[int(sys.argv[2])])/len(course[int(sys.argv[2])])
     Maximum=max(course[int(sys.argv[2])])
     template=Template(TEMPLATE2)
     plt.hist(course[int(sys.argv[2])])
     plt.xlabel('Marks')
     plt.ylabel('Frequency')
     plt.savefig("hist.png")
     f.write(template.render(Average=Average, Maximum=Maximum))
   else:
     template=Template(TEMPLATE3)
     f.write(template.render())
 else:
   template=Template(TEMPLATE3)
   f.write(template.render())
except IndexError:
 template=Template(TEMPLATE3)
 f.write(template.render())
f.close()