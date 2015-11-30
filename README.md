# pyscreen
A light-weight library for easy interaction between Python and GNU screen.

This library allows you create, find and kill screen sessions programmatically from Python, as well as send (string) commands to these sessions. You can use this to start other software inside a screen session from a Python script, like this:

    from pyview import ScreenSession, get_all_sessions, get_session_with_name

    #Start a new session and give it something to do    
    session = Session('myName')
    session.send_command('echo hello')

    #Kill a screen session with a partiular name
    session = get_session_with_name('testSession')
    session.kill()

    #Print all the id of all sessions
    for session in get_all_sessions:
        print(session.id)