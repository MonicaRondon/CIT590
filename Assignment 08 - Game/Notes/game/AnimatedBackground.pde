class AnimatedBackground {
  PImage img;
  float x = 0;
  
  int sourceH = 432;
  int sourceW = 512;
  
  float w, h;
  
  AnimatedBackground(){
    img = loadImage("images/bg.png");;
    h = 1.8 * sourceH;
    w = 1.8 * sourceW;
  }
  
  void drawBG(){
    for(int i = 0; i < 3; i++){
      image(img, x + (i*w), 0, w, h);    
    }
  }
  
  void animateBG(){
    if(x < 0 && x % w == 0){
      x = 0;
    } else {
      x -= 1;
    }
  }
  
}