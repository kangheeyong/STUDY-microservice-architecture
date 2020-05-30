import cmd


class my(cmd.Cmd):
    intro = " Hello "
    prompt = "cmd > "
    file = None

    def do_hello(self, arg):
        'prin Hello~'
        self.hello(arg)

    def do_name(self, arg):
        self.name()

#    def do_job(self, arg):
#        'prnt job'
#        self.job()'

    def hello(self, arg):
        print('Hello~', arg)

    def name(self):
        print('sdfsdf')

    def job(self):
        print('job')


my().cmdloop()
