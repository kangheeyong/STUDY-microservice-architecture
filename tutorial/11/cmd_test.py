import cmd


class my(cmd.Cmd):
    intro = " Hello "
    prompt = " (mdp) "
    file = None

    def do_hello(self, arg):
        'print Hello~'
        self.hello(arg)

    def do_name(self, arg):
        'print name'
        self.name()

    def do_job(self, arg):
        'print job'
        self.job()

    def hello(self, arg):
        print('Hello~', arg)

    def name(self):
        print('sdfsdf')

    def job(self):
        print('job')


my().cmdloop()
