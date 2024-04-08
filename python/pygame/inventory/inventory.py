import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)
ITEM_COLOR = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

# Item class


class Item:
    def __init__(self, name, position):
        self.name = name
        self.image = pygame.Surface((30, 30))
        self.image.fill(ITEM_COLOR)
        self.rect = self.image.get_rect()
        self.position = position
        self.quantity = 1
        self.quantity_total = 1

    def draw(self, surface):
        x, y = self.position
        self.rect.topleft = (x, y)
        surface.blit(self.image, self.rect)
        quantity_text = FONT.render(
            f"{self.quantity}/{self.quantity_total}", True, (255, 255, 255))
        surface.blit(quantity_text, (x + 35, y+5))

# Inventory class


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        # Check if the item is already in the inventory
        for existing_item in self.items:
            if existing_item.name == item.name:
                existing_item.quantity += 1
                return
        self.items.append(item)

    def draw(self, surface):
        for item in self.items:
            item.draw(surface)


# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Inventory System")

# Create an inventory
inventory = Inventory()

# Add items to the inventory with custom positions
item1 = Item("Item 1", (50, 50))
item2 = Item("Item 2", (50, 350))
# Add another "Item 1" to test quantity stacking
item3 = Item("Item 1", (50, 500))
item3 = Item("Item 3", (50, 500))
item4 = Item("Item 4", (700, 450))
item5 = Item("Item 5", (700, 50))
inventory.add_item(item1)
inventory.add_item(item2)
inventory.add_item(item3)
inventory.add_item(item4)
inventory.add_item(item5)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw the inventory
    inventory.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
