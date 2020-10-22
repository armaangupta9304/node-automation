import sys
import os

jscode = None
router = None
controller = None
with open('E:\\Programming\\NodeProjectManager\\test.js', 'r') as f:
    jscode = f.read().encode('utf8')

with open('E:\\Programming\\NodeProjectManager\\routes.js', 'r') as f:
    router = f.read()

with open('E:\\Programming\\NodeProjectManager\\controller.js', 'r') as f:
    controller = f.read()

class NodeProjectMaker:
    def __init__(self, projectName, dir_, preDefined=jscode, isMongoose = False, additional=''):
        if additional == None:
            additional = ''
        self.projectName = projectName
        self.dir = dir_
        self.jscode = preDefined
        if isMongoose:
            self.dependencies = 'express mongoose cors dotenv colors ' + additional
        else:
            self.dependencies = 'express pg sequelize cors dotenv colors '+additional
    def makeProject(self):
        os.mkdir(os.path.join(self.dir, self.projectName))
        os.mkdir(os.path.join(self.dir, self.projectName, 'routes'))
        with open(os.path.join(self.dir, self.projectName, 'routes', 'routes.js'), 'w') as f:
            f.write(router)

        os.mkdir(os.path.join(self.dir, self.projectName, 'models'))
        os.mkdir(os.path.join(self.dir, self.projectName, 'controllers'))
        with open(os.path.join(self.dir, self.projectName, 'controllers', 'controller.js'), 'w') as f:
            f.write(controller)
        
        with open(os.path.join(self.dir, self.projectName, 'app.js'), 'wb') as f:
            f.write(self.jscode)

        os.chdir(os.path.join(self.dir, self.projectName))
        print(os.getcwd())
        os.system('npm init -y')
        os.system('npm install ' + self.dependencies)
        os.system('git init')
        with open('.gitignore', 'w') as f:
            f.write('node_modules')
