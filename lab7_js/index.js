function showGraphNoAnimation(fromForGraph, toForGraph, funForGraph, object) {
	xPoint=[];
	yPoint=[];
	for(fromForGraph; fromForGraph<=toForGraph; fromForGraph+=0.01){
		let x;
		x=fromForGraph;
		y=eval(funForGraph);
		xPoint.push(fromForGraph);
		yPoint.push(y);
	}
	
	let points = new Array();
		for(let i=0; i<xPoint.length; i++) {
		points[i] = new Array();
	}


	for (let i = 0; i < xPoint.length; i++) {
		points[i][0]=xPoint[i];
		points[i][1]=yPoint[i];
	}
		
	let options = {
        legend: {       
        	show: true
    	},
		color: "#F2B2F2",
    	label: funForGraph, 
    	data: points, 
    	lines: { show: true, fill: false }
    }

	let outProj=$(object);
	$.plot(outProj, [options]);
}

$('document').ready(function(){
	$('.butProj').on('click', function(){
		let fromForGraph, toForGraph, funForGraph;
		fromForGraph=$('#fromValue').val(); 
		//fromForGraph=0;
		toForGraph=$('.toProj').val();
		//toForGraph=2;
		funForGraph=$('.funProj').val();
		//funForGraph='Math.sin(x)'

		fromForGraph=parseFloat(fromForGraph);
		toForGraph=parseFloat(toForGraph);

		showGraphNoAnimation(fromForGraph, toForGraph, funForGraph,'.outProj');

	});
});