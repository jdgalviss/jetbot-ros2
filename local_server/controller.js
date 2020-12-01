// alert("WebSocket is supported by your Browser!");

// Add key Listener
let playerSpriteX = 0.0;
var steering_ = 0.0;
var throttle_ = 0.0;
var throttle_factor = 0.2;

document.addEventListener('keyup', (e) => {
    if (e.code === "KeyW") throttle_ = 0.0
    else if (e.code === "KeyS") throttle_ = 0.0
    else if (e.code === "KeyA") steering_ = 0.0
    else if (e.code === "KeyD") steering_ = 0.0
    else if (e.code === "KeyE") throttle_factor += 0.1
    else if (e.code === "KeyQ") throttle_factor -= 0.1
    if (throttle_factor > 1.0) throttle_factor = 1.0
    if (throttle_factor < 0.0) throttle_factor = 0.0
    document.getElementById('Throttle_factor').innerHTML = 'throttle_factor = ' + throttle_factor;
    document.getElementById('Steering').innerHTML = 'steering = ' + steering_;
    document.getElementById('Throttle').innerHTML = 'throttle = ' + throttle_ * throttle_factor;

    // Let us open a web socket
    var ws = new WebSocket("ws://192.168.0.167:8765");
    ws.onopen = function () {

        // Web Socket is connected, send data using send()
        //  var msg_to_send = "I am a client sending a msg"
        //  ws.send(msg_to_send);
        //  alert("Message: "+ msg_to_send +" sent");
        var msg = {
            steering: steering_,
            throttle: throttle_ * throttle_factor
        };
        ws.send(JSON.stringify(msg));
    };
//    ws.onclose = function () {
            // websocket is closed.
            //  alert("Connection is closed..."); 
  //  };
});


document.addEventListener('keypress', (e) => {
    if(throttle_ != 1.0 && e.code === "KeyW" || throttle_ != -1.0 && e.code === "KeyS" || steering_ != 1.0 && e.code === "KeyA" || steering_ != -1.0 && e.code === "KeyD" ){
	    if (e.code === "KeyW") throttle_ = 1.0
	    else if (e.code === "KeyS") throttle_ = -1.0
	    else if (e.code === "KeyA") steering_ = 1.0
	    else if (e.code === "KeyD") steering_ = -1.0

	    // alert(e.code);
	    document.getElementById('Steering').innerHTML = 'steering = ' + steering_;
	    document.getElementById('Throttle').innerHTML = 'throttle = ' + throttle_ * throttle_factor;

	    // Let us open a web socket
	    var ws = new WebSocket("ws://192.168.0.167:8765");
	    ws.onopen = function () {

		// Web Socket is connected, send data using send()
		//  var msg_to_send = "I am a client sending a msg"
		//  ws.send(msg_to_send);
		//  alert("Message: "+ msg_to_send +" sent");
		var msg = {
		    steering: steering_,
		    throttle: throttle_ * throttle_factor
		};
		ws.send(JSON.stringify(msg));
	    };
	//    ws.onclose = function () {
		    // websocket is closed.
		    //  alert("Connection is closed..."); 
	  //  };
	}
});


function WebSocketTest() {
    if ("WebSocket" in window) {
        //   alert("WebSocket is supported by your Browser!");

        // Let us open a web socket
        var ws = new WebSocket("ws://192.168.0.167:8765");

        ws.onopen = function () {

            // Web Socket is connected, send data using send()
            //  var msg_to_send = "I am a client sending a msg"
            //  ws.send(msg_to_send);
            //  alert("Message: "+ msg_to_send +" sent");
            var msg = {
                steering: 3.4,
                throttle: -1.2,
            };
            ws.send(JSON.stringify(msg));
        };

        ws.onmessage = function (evt) {
            var received_msg = evt.data;
            //  alert("Message received: " + received_msg);
        };

        ws.onclose = function () {

            // websocket is closed.
            //  alert("Connection is closed..."); 
        };
    } else {

        // The browser doesn't support WebSocket
        alert("WebSocket NOT supported by your Browser!");
    }
}
