import pygame

computerCombination: []
playerCombination: []
computerCombinationPosition: 1
combinationMaxPosition: 5
memoryMaxCombination: 9


def startReactor():

    audio: {
        'start': pygame.mixer.music('audio/start.mp3'),
        'fail': pygame.mixer.music('audio/fail.mp3'),
        'complete': pygame.mixer.music('audio/complete.mp3'),
        'combinations': [pygame.mixer.music('audio/first.mp3', 'audio/second.mp3', 'audio/third.mp3', 'audio/fourth.mp3', 'audio/fiveth.mp3', 'audio/sixth.mp3', 'audio/seven.mp3', 'audio/eighth.mp3', 'audio/nineth.mp3')]
    }

    inteface: {

    }
