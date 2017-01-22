// single line comment
//Java is a strong type language, it has to know your type of 
void setup() {
  size(1000, 1000);
  background(200, 245, 250);
  fill(0, 0, 20);
  text("Monica Rondon", 900, 990);
  cirTwo(700);
  triThree();
  cirOne(500);
  sqOne();
  triOne();
  centre(100);
  ringOne(80);
  translate(0, 185);
  ringOne(80);
  translate(92.5, -92.5);
  ringOne(80);
  translate(-185, 0);
  ringOne(80);
  resetMatrix();
  ringTwo(20);
  translate(0, 459);
  ringTwo(20);
  translate(229.5, -229.5);
  ringTwo(20);
  translate(-459, 0);
  ringTwo(20);
  translate(114.75, -114.75);
  ringTwo(20);
  translate(229.5, 0);
  ringTwo(20);
  translate(0, 229.5);
  ringTwo(20);
  translate(-229.5, 0);
  ringTwo(20);
  resetMatrix();
  triTwo();
  ringThree(35);
  translate(0,743);
  ringThree(35);
  translate(371.5,-371.5);
  ringThree(35);
  translate(-734, 0);
  ringThree(35);
  resetMatrix();
  ringFour(20);
  strokeWeight(1);
  line(500, 0, 500, 1000);
  line(0, 500, 1000, 500);
  line(0,0, 1000, 1000);
  line(0,1000, 1000,0);
}

void centre(int n) {
  strokeWeight(10);
  fill(200, 245, 250);
  ellipse(500, 500, n, n);
}

void ringOne(int n) {
  strokeWeight(1);
  fill(190, 255, 230);
  ellipse(500, 410, n, n);
}

void triOne() {  
 strokeWeight(5);
  fill(100,220,255);
  triangle(399,280, 500,500, 601, 280);
  triangle(399,720, 500,500, 601, 720);
  triangle(720,399, 500,500, 720, 601);
  triangle(280,399, 500,500, 280, 601);
  
  strokeWeight(5);
  fill(160,230,255);
  triangle(399,500, 500, 280, 601, 500);
  triangle(399,500, 500,720, 601, 500);
  triangle(500,399, 720, 500, 500, 601);
  triangle(500,399, 280, 500, 500, 601);
}

void sqOne() {  
  strokeWeight(2);
  fill(255, 255, 255);
  quad(280, 500, 500, 720, 720, 500, 500, 280);
}

void cirOne(int n){
  strokeWeight(10);
  fill(200, 250, 255);
  ellipse(500, 500, n, n); 
}

void cirTwo(int n){
  strokeWeight(10);
  fill(50, 245, 250);
  ellipse(500, 500, n, n); 
}

void ringTwo(int n){
  strokeWeight(1);
  fill(90,230,230);
  ellipse(500, 270, n, n);
}

void ringThree(int n){
  strokeWeight(1);
  fill(20,230,220);
  ellipse(500, 129, n, n);
}

void ringFour(int n){
  strokeWeight(1);
  fill(90,175,250);
  ellipse(240, 240, n, n);
  ellipse(240, 760, n, n);
  ellipse(760, 760, n, n);
  ellipse(760, 240, n, n);
}

void triTwo(){
 strokeWeight(2);
 fill(0,180,230);
 triangle(280,399, 240, 240, 399, 280);
 triangle(280,601, 240, 760, 399, 720);
 triangle(607,720, 760, 760, 720, 601);
 triangle(720,399, 760, 240, 601, 280);
}

void triThree(){
 strokeWeight(5);
 fill(15,200,200);
 triangle(399,280, 500, 200, 601, 280);
 triangle(280,399, 200, 500, 280, 601);
 triangle(399,720, 500, 800, 601, 720);
 triangle(720,399, 800,500, 720, 601);
 
 strokeWeight(5);
 fill(0,200,211);
 triangle(500, 200, 240, 240, 200, 500);
 triangle(200, 500, 240, 760, 500, 800);
 triangle(500, 800, 760, 760, 800, 500);
 triangle(800, 500, 760, 240, 500, 200);

}