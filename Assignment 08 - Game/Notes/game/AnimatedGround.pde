class AnimatedGround {
  PImage img;
  float x = 0;
  
  int sourceH = 16;
  int sourceW = 16;
  int number_of_tiles;

  float w, h;
  
  AnimatedGround(){
    img = loadImage("images/floor.png"); // sourceImage;
    h = 2 * sourceH;
    w = 2 * sourceW;
    number_of_tiles = (int)(width / w) + 3; 
  }
  
  void drawFloor(){
    for(int i = 0; i < number_of_tiles; i++){
      image(img, x + (i*w), height-h, w, h);    
    }
  }
  
  void animateFloor(){
    if(x < 0 && x % w == 0){
      x = 0;
    } else {
      x -= 4;
    }
  }
  
}