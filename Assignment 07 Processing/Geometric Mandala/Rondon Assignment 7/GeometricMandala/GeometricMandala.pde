/**this a program by Monica Rondon that draws a mandala
using geomtric shapes*/

void setup() {
  //sets up background to create picture in processing
  size(1000, 1000);
  background(200, 245, 250);
  //places names in lower right corner
  fill(0, 0, 20);
  textSize(14);
  text("Monica Rondon", 868, 920);
  
  //populates mandela with shapes
  cirTwo(700);
  triThree();
  cirOne(500);
  sqOne();
  triOne();
  centre(100);
  /*for loop which creates the first ring of circles
  around the centre*/
  float TranslateBase = 185;
  float[] xvalues = new float[]{ 0, 0, 0.5, -1 };
  float[] yvalues = new float[]{ 0, 1, -0.5, 0 };
  for (int i = 0; i < 4; i++){
    translate(TranslateBase*xvalues[i], TranslateBase*yvalues[i]);
    ringOne(80);
  }
  resetMatrix();
  /*for loop that creates the second part of
  second ring of circles around the centre*/
  TranslateBase = 459;
  for (int i = 0; i < 4; i++){
    translate(TranslateBase*xvalues[i], TranslateBase*yvalues[i]);
    ringTwo(20);
  }
  /*creates the first part of the second ring of circles
  around the centre*/
  translate(114.75, -114.75);
  ringTwo(20);
  translate(229.5, 0);
  ringTwo(20);
  translate(0, 229.5);
  ringTwo(20);
  translate(-229.5, 0);
  ringTwo(20);
  resetMatrix();
  //populates mandela with shapes
  triTwo();
  /*for loop that creates the third ring of circles
  around the centre*/
  TranslateBase = 743;
  for (int i = 0; i < 4; i++){
    translate(TranslateBase*xvalues[i], TranslateBase*yvalues[i]);
    ringThree(35);
  }
  resetMatrix();
  //creates last ring of circles
  ringFour(20);
  //adds in lines
  strokeWeight(1);
  line(500, 0, 500, 1000);
  line(0, 500, 1000, 500);
  line(0, 0, 1000, 1000);
  line(0, 1000, 1000, 0);
}

void centre(int n) {
  /**creates the centre circle*/
  strokeWeight(10);
  fill(200, 245, 250);
  ellipse(500, 500, n, n);
}

void ringOne(int n) {
  /**creates the first circle in the first ring of circles
  out from the centre circle*/
  strokeWeight(1);
  fill(190, 255, 230);
  ellipse(500, 410, n, n);
}

void triOne() { 
  /**creates the first set of eight triangles around the centre
  circle*/
  strokeWeight(5);
  fill(100, 220, 255);
  triangle(399, 280, 500, 500, 601, 280);
  triangle(399, 720, 500, 500, 601, 720);
  triangle(720, 399, 500, 500, 720, 601);
  triangle(280, 399, 500, 500, 280, 601);
  strokeWeight(5);
  fill(160, 230, 255);
  triangle(399, 500, 500, 280, 601, 500);
  triangle(399, 500, 500, 720, 601, 500);
  triangle(500, 399, 720, 500, 500, 601);
  triangle(500, 399, 280, 500, 500, 601);
}

void sqOne() {  
  /**creates the inner white square*/
  strokeWeight(2);
  fill(255, 255, 255);
  quad(280, 500, 500, 720, 720, 500, 500, 280);
}

void cirOne(int n){
  /**creates the first circle out from the
  centre circle*/
  strokeWeight(10);
  fill(200, 250, 255);
  ellipse(500, 500, n, n); 
}

void cirTwo(int n){
  /**creates the second circle out from the
  centre circle*/
  strokeWeight(10);
  fill(50, 245, 250);
  ellipse(500, 500, n, n); 
}

void ringTwo(int n){
  /**creates the first circle in the second ring of circles
  out from the centre circle*/
  strokeWeight(1);
  fill(90, 230, 230);
  ellipse(500, 270, n, n);
}

void ringThree(int n){
  /**creates the first circle in the third ring of circles
  out from the centre circle*/
  strokeWeight(1);
  fill(20, 230, 220);
  ellipse(500, 129, n, n);
}

void ringFour(int n){
  /**creates the fourth ring of circles
  out from the centre circle*/
  strokeWeight(1);
  fill(90, 175, 250);
  ellipse(240, 240, n, n);
  ellipse(240, 760, n, n);
  ellipse(760, 760, n, n);
  ellipse(760, 240, n, n);
}

void triTwo(){
 /**creates the second set of four triangles around the centre
  circle*/
 strokeWeight(2);
 fill(0, 180, 230);
 triangle(280, 399, 240, 240, 399, 280);
 triangle(280, 601, 240, 760, 399, 720);
 triangle(607, 720, 760, 760, 720, 601);
 triangle(720, 399, 760, 240, 601, 280);
}
  
void triThree(){
 /**creates the outer set of eight triangles around the centre
  circle*/
 strokeWeight(5);
 fill(15, 200, 200);
 triangle(399, 280, 500, 200, 601, 280);
 triangle(280, 399, 200, 500, 280, 601);
 triangle(399, 720, 500, 800, 601, 720);
 triangle(720, 399, 800, 500, 720, 601);
 strokeWeight(5);
 fill(0, 200, 211);
 triangle(500, 200, 240, 240, 200, 500);
 triangle(200, 500, 240, 760, 500, 800);
 triangle(500, 800, 760, 760, 800, 500);
 triangle(800, 500, 760, 240, 500, 200);
}