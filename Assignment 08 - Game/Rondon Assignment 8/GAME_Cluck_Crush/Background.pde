/**creates the Background class, which includes the blueprint
for the background object and creates the drawBG method that
makes the background using the two images **/

class Background {
  PImage bckgrnd;
  PImage floor;
  int floorSize = 32;
  Background(){
    /**constructs the background object**/
    /**background image source: https://www.spriters-resource.com/snes/smarioworld**/
    bckgrnd = loadImage("images/bg.png");
    /**floor image source: https://www.spriters-resource.com/snes/smarioworld/ **/
    floor = loadImage("images/floor.png");
  }
  
  void drawBG(){
    /**creates method to draw the game backrground, including floor**/
    image(bckgrnd, 0, 0, width, height);
    for(int i = 0; i <= width / floorSize; i++){
      image(floor, 0 + (floorSize * i), height - floorSize, floorSize, floorSize);
    }
  }
}