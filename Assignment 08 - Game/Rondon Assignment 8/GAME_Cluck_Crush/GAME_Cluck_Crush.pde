/**This is a program  by Monica Rondon for the game "Cluck Crush!".
The purpose of the game is to help grandma avoid the falling chickens by 
moving her Left/Right across the screen.
Every second you keep grandma safe, your score goes up. 
But as time passes the number of chickens falling increases. 
The game ends when grandma fails to dodge a falling chicken and
she gets smooshed!**/

/**GLOBAL VALUES**/
ArrayList<Chicken> Chickens = new ArrayList();
PFont myFont;
int gameHeight = 800;
int gameTime = 0;
PImage playerImage;
int playerHeight = 114;
int playerWidth = 60;
int playerSpeed = 20;
int playerPosition = 470;
boolean smooshed = false;
Background bg;
long gameStart;
long score;

void setup() {
  /** sets up Cluck Crushed game **/
  size(1000, 800);
  background(255, 255, 255);
  /** OldLadyIdle image source: http://www.blackgaruda.com/#/pixelretro/ **/
  playerImage = loadImage("images/OldLadyIdle.gif");
  gameStart = System.currentTimeMillis();
  myFont = createFont("font/emulogic.ttf", 32);
  textFont(myFont); 
  smooshed = false;
  Chickens = new ArrayList();
  gameTime = 0;
  playerPosition = 470;
  bg = new Background();
}

void draw() {
  /** Creates animation and draws images **/
  background(255);
  bg.drawBG();
  player();
  /** gameTime code inspired by Dr. Dave's DodgeEm code, tracks
  game time for the score and creation/dropping of chickens **/
  if (!smooshed){
    gameTime += 1;
    score = (System.currentTimeMillis() - gameStart) / 1000;
    if (gameTime % 60 == 0){
      // creates a new chicken every 60 frames (1 per second)
      Chickens.add(new Chicken());    
    }
    dropChickens();
  }
  drawChickens();
  Smoosh();
  fill(255, 255, 255);
  text("Score: " + score, width - 300, 50);  
  if(smooshed){
    drawEnding();
  }
}

void keyPressed() { 
  /** checks if the player has pressed one of the control keys
      - left arrow: move the player to the left
      - right arrow: move the player to the right
      - enter restarts the game **/
  if (keyCode == ENTER){
    setup();
  }
  if (keyCode == LEFT){
    playerPosition = playerPosition - playerSpeed;
    if(playerPosition < 0){
      // player cannot go off the left side of the screen 
      playerPosition = 0;
    }
  }
  if (keyCode == RIGHT){
    playerPosition = playerPosition + playerSpeed;
    if(playerPosition > width - playerWidth){
      // player cannot go off the right side of the screen
      playerPosition = width - playerWidth;
    }
  }
}

void player(){
  /**creates the player using the loaded OldLadyIdle image to represent
  grandma**/
  image(playerImage, playerPosition - 32, gameHeight - playerHeight - 32);
}

void drawChickens(){
  /**drawChickens code inspired by Dr. Dave's DodgeEm code,
  draws the chickens, using the drawChick method from the Chicken class**/
  for (Chicken chck: Chickens){
    chck.drawChicken();
  }
}

void dropChickens(){
  /**dropChickens code inspired by Dr. Dave's DodgeEm code
  makes the chickens fall, using the fall method from the Chicken class**/
  for (Chicken chck: Chickens){
    chck.fall();
  }
}

void drawEnding() {
  /** called when the game ends (i.e., grandma overlaps with a chicken),
  tells the player their score and instructs them on how to play again**/
  fill(255, 0, 0);
  text("Smoosh!", 395, 200);
  textFont(myFont);
  text("You got Cluck Crushed!", 150, 350);
  text("You survived for " + score + " seconds", 80, 500);
  fill(255, 255, 255);
  text("Press ENTER to play again.", 95, 700);
}

boolean IsSmooshing(float player_x, float player_y, float player_w, float player_h, 
float block_x, float block_y, float block_w, float block_h){
  /** source code: http://gamemath.com/2011/09/detecting-whether-two-boxes-overlap/
  detects if two rectangles overlap**/
    if (player_w < block_x) return false; // a is left of b
    if (player_x > block_w) return false; // a is right of b
    if (player_h < block_y) return false; // a is above b
    if (player_y > block_h) return false; // a is below b
    return true; // boxes overlap
    
}

void Smoosh(){
  /**uses the IsSmooshing functiong to see grandama has been smooshed (overlaps)
  with a chicken**/
  float player_x = playerPosition;
  float player_y = (gameHeight - playerHeight);
  float player_w = (playerPosition + playerWidth);
  float player_h = gameHeight - 32;
  for (Chicken chck: Chickens){
    float block_x = chck.x;
    float block_y = chck.y;
    float block_w = (chck.x + chck.w);
    float block_h = (chck.y + chck.h);
    if(IsSmooshing(player_x, player_y, player_w, player_h, block_x, block_y, block_w, block_h)){
      smooshed = true;
    }
  } 
}
  