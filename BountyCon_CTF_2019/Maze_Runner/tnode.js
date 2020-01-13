var fs = require("fs");

fs.readFile('maze.js', function(err, data) {
	var input = "BountyCon{}"
	var code = data.toString();
	
	let H=0,
	h=1,
	X=0,
	x=1,
	D=1,
	d=0,
	T=0,
	t=L=>L.split("").map(l=>l.charCodeAt(0)),
	B=`${code/*  |%$*/}`.split("\n").map(t),//Maze Code in Array
	b=t(input).reverse();
	

	while(d>=0){
		console.log("--------------------------");
		console.log("h: " + h + " H: " + H + " X: " + X + " x: " + x + " D: " + D + " d: " + d + " T: " + T);
		console.log("B[h][H]: " + B[h][H] + " | " + String.fromCharCode(B[h][H]));
		console.log("B[h][H] & 15: " + (B[h][H] & 15));
		console.log("--------------------------");
		
		[
		(_=>{H+=X*(D-1);h+=x*(D-1);}),
		(_=>{T=x;x=-X;X=T;}),
		(_=>{T=x;x=X;X=-T;}),
		(_=>b.length?(D=b.pop()):d=-2),
		(_=>D^=B[24][2+(d++%31)]^32),
		(_=>{H+=X;h+=x;(D==B[h][H])||(d=-2);}),
		(_=>d=-1),
		(_=>{})
		][B[h][H] & 15]();

		H=(H+31+X) % 31;
		h=(h+B.length+x) % B.length
	}
});