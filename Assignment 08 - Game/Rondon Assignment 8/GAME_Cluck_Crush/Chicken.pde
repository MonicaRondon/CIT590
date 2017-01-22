/**Inspired by Dr. Dave's DodgeEmBall code.
Creates the chicken class, which include the blueprint for making
chickens and creates the drawChicken and fall methods**/

class Chicken {
  float x;
  float y;
  int w = 48;
  int h = 48;
  int s = 5;
  PImage shell;
  int time;

  Chicken(){
  /**constructs the Chicken object, using an image**/
    x = random(width - w);
    y = 0;
    s = (int)random(13) + 1; // can never be zero
    time = 0;
    /**chicken image source: http://piq.codeus.net/picture/18606/male_chicken **/
    shell = loadImage("images/chicken.png");
  }

  void drawChicken(){
    /**creates method to draw chickens**/
    image(shell, x, y, w, h);
  }

  void fall(){
  /** creates method to make chickens fall vertically**/
    y += s;
    if(y > height){
      y = 0;
    }
  }
}