import sqlite3

class GameDB:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def establish_connection(self, db_file):
        try:
            self.connection = sqlite3.connect(db_file)
            self.cursor = self.connection.cursor()
            return True
        except ValueError:
            return False

    def close_connection(self):
        try:
            self.connection.close()
            return True
        except ValueError:
            return False

    def get_players(self, game):
        self.cursor.execute('SELECT players FROM games WHERE game = ' + game)
        result = self.cursor.fetchall()
        self.cursor = None
        return result

    def get_game(self, user):
        self.cursor.execute('SELECT game FROM users WHERE user = ' + user)
        result = self.cursor.fetchall()
        self.cursor = None
        return result

    '''def join_game(self, game, player):
        players = get_players(game)
        self.cursor.execute('UPDATE games SET players = 'players' WHERE game = ' + game)'''
