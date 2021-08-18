@namespace
class SpriteKind:
    Grocery = SpriteKind.create()
    CartItem = SpriteKind.create()

def on_on_overlap(person, grocery):
    if controller.A.is_pressed():
        addToCart(grocery)
        pause(100)
sprites.on_overlap(SpriteKind.player, SpriteKind.Grocery, on_on_overlap)

def createSubTotalSprite():
    global subTotalSprite
    subTotalSprite = textsprite.create("$0")
    subTotalSprite.set_max_font_height(8)
    subTotalSprite.left = 0
    subTotalSprite.top = 0
    subTotalSprite.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)

def on_overlap_tile(sprite, location):
    global display, cost3, name2
    display = "Subtotal: $" + str(subTotal)
    for item in sprites.all_of_kind(SpriteKind.CartItem):
        cost3 = sprites.read_data_number(item, "cost")
        name2 = sprites.read_data_string(item, "name")
        display = "" + display + "\\n" + name2 + ": $" + str(cost3)
    info.set_score(subTotal)
    game.show_long_text(display, DialogLayout.CENTER)
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile10
    """),
    on_overlap_tile)

def addToCart(grocery2: Sprite):
    global item2, cost2, weight2, subTotal, speed
    # Clone and place the item inside the cart
    item2 = sprites.create(grocery2.image, SpriteKind.CartItem)
    item2.follow(player)
    item2.x = player.x
    item2.y = player.y
    cost2 = sprites.read_data_number(grocery2, "cost")
    weight2 = sprites.read_data_number(grocery2, "weight")
    # Update the subtotal
    subTotal = subTotal + cost2
    subTotalSprite.set_text("$" + str(subTotal))
    # Update the moving speed
    speed = speed - weight2
    # set a min
    if speed < 0:
        speed = 5
    controller.move_sprite(player, speed, speed)
    # NOTE: Do this last
    sprites.set_data_string(item2, "name", sprites.read_data_string(grocery2, "name"))
    sprites.set_data_number(item2, "cost", cost2)
# Let's use a function to do this, we are going to set up a bunch of products
def createProduct(productImg: Image, cost: number, weight: number, name: str):
    global p
    p = sprites.create(productImg, SpriteKind.Grocery)
    sprites.set_data_string(p, "name", name)
    sprites.set_data_number(p, "cost", cost)
    sprites.set_data_number(p, "weight", weight)
    tiles.place_on_random_tile(p, assets.tile("""
        tile1
    """))
    return p
def createAllProducts():
    i = 0
    while i <= len(groceryNames) - 1:
        createProduct(groceryImages[i],
            groceryCosts[i],
            groceryWeights[i],
            groceryNames[i])
        i += 1
p: Sprite = None
weight2 = 0
cost2 = 0
item2: Sprite = None
name2 = ""
cost3 = 0
subTotal = 0
display = ""
subTotalSprite: TextSprite = None
player: Sprite = None
groceryImages: List[Image] = []
groceryWeights: List[number] = []
groceryCosts: List[number] = []
groceryNames: List[str] = []
speed = 0
speed = 100
groceryNames = ["Milk",
    "Grape Soda",
    "Oatmeal",
    "Turkey",
    "Fancy glass",
    "Chicken soup",
    "Sardines",
    "Flour",
    "Watermelon"]
groceryCosts = [2, 3, 4, 20, 1000, 2, 1, 5, 1]
groceryWeights = [0.3, 0.2, 0.1, 0.1, 0.1, 0.5, 0.5, 0.5, 0.1]
groceryImages = [img("""
        . . . 2 2 2 . . . . . . . . . . 
            . . . c c c 6 6 8 8 . . . . . . 
            . . 6 1 1 1 1 1 9 6 8 . . . . . 
            . 6 1 1 1 1 1 1 8 9 6 8 . . . . 
            6 1 1 1 1 1 1 8 . 8 9 8 . . . . 
            6 1 1 1 1 1 1 8 . 8 9 8 . . . . 
            8 9 1 1 1 1 1 8 . 8 9 8 . . . . 
            8 9 1 1 1 1 1 8 8 9 9 8 . . . . 
            8 9 9 9 9 9 9 9 9 9 9 8 . . . . 
            8 6 9 9 9 9 9 9 9 9 9 8 . . . . 
            . 8 6 9 9 9 9 9 9 9 6 8 . . . . 
            . . 8 8 8 8 8 8 8 8 8 . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    img("""
        . . . . . . . 6 6 6 . . . . . . 
            . . . . . . . c b c . . . . . . 
            . . . . . c c c b c c c . . . . 
            . . . . c b b b b b b b c . . . 
            . . . . c 1 b b b b b 1 c . . . 
            . . . . c 1 1 7 1 7 1 1 c . . . 
            . . . . c 1 1 1 7 1 1 1 c . . . 
            . . . . c 1 1 a c a 1 1 c . . . 
            . . . . c 1 a c a c a 1 c . . . 
            . . . . c 1 c a c a c 1 c . . . 
            . . . . c 1 a c a c a 1 c . . . 
            . . . . c 1 c a c a 1 1 c . . . 
            . . . . c 1 a c a 1 1 1 c . . . 
            . . . . c b 1 a 1 1 1 b c . . . 
            . . . . c b b b b b b b c . . . 
            . . . . . c c c c c c c . . . .
    """),
    img("""
        . c c c c c c c c c c c c c . . 
            c b b b b b b b b b b b b b c . 
            c b b b b b b b b b b b b b c . 
            c c c c c c c c c c c c c c c . 
            c d d 1 1 1 1 1 1 1 1 1 d d c . 
            c d c c c 1 c c c 1 c c c d c . 
            c d c 1 c 1 c 1 c 1 1 c d d c . 
            c d c 1 c 1 c c c 1 1 c d d c . 
            c d c c c 1 c 1 c 1 1 c d d c . 
            c d d 1 1 1 1 1 1 1 1 1 d d c . 
            c d d 1 1 1 2 2 2 1 1 1 d d c . 
            c d d 1 1 2 8 8 8 2 1 1 d d c . 
            c d d 1 1 2 8 d 8 2 1 1 d d c . 
            c d d 1 1 2 8 6 8 2 1 1 d d c . 
            . c d 1 1 1 2 2 2 1 1 1 d c . . 
            . . c c c c c c c c c c c . . .
    """),
    img("""
        . . . c c c c . . . . . . . . . 
            . . c e e e e c c c . . . . . . 
            . c e e e e e e e e c . . . . . 
            . c e e e e e e e e e c . . . . 
            f e e e e c c c e e e c . b b . 
            f e e e c e e e c c c c c d d b 
            f c e e f e e e e e e e c d d b 
            f c c c f e e e f f f f c b b b 
            f c c c c f f f c c c f . c c . 
            . f c c c c c c c c c f . . . . 
            . f c c c c c c c c f . . . . . 
            . . f f f f f f f f . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    img("""
        . . . . . . . . . . . . . . . . 
            . . 6 6 9 9 9 9 . . . . . . . . 
            . 6 9 9 1 1 1 1 9 . . . . . . . 
            6 9 6 9 9 9 1 9 1 9 . . . . . . 
            6 9 9 6 6 6 6 1 1 9 . . . . . . 
            6 9 9 6 9 9 6 1 1 9 . . . . . . 
            . 6 9 6 9 9 6 1 9 . . . . . . . 
            . . 6 9 6 6 1 9 . . . . . . . . 
            . . . 6 9 9 9 . . . . . . . . . 
            . . . . 6 6 . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    img("""
        . . . . . . . . . . . . . . . . 
            . . . . c c c c c c c . . . . . 
            . . . c d d d d d d d c . . . . 
            . . c d d d d d b b d d c . . . 
            . . b c d d d d d d d c b . . . 
            . . b 2 c c c c c c c 2 b . . . 
            . . b 2 2 2 2 2 2 2 2 2 b . . . 
            . . b 2 2 2 2 2 2 2 2 2 b . . . 
            . . b 2 2 2 b b b 2 2 2 b . . . 
            . . b 2 2 b 2 2 2 b 2 2 b . . . 
            . . d 1 2 b 2 2 2 b 2 1 d . . . 
            . . d 1 1 b 2 2 2 b 1 1 d . . . 
            . . d 1 1 b 2 2 2 b 1 1 d . . . 
            . . d 1 1 1 b b b 1 1 1 d . . . 
            . . . d 1 1 1 1 1 1 1 d . . . . 
            . . . . d d d d d d d . . . . .
    """),
    img("""
        . . c c c c c c c c c c . . . . 
            . c d d d d d d d c b b c . . . 
            c d d d d d d d c b d b b c . . 
            c c d d d d d d d c b b c c . . 
            c b c c c c c c c c c c b c . . 
            c b 8 9 8 b 8 9 9 9 8 b b c . . 
            c b b 8 9 6 9 6 9 6 9 8 b c . . 
            c b b 8 9 6 9 6 9 6 9 8 b c . . 
            c b 8 9 8 b 8 9 9 9 8 b b c . . 
            . c c c c c c c c c c c c . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    img("""
        . . . . . . . . . . . . . . . . 
            . . . b 1 1 1 1 1 1 1 1 1 . . . 
            . . b 1 1 1 1 1 1 1 1 1 1 1 . . 
            . . b 1 1 1 1 1 1 1 1 1 8 8 . . 
            . . b 1 1 1 1 1 1 1 8 8 8 8 . . 
            . . b 1 1 1 5 5 5 5 8 8 8 8 . . 
            . . b 1 1 5 5 5 5 5 5 8 8 8 . . 
            . . b 1 8 5 5 5 5 5 5 8 8 8 . . 
            . . c 8 8 5 5 5 5 5 5 8 1 1 . . 
            . . c 8 8 5 5 5 5 5 5 1 1 1 . . 
            . . c 8 8 8 5 5 5 5 1 1 1 1 . . 
            . . c 8 8 8 1 1 1 1 1 1 1 1 . . 
            . . c 2 2 2 1 1 1 1 6 6 6 1 . . 
            . . b 1 2 1 1 1 1 1 1 1 1 1 . . 
            . . b 1 1 1 1 1 1 1 1 1 1 1 . . 
            . . . b b b b b b b b b b . . .
    """),
    img("""
        . . . . . . . 6 . . . . . . . . 
            . . . . 6 6 6 6 6 6 6 . . . . . 
            . . 6 6 6 6 7 6 7 6 6 6 6 . . . 
            . 6 6 7 6 6 7 6 7 6 6 7 7 6 . . 
            . 6 6 7 6 7 6 6 7 6 6 7 6 6 . . 
            6 7 6 7 6 7 6 6 7 7 6 7 6 7 6 . 
            6 7 6 7 6 7 6 6 7 7 6 7 6 7 6 . 
            6 7 6 7 6 7 6 6 7 7 6 7 6 7 6 . 
            6 7 6 7 6 7 6 6 7 7 6 7 6 7 6 . 
            6 7 6 7 6 7 6 6 7 7 6 7 6 7 6 . 
            6 7 6 7 6 7 6 6 7 6 6 7 6 7 6 . 
            6 6 6 7 6 7 6 6 7 6 6 7 6 6 6 . 
            . 6 6 7 6 7 6 6 7 6 6 7 6 6 . . 
            . 6 6 7 6 7 7 6 7 6 6 7 6 6 . . 
            . . 6 6 6 6 7 6 7 6 6 6 6 . . . 
            . . . . 6 6 6 6 6 6 6 . . . . .
    """)]
scene.set_background_color(9)
tiles.set_tilemap(tilemap("""
    level
"""))
player = sprites.create(img("""
        ..fffff......................
            ..fffcd......................
            ..ffddc......................
            ..fdddf......................
            ..fdddd......................
            ...88........................
            ..88dddbbbbbbbbbbbb..........
            ..888....b..b..b..b..........
            .8888....bbbbbbbbbb..........
            .8888....b..b..b..b..........
            .8888....bbbbbbbbbb..........
            .6666.....b.b..b.bb..........
            .6.66......bbbbbbb...........
            .d.d.......d.....d...........
            .d..d......ddddddd...........
            .d..dd......c....c...........
    """),
    SpriteKind.player)
controller.move_sprite(player, speed, speed)
scene.camera_follow_sprite(player)
tiles.place_on_tile(player, tiles.get_tile_location(1, 3))
createSubTotalSprite()
createAllProducts()
info.start_countdown(30)