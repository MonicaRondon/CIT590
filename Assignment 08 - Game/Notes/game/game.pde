// Major components of a game
// PLAYER
// PLAYER - controls
//  - left / right arrow
// ENEMYS - blocks
// COLLISION (hit test)
// SCORE?
// LOSS CONDITION?
// START, MENU?

// GLOBAL VALUES
ArrayList<Block> Blocks = new ArrayList();
int gameHeight = 800;
int gameTime = 0;
int playerHeight = 60;
int playerWidth = 60;
int playerSpeed = 20;
int playerPosition = 500;
int groundHeight = 32;
boolean smooshed = false;
AnimatedBackground bg;
AnimatedGround floor;
ArrayList<PImage> shell_images = new ArrayList<PImage>();

// SET UP
  // Monica job #1 - get a PLAYER onto the screen
  // the PLAYER should be a BOX that is a BOX
void setup() {
  //sets up background to create picture in processing
  bg = new AnimatedBackground();
  floor = new AnimatedGround();

  for(int i = 0; i < 4; i++){
    shell_images.add(loadImage("./images/shell-0"+i+".png"));
  }
  
  
  size(1000, 800);
  background(255, 255, 255);
}

// DRAW
// *** DRAW HAPPENS 60 times a second
void draw() {
  background(255);
  bg.drawBG();
  floor.drawFloor();
  player();
  if(smooshed){
    drawEnding();
    return;
  }
  /*gameTime code inspired by Dr. Dave's DodgeEm code*/
  gameTime += 1;
  if (gameTime % 10 == 0){
    Blocks.add(new Block(shell_images));    
  }
  createBlocks();
  dropBlocks();
  bg.animateBG();
  floor.animateFloor();
  Smoosh();
}

void keyPressed() {
  if(smooshed){
    return;
  }
  
  /* check if the user has pressed one of the control keys
      - left arrow: move the player to the left
      - right arrow: move the player to the right
      - ???? any others (can add these later AFTER the game works basically)
          for example: kaboom, lazer beams, turtles  (shoot turtles at blocks) 
        ???
  */
  if (keyCode == LEFT){
    playerPosition = playerPosition - playerSpeed;
  }
  if (keyCode == RIGHT){
    playerPosition = playerPosition + playerSpeed;
  }
  // the variable 'key' is special. in this function
  // it holds the value of the key that was pressed 
  //

}


void player(){
  /*creates the square that represents the player*/
  fill(0,240,240);
  rect(playerPosition, gameHeight - playerHeight - groundHeight, playerWidth, playerHeight);
}

void createBlocks(){
  /*createBlock code inspired by Dr. Dave's DodgeEm code*/
  for (Block blck: Blocks){
    blck.drawBlock();
  }
}

void dropBlocks(){
  /*dropBlock code inspired by Dr. Dave's DodgeEm code*/
  ArrayList<Block> remove = new ArrayList<Block>();
  for (Block blck: Blocks){
    blck.fall();
    if(blck.y > gameHeight - groundHeight){
      blck.y = 0;
      //remove.add(blck);
    }
  }
  //Blocks.removeAll(remove);
}

void drawEnding() {
  text("smoosh", 500, 500);

}

boolean overlap(float x1, float  y1, float  w1, float  h1, float  x2, float  y2, float  w2, float  h2){
    if (x1 + w1 < x2) return false; // a is left of b
    if (x1 > x2 + w2) return false; // a is right of b
    if (y1 + h1 < y2) return false; // a is above b
    if (y1 > y2 + h2) return false; // a is below b
    return true; // boxes overlap
}

void Smoosh(){
  float player_bottom = gameHeight - groundHeight;
  float player_top = player_bottom - playerHeight;
  float player_right = playerPosition + playerWidth;
  /*detects when a Block smooshes a player*/
  for (Block blck: Blocks){
    if(overlap(blck.x, blck.y, blck.w, blck.h, playerPosition, player_top, playerWidth, playerHeight)){
      smooshed = true; 
    };
  }

}