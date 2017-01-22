class Block {
  float x, y;
  int h = 32;
  int w = 32;
  int time = 0;
  ArrayList<PImage> images;
  
  Block(ArrayList<PImage> shell_images){
    images = shell_images;
    x = random(width - w);
    y = 0;
  }

  void drawBlock(){
    //image(images.get((time++) % 4), x, y, w, h);
    image(images.get((time++/4) % 4), x, y, w, h);
  }
  
  void fall(){
    y += 10;
  }

}