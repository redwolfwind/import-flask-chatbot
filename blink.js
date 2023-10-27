var eyesImg = document.getElementById("eyes");
var eye = 1;
setInterval(function(){
	eye += 1;
	if(eye >= 13){
		eyes.style.display = "none";
		eye = 0;
	}
	else{
		eyes.style.display = "block";
	}
}, 500)


var open = true;
var mouthImg = document.getElementById("closed");
var move;

function StartAnimation(){
	move = setInterval(function(){
		if(open){
			open = false;
			mouthImg.src = "../static/mouthclosed.png"
		}
		else{
			open = true;
			mouthImg.src = "../static/mouthopen.png"
		}
	}, 200)
}
function EndAnimation(){
	running = false;
	clearInterval(move);
	open = false;
	mouthImg.src = "../static/mouthclosed.png"
}