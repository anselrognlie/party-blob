import pygame
from red_blob import RedBlob
from green_blob import GreenBlob
from blue_blob import BlueBlob
import color

WIDTH = 300
HEIGHT = 300

STARTING_RED_BLOBS = 3
STARTING_GREEN_BLOBS = 5
STARTING_BLUE_BLOBS = 10


game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()

def draw_environment(blobs_list):
    # update
    for blob_dict in blobs_list:
      for (blob_id, blob) in blob_dict.items():
          blob.update()

    # draw
    game_display.fill(color.WHITE)
    for blob_dict in blobs_list:
      for (blob_id, blob) in blob_dict.items():
        blob.draw(game_display, pygame.draw)

    # present
    pygame.display.update()


def main():
    red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
    blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))

    print('Current blue size: {}. Current red size: {}'.format(str(blue_blobs[0].size), str(red_blobs[0].size)))
    blue_blobs[0] + red_blobs[0]
    print('Current blue size: {}. Current red size: {}'.format(str(blue_blobs[0].size), str(red_blobs[0].size)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([red_blobs, green_blobs, blue_blobs])
        clock.tick(60)


if __name__ == '__main__':
    main()
