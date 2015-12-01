import command

class ScreenSession():

    id = None

    def __init__(self,name,new=True):

        self.name = name

        if new:

            #Check whether there are sessions with the same name
            for session in get_all_sessions():
                if name == session.name:
                    raise MoreSessionsWithTheSameNameException

            #Create the session
            command.command('screen -d -m -S '+name)

            #Look for the id
            for session in get_all_sessions():
                if session.name == self.name:
                    self.id = session.id

    def send_command(self,command_to_send):

       command.command(['screen', '-r', self.name, '-X', 'stuff',command_to_send+' \r'])

    def kill(self):

        command.command('screen -S '+self.name+' -X quit')

    def __repr__(self):

        return '<ScreenSession, id=\''+str(self.id)+'\', name=\''+self.name+'\'>'

class MoreSessionsWithTheSameNameException(Exception):

    pass

def get_all_sessions():

    raw_screens = command.command('screen -ls',return_output=True)
    screen_sessions = []

    for n,line in enumerate(raw_screens):

        #Skip the first and last lines
        if n == 0 or n > len(raw_screens) -3:
            continue

        session, date, attached_state = line.strip().split('\t')

        id, name = session.split('.')
        session = ScreenSession(name,new=False)
        session.id = int(id)
        screen_sessions.append(session)

    return screen_sessions

def get_session_with_name(name):

    for session in get_all_sessions():

        if name == session.name:
            return session
