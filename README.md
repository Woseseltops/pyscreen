# pyscreen
A light-weight library for easy interaction between Python and GNU screen.

This library allows you create, find and kill screen sessions programmatically from Python, as well as send (string) commands to these sessions. You can use this to start other software inside a screen session from a Python script, like this:

    import pyscreen

    #Start a new session and give it something to do    
    session = pyscreen.ScreenSession('myName')
    session.send_command('echo hello')

    #Kill a screen session with a particular name
    session = pyscreen.get_session_with_name('testSession')
    session.kill()

    #Print all the id of all sessions
    for session in pyscreen.get_all_sessions():
        print(session.id)

## Installation

Either `git clone` this directory, or run

    pip install pyscreen
