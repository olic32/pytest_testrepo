class MusicTracker():
    def __init__(self):
        self.track_list = []
        pass
    def show_list(self):

        if len(self.track_list) == 0:
            return "No tracks in library"

        songs = ", ".join(self.track_list)

        new_str = f"In your library, you have {songs}"
    
        return new_str

    def add_a_track(self,track):

        if track in self.track_list:
            pass
        else:
            if type(track) != str:
                raise Exception("Wrong data type!")
            else:
                self.track_list.append(track)