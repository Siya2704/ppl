% courses
course(comp,dsa).
course(comp,dsgt).
course(comp,ppl).
course(comp,dld).
course(math,odemc).
course(math,la).
course(math,uvc).

% faculty
faculty(vk,ppl).
faculty(sh,ppl).
faculty(jm,odemc).
faculty(dng,odemc).
faculty(rs,dsgt).
faculty(jw,dld).
faculty(am,dsa).
faculty(jm,uvc).
faculty(ym,la).

% students
student(comp,ssd).
student(comp,tnb).
student(comp,pas).
student(comp,gvd).
student(comp,sk).
student(math,ssd).
student(math,tnb).
student(math,pas).
student(math,gvd).
student(math,sk).

% faculty in department
dept_faculty(D,F):-course(D,C),faculty(F,C).

% courses taken by student
student_course(S,C):-student(X,S),course(X,C).


% faculty teaches students
faculty_student(F,S):-student(D,S),course(D,C),faculty(F,C).
