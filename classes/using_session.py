from header import *

class using_session:
    # @app.route('/set_session/<value>')
    @staticmethod
    def set_session(value):
        session['session_values'] = value
        return 'Session has been created!'

    # @app.route('/get_session')
    @staticmethod
    def get_session():
        if 'session_values' in session:
            return session.get('session_values')
        else:
            return "No any session is available!"

    # @app.route('/del_session')
    @staticmethod
    def del_session():
        if 'session_values' in session:
            session.pop('session_values')
            return 'Session has been deleted!'
        else:
            return "No any session is available!"