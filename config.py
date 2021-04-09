import pygame
import os


computerCombination = []
playerCombination = []
computerCombinationPositions = 1
combinationMaxPositions = 5
memoryMaxCombination = 9


class audio():

    start = pygame.mixer.music.load(os.path.join('audio', 'start.mp3'))
    fail = pygame.mixer.music.load(os.path.join('audio', 'fail.mp3'))
    complete = pygame.mixer.music.load(os.path.join('audio', 'complete.mp3'))
    combinations = [
        pygame.mixer.music.load(os.path.join('audio', 'first.mp3', 'second.mp3', 'third.mp3',
                                'fourth.mp3', 'fifth.mp3', 'sixth.mp3', 'seventh.mp3', 'eighth.mp3', 'nineth.mp3'))
    ]

    def loadAudio(self, filename):
        self.file = open(filename)
        self.audio = open(self.file)
        audio.load()
        return audio


class interface():
    pass


class startReactor():
    pass
