let MAGENTA50 = "#dc267f";

function setup() {
  createCanvas(400, 400);
  background(220);
  scene = new Scene();
  createControls(); //create play/pause/stop buttons and progress bar
  shannon();
}

function draw() {}

function shannon() {
  let heading = createText("Shannon Entropy");
  heading.position(20, 50);
  heading.size(45);
  heading.style("font-family", "cursive");
  heading.fill(color(119, 198, 110));
  heading.play("write", 0, 1.5); //startTime = 0, endTime = 1.5 sec

  let equation = createTeX(
    "{\\displaystyle \\mathrm {H} (X)=-\\sum _{i=1}^{n}{\\mathrm {P} (x_{i})\\log \\mathrm {P} (x_{i})}}"
  );
  equation.position(20, 175);
  equation.size(28);
  equation.stroke(MAGENTA50);
  equation.fill(MAGENTA50);
  
  equation.play("createFill", 0, 6.5); //startTime = 0, endTime = 2.5 sec
}
