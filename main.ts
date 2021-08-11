namespace SpriteKind {
    export const Grocery = SpriteKind.create()
    export const CartItem = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Grocery, function (person, grocery) {
    if (controller.A.isPressed()) {
        addToCart(grocery)
        pause(100)
    }
})
function createSubTotalSprite () {
    subTotalSprite = textsprite.create("$0")
    subTotalSprite.setMaxFontHeight(8)
    subTotalSprite.left = 0
    subTotalSprite.top = 0
    subTotalSprite.setFlag(SpriteFlag.RelativeToCamera, true)
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`tile10`, function (sprite, location) {
    display = "Subtotal: $" + subTotal
    for (let item of sprites.allOfKind(SpriteKind.CartItem)) {
        cost = sprites.readDataNumber(item, "cost")
        name = sprites.readDataString(item, "name")
        display = "" + display + "\\n" + name + ": $" + cost
    }
    info.setScore(subTotal)
    game.showLongText(display, DialogLayout.Center)
    game.over(true)
})
function addToCart (grocery: Sprite) {
    // Clone and place the item inside the cart
    item2 = sprites.create(grocery.image, SpriteKind.CartItem)
    item2.follow(player)
    item2.x = player.x
    item2.y = player.y
    cost2 = sprites.readDataNumber(grocery, "cost")
    weight = sprites.readDataNumber(grocery, "weight")
    // Update the subtotal
    subTotal = subTotal + cost2
    subTotalSprite.setText("$" + subTotal)
    // Update the moving speed
    speed = speed - weight
    // set a min
    if (speed < 0) {
        speed = 5
    }
    controller.moveSprite(player, speed, speed)
    // NOTE: Do this last
    sprites.setDataString(item2, "name", sprites.readDataString(grocery, "name"))
    sprites.setDataNumber(item2, "cost", cost2)
}
// Let's use a function to do this, we are going to set up a bunch of products
function createProduct (productImg: Image, cost: number, weight: number, name: string) {
    p = sprites.create(productImg, SpriteKind.Grocery)
    sprites.setDataString(p, "name", name)
    sprites.setDataNumber(p, "cost", cost)
    sprites.setDataNumber(p, "weight", weight)
    tiles.placeOnRandomTile(p, assets.tile`tile1`)
    return p
}
function createAllProducts () {
    for (let i = 0; i <= groceryNames.length - 1; i++) {
        createProduct(groceryImages[i], groceryCosts[i], groceryWeights[i], groceryNames[i])
    }
}
let p: Sprite = null
let weight = 0
let cost2 = 0
let item2: Sprite = null
let name = ""
let cost = 0
let subTotal = 0
let display = ""
let subTotalSprite: TextSprite = null
let player: Sprite = null
let groceryImages: Image[] = []
let groceryWeights: number[] = []
let groceryCosts: number[] = []
let groceryNames: string[] = []
let speed = 0
speed = 100
groceryNames = [
"Milk",
"Grape Soda",
"Oatmeal",
"Turkey",
"Fancy glass",
"Chicken soup",
"Sardines",
"Flour",
"Watermelon"
]
groceryCosts = [
2,
3,
4,
20,
1000,
2,
1,
5,
1
]
groceryWeights = [
0.3,
0.2,
0.1,
0.1,
0.1,
0.5,
0.5,
0.5,
0.1
]
groceryImages = [
img`
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
    `,
img`
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
    `,
img`
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
    `,
img`
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
    `,
img`
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
    `,
img`
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
    `,
img`
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
    `,
img`
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
    `,
img`
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
    `
]
scene.setBackgroundColor(9)
tiles.setTilemap(tilemap`level`)
player = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(player, speed, speed)
scene.cameraFollowSprite(player)
tiles.placeOnTile(player, tiles.getTileLocation(1, 3))
createSubTotalSprite()
createAllProducts()
info.startCountdown(30)
