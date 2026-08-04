class DuelManager:
    def __init__(self):
        self.pending_duels = []

    def add_duel(self, duel):
        self.pending_duels.append(duel)

    def get_duel_by_player(self, player_id):
        for duel in self.pending_duels:
            if duel.opponent.id == player_id:
                return duel
    
        return None

    def remove_duel(self, duel):
        self.pending_duels.remove(duel)