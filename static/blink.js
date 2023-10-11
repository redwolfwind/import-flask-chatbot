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