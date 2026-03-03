
var crypto = require('crypto');

var hash = crypto.createHash('sha256');
var i=0;
var OK=1;
var	   txt='text';
data = hash.update(txt+1, 'utf-8');
gen_hash= data.digest('hex');



let startTime = performance.now();




while(OK==1) {
    const hash = crypto.createHash('sha256');
    hash.update('cuvantX' + i);
		patt=hash.digest('hex');
    console.log('hash: '+patt+ '  i='+i);
		i++;
		if(patt.substring(0,6)=="000000")
			OK=0;

	
}
let stopTime = performance.now();
let timeElapsed = stopTime - startTime;

console.log('START:'+ startTime);
console.log('STOP:'+stopTime);

console.log('Timp executie: ' + timeElapsed + ' milisecunde');