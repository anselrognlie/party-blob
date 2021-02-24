import pygame
from blue_blob import BlueBlob
import color

WIDTH = 300
HEIGHT = 300

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3


game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()

def draw_environment(blobs_list):
    # update
    for blob_dict in blobs_list:
      for (blob_id, blob) in blob_dict.items():
          blob.move_fast()
          blob.check_bounds()

    # draw
    game_display.fill(color.WHITE)
    for blob_dict in blobs_list:
      for (blob_id, blob) in blob_dict.items():
          pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)

    # present
    pygame.display.update()


def main():
    blue_blobs = dict(enumerate([BlueBlob(color.BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([BlueBlob(color.RED, WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs, red_blobs])
        clock.tick(60)


if __name__ == '__main__':
    main()
